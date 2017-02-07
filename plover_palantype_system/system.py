
KEYS = (
    'S-', 'C-', 'P-', 'T-', 'H-', '+-', 'M-', 'F-', 'R-', 'N-', 'L-', 'Y-',
    'O-', 'E-', '-A', '-U',
    'I',
    '-^', '-N', '-L', '-C', '-M', '-F', '-R', '-P', '-T', '-+', '-S', '-H'
)

IMPLICIT_HYPHEN_KEYS = ('O-', 'E-', '-A', '-U', 'I')

SUFFIX_KEYS = ('-S')

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'ULFTS'

ORTHOGRAPHY_RULES = [
    # == +ly ==
    # artistic + ly = artistically
    (r'^(.*[aeiou]c) \^ ly$', r'\1ally'),
        
    # == +ry ==      
    # statute + ry = statutory
    (r'^(.*t)e \^ ry$', r'\1ory'),
        
    # == t +cy ==      
    # frequent + cy = frequency (tcy/tecy removal)
    (r'^(.*[naeiou])te? \^ cy$', r'\1cy'),

    # == +s ==
    # establish + s = establishes (sibilant pluralization)
    (r'^(.*(?:s|sh|x|z|zh)) \^ s$', r'\1es'),
    # speech + s = speeches (soft ch pluralization)
    (r'^(.*(?:oa|ea|i|ee|oo|au|ou|l|n|(?<![gin]a)r|t)ch) \^ s$', r'\1es'),
    # cherry + s = cherries (consonant + y pluralization)
    (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ s$', r'\1ies'),

    # == y ==
    # die+ing = dying
    (r'^(.+)ie \^ ing$', r'\1ying'),
    # metallurgy + ist = metallurgist
    (r'^(.+[cdfghlmnpr])y \^ ist$', r'\1ist'),
    # beauty + ful = beautiful (y -> i)
    (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ ([a-hj-xz].*)$', r'\1i\2'),

    # == e ==
    # write + en = written
    (r'^(.+)te \^ en$', r'\1tten'),
    # free + ed = freed 
    (r'^(.+e)e \^ (e.+)$', r'\1\2'),
    # narrate + ing = narrating (silent e)
    (r'^(.+[bcdfghjklmnpqrstuvwxz])e \^ ([aeiouy].*)$', r'\1\2'),

    # == misc ==
    # defer + ed = deferred (consonant doubling)   XXX monitor(stress not on last syllable)
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([aeiouy].*)$', r'\1\2\2\3'),
]

ORTHOGRAPHY_RULES_ALIASES = {
    'able': 'ible',
}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-': 'a',
        'C-': 'q',
        'P-': '2',
        'T-': 'w',
        'H-': 's',
        '+-': ('m', 'z', 'x', 'c'),
        'M-': '3',
        'F-': 'e',
        'R-': 'd',
        'N-': '4',
        'L-': 'r',
        'Y-': 'f',
        'O-': 'g',
        'E-': 'v',
        '-A': 'h',
        '-U': 'n',
        'I': 'b',
        '-^': (',', '.', '/'),
        '-N': '8',
        '-L': 'u',
        '-C': 'j',
        '-M': '9',
        '-F': 'i',
        '-R': 'k',
        '-P': '0',
        '-T': 'o',
        '-+': 'l',
        '-S': ';',
        '-H': 'p',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('1', '5', '6', '7', 't', 'y', '[', ']', '-', '=', '\'', '\\'),
    },
    'Palantype': {
        'S-': 'S-',
        'C-': 'C-',
        'P-': 'P-',
        'T-': 'T-',
        'H-': 'H-',
        '+-': ('+1-', '+2-'),
        'M-': 'M-',
        'F-': 'F-',
        'R-': 'R-',
        'N-': 'N-',
        'L-': 'L-',
        'Y-': 'Y-',
        'O-': 'O-',
        'E-': 'E-',
        '-A': '-A',
        '-U': '-U',
        'I': 'I',
        '-^': ('-^1', '-^2'),
        '-N': '-N',
        '-L': '-L',
        '-C': '-C',
        '-M': '-M',
        '-F': '-F',
        '-R': '-R',
        '-P': '-P',
        '-T': '-T',
        '-+': '-+',
        '-S': '-S',
        '-H': '-H',
    },
}

DICTIONARIES_ROOT = 'asset:plover_palantype_system:dictionaries'
DEFAULT_DICTIONARIES = (
    'sample.json',
    'user.json'
)
