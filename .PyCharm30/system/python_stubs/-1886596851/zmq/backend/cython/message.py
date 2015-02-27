# encoding: utf-8
# module zmq.backend.cython.message
# from C:\test.env\lib\site-packages\zmq\backend\cython\message.pyd
# by generator 1.135
""" 0MQ Message related classes. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import time as time # <module 'time' (built-in)>
import zmq as zmq # C:\test.env\lib\site-packages\zmq\__init__.pyc
import threading as __threading


# Variables with simple values

gc = None

# no functions
# classes

from object import object

class basestring(object):
    """ Type basestring cannot be instantiated; it is the base for str and unicode. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from basestring import basestring

class bytes(basestring):
    """
    str(object) -> string
    
    Return a nice string representation of the object.
    If the argument is a string, the return value is the same object.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> string
        
        Return a copy of the string S with only its first character
        capitalized.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> string
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.decode([encoding[,errors]]) -> object
        
        Decodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
        as well as any other name registered with codecs.register_error that is
        able to handle UnicodeDecodeErrors.
        """
        return object()

    def encode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.encode([encoding[,errors]]) -> object
        
        Encodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that is able to handle UnicodeEncodeErrors.
        """
        return object()

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=None): # real signature unknown; restored from __doc__
        """
        S.expandtabs([tabsize]) -> string
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub [,start [,end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> string
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub [,start [,end]]) -> int
        
        Like S.find() but raise ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> string
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> string
        
        Return S left-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> string
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> string or unicode
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> string
        
        Return a copy of string S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub [,start [,end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub [,start [,end]]) -> int
        
        Like S.rfind() but raise ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> string
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.rsplit([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string, starting at the end of the string and working
        to the front.  If maxsplit is given, at most maxsplit splits are
        done. If sep is not specified or is None, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> string or unicode
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def split(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.split([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are removed
        from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> string or unicode
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> string
        
        Return a copy of the string S with uppercase characters
        converted to lowercase and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> string
        
        Return a titlecased version of S, i.e. words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        return ""

    def translate(self, table, deletechars=None): # real signature unknown; restored from __doc__
        """
        S.translate(table [,deletechars]) -> string
        
        Return a copy of the string S, where all characters occurring
        in the optional argument deletechars are removed, and the
        remaining characters have been mapped through the given
        translation table, which must be a string of length 256 or None.
        If the table argument is None, no translation is applied and
        the operation simply removes the characters in deletechars.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> string
        
        Return a copy of the string S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> string
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width.  The string S is never truncated.
        """
        return ""

    def _formatter_field_name_split(self, *args, **kwargs): # real signature unknown
        pass

    def _formatter_parser(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> string
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class Event(__threading._Verbose):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def isSet(self, *args, **kwargs): # real signature unknown
        pass

    def is_set(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def wait(self, *args, **kwargs): # real signature unknown
        pass

    def _reset_internal_locks(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


from object import object

class Message(object):
    """
    Frame(data=None, track=False)
    
        A zmq message Frame class for non-copy send/recvs.
    
        This class is only needed if you want to do non-copying send and recvs.
        When you pass a string to this class, like ``Frame(s)``, the 
        ref-count of `s` is increased by two: once because the Frame saves `s` as 
        an instance attribute and another because a ZMQ message is created that
        points to the buffer of `s`. This second ref-count increase makes sure
        that `s` lives until all messages that use it have been sent. Once 0MQ
        sends all the messages and it doesn't need the buffer of s, 0MQ will call
        ``Py_DECREF(s)``.
    
        Parameters
        ----------
    
        data : object, optional
            any object that provides the buffer interface will be used to
            construct the 0MQ message data.
        track : bool [default: False]
            whether a MessageTracker_ should be created to track this object.
            Tracking a message has a cost at creation, because it creates a threadsafe
            Event object.
    """
    def get(self, option): # real signature unknown; restored from __doc__
        """
        Frame.get(option)
                
                Get a Frame option.
                
                See the 0MQ API documentation for zmq_msg_get
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        """
        pass

    def set(self, option, value): # real signature unknown; restored from __doc__
        """
        Frame.set(option, value)
                
                Set a Frame option.
                
                See the 0MQ API documentation for zmq_msg_set
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        Create a shallow copy of the message.
        
                This does not copy the contents of the Frame, just the pointer.
                This will increment the 0MQ ref count of the message, but not
                the ref count of the Python object. That is only done once when
                the Python is first turned into a 0MQ message.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ Enforce signature """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return the length of the message in bytes. """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return the str form of the message. """
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A read-only buffer view of the message contents."""

    bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message content as a Python bytes object.

        The first time this property is accessed, a copy of the message 
        contents is made. From then on that same copy of the message is
        returned.
        """

    more = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


Frame = Message


from object import object

class MessageTracker(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from basestring import basestring

class unicode(basestring):
    """
    unicode(string [, encoding[, errors]]) -> object
    
    Create a new Unicode object from the given encoded string.
    encoding defaults to the current default string encoding.
    errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> unicode
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return u""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> unicode
        
        Return S centered in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return u""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        Unicode string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def decode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.decode([encoding[,errors]]) -> string or unicode
        
        Decodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
        as well as any other name registered with codecs.register_error that is
        able to handle UnicodeDecodeErrors.
        """
        return ""

    def encode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.encode([encoding[,errors]]) -> string or unicode
        
        Encodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return ""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=None): # real signature unknown; restored from __doc__
        """
        S.expandtabs([tabsize]) -> unicode
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return u""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub [,start [,end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> unicode
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return u""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub [,start [,end]]) -> int
        
        Like S.find() but raise ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> unicode
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return u""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> int
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return 0

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> unicode
        
        Return a copy of the string S converted to lowercase.
        """
        return u""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> unicode
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        return u""

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> unicode
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return u""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub [,start [,end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub [,start [,end]]) -> int
        
        Like S.rfind() but raise ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> unicode
        
        Return S right-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return u""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.rsplit([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> unicode
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        return u""

    def split(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.split([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> unicode
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is a str, it will be converted to unicode before stripping
        """
        return u""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> unicode
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return u""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> unicode
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return u""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> unicode
        
        Return a copy of the string S, where all characters have been mapped
        through the given translation table, which must be a mapping of
        Unicode ordinals to Unicode ordinals, Unicode strings or None.
        Unmapped characters are left untouched. Characters mapped to None
        are deleted.
        """
        return u""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> unicode
        
        Return a copy of S converted to uppercase.
        """
        return u""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> unicode
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return u""

    def _formatter_field_name_split(self, *args, **kwargs): # real signature unknown
        pass

    def _formatter_parser(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> unicode
        
        Return a formatted version of S as described by format_spec.
        """
        return u""

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, string, encoding=None, errors=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


# variables with complex values

__all__ = [
    'Frame',
    'Message',
]

__test__ = {}

