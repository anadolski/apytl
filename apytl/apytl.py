#!/usr/bin/env python

"""
A logging package implementation of another progress bar I have seen 
floating around the web. I will link to it if I can find it, because it 
is excellent. One advantage of this implementation is that the progress 
bar will be correctly piped to STDOUT even if it is called via a shell 
script.

I haven't checked how this behaves when logging to a file. Caveat 
emptor, or something.
"""

import logging
import sys

_EMOJIS = {
    'eggplant'     : '\\U0001F346',
    'middlefinger' : '\\U0001F595',
    'poop'         : '\\U0001F4A9',
    'skullnbones'  : '\\u2620',
}

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logginghandler = logging.StreamHandler()
logginghandler.terminator = ''

def parse_unicode(string):
    """
    Parse a unicode string of the form UXXXXXXXX or uXXXX
    """
    pass

def drawbar(iteration, total, prefix='Progress', suffix='Complete',
           decimal=1, barsize=50, fill=None, fillfactor=1):
    """
    Draw a progress bar on the terminal.

    Parameters
    ----------
    iteration : int
        The current iteration number. Note that it is assumed that your
        counter starts at zero.
    total : int
        The total number of iterations that will be executed.
    prefix : str, optional
        An string to place at the left side of the bar. Default is
        'Progress'.
    suffix : str, optional
        A string to place at the right side of the bar, Default is
        'Complete'.
    decimal : int, optional
        The number of decimal places to which the completion progress
        should be calculated. Default it 1.
    barsize : int, optional
        The size of the progress bar in units of characters. Default is
        50.
    fill : str or None, optional
        The character to use to fill the bar and represent completion.
        If `None`, then `#` will be used to fill the bar. Any single-width
        alphanumeric or punctuation character may be passed.

        USE THE FOLLOWING FEATURE AT YOUR OWN PERIL:
        Choose from a preselected set of unicode emojis:
            `eggplant`, `poop`, `skullnbones`
        or pass your own unicode.

        Due to the variety of terminal emulators, font support, and display
        and window managers it's impossible to know how well (if at all) this
        will function on your system. If passing a custom emoji, you will have
        to use a format Python will recognize. For instance:
            `\\U0001F4A9` --> poop emoji
            `\\u2620`     --> skull and crossbones emoji
        Note the difference in capitalization and the zero-padding.
    fillfactor : int, optional
        A padding factor used to accommodate unicode emojis. Default is `1`,
        which shouldn't need to change for English single-width characters and
        punctuation.
    """
    iteration = iteration + 1
    str_format = '{0:.' + str(decimal) + 'f}'
    percent = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(barsize * iteration / float(total * fillfactor)))
    bar = fill * filled_length + '-' * ((barsize - int(filled_length * fillfactor)))
    # Note that most of the arguments passed to LogRecord are filler. We only
    # really care about the last three.
    msg = '\r{} |{}| {}{} {}'.format(prefix, bar, percent, '%', suffix)
    record = logging.LogRecord('bar', 2, '.', 1, msg, None, None)
    logginghandler.emit(record)
    if iteration == total:
        logginghandler.terminator = '\n'
        endrecord = logging.LogRecord('end', 2, '.', 1, '%s', (' '), None)
        logginghandler.emit(endrecord)
        logginghandler.terminator = ''
    return
