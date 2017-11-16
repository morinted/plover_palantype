# -*- coding: utf-8 -*-

from time import sleep
from six import iterbytes
import plover.machine.base
from plover import log

STENO_KEY_CHART = (
    ('M-', '+2-', '+1-', 'H-', 'T-', 'P-', 'S-', 'C-'),
    ('-A', 'E-', 'O-', 'Y-', 'L-', 'N-', 'R-', 'F-'),
    ('-M', '-C', '-L', '-N', '-^2', '-^1', 'I', '-U'),
    ('', '-S', '-H', '-+', '-T', '-P', '-R', '-F'),
)

# This sequence *seems* arbitrary, but it is really what is sent by CAT software.
# The machine doesn't give any response before or during the sequence, unfortunately.
REALTIME_COMMANDS = [0x81, 0x91, 0x90, 0x93, 0xAA]
REQUEST_READ = bytearray(0x80)
END = bytearray(0x95)


class Palantype(plover.machine.base.SerialStenotypeBase):

    KEYS_LAYOUT = '''
           P- M- N-         -N -M -P
        C- T- F- L-         -L -F -T -H
        S- H- R- Y- O- I -A -C -R -+ -S
          +1-  +2-  E- I -U  -^1  -^2
    '''

    def __init__(self, params):
        super(Palantype, self).__init__(params)

    def run(self):
        settings = self.serial_port.getSettingsDict()
        settings['timeout'] = 0.01
        self.serial_port.applySettingsDict(settings)
        for command in REALTIME_COMMANDS:
            log.debug('Palantype: sending %s', str(command))
            self.serial_port.write(bytearray(command))
            sleep(0.5)
        self._ready()
        while not self.finished.isSet():
            if not self.serial_port.inWaiting():
                self.serial_port.write(REQUEST_READ)
                # Request a read 5 times a second
                sleep(0.2)

            raw = self.serial_port.read(5)
            if raw is None:
                continue
            log.debug('Palantype: read %s', raw)
            try:
                # Look for start of chord
                stroke_beginning = raw.index(1)
            except ValueError:
                pass
            else:
                # Trim anything else
                raw = raw[stroke_beginning:]
                if len(raw) < 5:
                    # Read more if it's an incomplete chord
                    raw += self.serial_port.read(5 - len(raw))
                if len(raw) == 5:
                    keys = self._parse_packet(raw)
                    steno_keys = self.keymap.keys_to_actions(keys)
                    if steno_keys:
                        self._notify(steno_keys)

        if self.serial_port:
            self.serial_port.write(END)

    @staticmethod
    def _parse_packet(packet):
        assert packet[0] == 1, 'Palantype packet is missing chord beginning'
        assert len(packet) == 5, 'Palantype packet is not 5 bytes'
        keys = []
        # Packet is a byte array with 4 bytes of data
        for i, byte in enumerate(iterbytes(packet[1:])):
            map = STENO_KEY_CHART[i]
            for j in range(8):
                if not byte >> j & 1:
                    key = map[-j + 7]
                    if key:
                        keys.append(key)
        return keys
