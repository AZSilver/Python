# encoding: utf-8
# module winsound
# from C:\Python34\DLLs\winsound.pyd
# by generator 1.135
"""
PlaySound(sound, flags) - play a sound
SND_FILENAME - sound is a wav file name
SND_ALIAS - sound is a registry sound association name
SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC
SND_MEMORY - sound is a memory image of a wav file
SND_PURGE - stop all instances of the specified sound
SND_ASYNC - PlaySound returns immediately
SND_NODEFAULT - Do not play a default beep if the sound can not be found
SND_NOSTOP - Do not interrupt any sounds currently playing
SND_NOWAIT - Return immediately if the sound driver is busy

Beep(frequency, duration) - Make a beep through the PC speaker.
"""
# no imports

# Variables with simple values

MB_ICONASTERISK = 64
MB_ICONEXCLAMATION = 48
MB_ICONHAND = 16
MB_ICONQUESTION = 32
MB_OK = 0

SND_ALIAS = 65536
SND_APPLICATION = 128
SND_ASYNC = 1
SND_FILENAME = 131072
SND_LOOP = 8
SND_MEMORY = 4
SND_NODEFAULT = 2
SND_NOSTOP = 16
SND_NOWAIT = 8192
SND_PURGE = 64

# functions

def Beep(frequency, duration): # real signature unknown; restored from __doc__
    """
    Beep(frequency, duration) - a wrapper around the Windows Beep API
    
    The frequency argument specifies frequency, in hertz, of the sound.
    This parameter must be in the range 37 through 32,767.
    The duration argument specifies the number of milliseconds.
    """
    pass

def MessageBeep(x): # real signature unknown; restored from __doc__
    """ MessageBeep(x) - call Windows MessageBeep(x). x defaults to MB_OK. """
    pass

def PlaySound(sound, flags): # real signature unknown; restored from __doc__
    """
    PlaySound(sound, flags) - a wrapper around the Windows PlaySound API
    
    The sound argument can be a filename, data, or None.
    For flag values, ored together, see module documentation.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

