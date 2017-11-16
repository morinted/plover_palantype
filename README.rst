Plover Palantype
================

Possum Palantype support for Plover.

Activating Palantype
~~~~~~~~~~~~~~~~~~~~

After installing this plugin, you need to turn on Palantype in Plover:

1. In Plover's configuration, go to the ``Systems`` tab, and change the active system to ``Possum Palantype``.
2. In Plover's machine tab, select the ``Palantype`` machine and ensure the settings point to your Palantype machine.

    - "Palantype" machine type in Plover is what other CAT software calls "Palantype B".
    - If you have a *Neutrino* machine, you may need to select the "Gemini PR" protocol.
    - If you do not own a Palantype machine, you can use an N-key rollover keyboard instead, as outlined in `this tutorial <http://www.openstenoproject.org/palantype/tutorial/2016/08/21/learn-palantype.html>`_.
    - At this time, other protocols are not supported.

3. Plover will install ``sample.json`` and ``user.json`` as dictionaries. You can remove the sample if you already have your own dictionary or want to start from scratch. Plover accepts ``json`` and ``RTF`` dictionaries. It is recommended to use ``user.json`` when adding new strokes.
4. Note: at the moment, **only** ``ULFTS`` is supported to backspace the last stroke.

Common Commands
~~~~~~~~~~~~~~~

It would be a good time to define some custom commands that make using Plover much easier!

The "Add Definition" button lets you define a new dictionary entry. The first recommended entry is one that summons this dialog!

- ``T+UPT``: ``{PLOVER:ADD_TRANSLATION}`` (think "dictionary update")

Some other useful translations for you to define (come up with your own strokes):

- ``{-|}`` capitalize next word
- ``{^^}`` suppress space
- ``{#right}``, ``{#left}``, ``{#up}``, ``{#down}`` press arrow keys: right, left, up, down (recommendation is to create an arrow-key cluster on one hand with a chord on the other)
- ``{#control(c)}`` copy on Windows, Linux, or ``{#command(c)}`` for Mac
- ``{#control(v)}`` paste on Windows, Linux, or ``{#command(v)}`` for Mac
- ``{#control(z)}`` undo on Windows, Linux, or ``{#command(z)}`` for Mac
- ``{#tab}`` press the tab key
- ``{#alt(tab tab)}`` change application on Windows
- ``{#backspace}`` press the backspace key
- ``{#escape}`` press the escape key
- ``{#return}`` press the return/enter key
- ``{^\n^}{-|}`` new line, capitalize
- ``{^\n\n^}{-|}`` new paragraph, capitalize