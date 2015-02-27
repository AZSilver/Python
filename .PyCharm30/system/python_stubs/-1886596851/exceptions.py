# encoding: utf-8
# module exceptions
# from (built-in)
# by generator 1.135
"""
Python's standard exception class hierarchy.

Exceptions found here are defined both in the exceptions module and the
built-in namespace.  It is recommended that user-defined exceptions
inherit from Exception.  See the documentation for the exception
inheritance hierarchy.
"""
# no imports

# no functions
# classes

from object import object

class BaseException(object):
    """ Common base class for all exceptions """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __unicode__(self): # known case of exceptions.BaseException.__unicode__
        # no doc
        return u""

    args = property(lambda self: tuple())
    """:type: tuple"""

    message = property(lambda self: '', lambda self, v: None, lambda self: None)
    """:type: string"""


    __dict__ = None # (!) real value is ''


from BaseException import BaseException

class Exception(BaseException):
    """ Common base class for all non-exit exceptions. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Exception import Exception

class StandardError(Exception):
    """
    Base class for all standard Python exceptions that do not represent
    interpreter exiting.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class ArithmeticError(StandardError):
    """ Base class for arithmetic errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class AssertionError(StandardError):
    """ Assertion failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class AttributeError(StandardError):
    """ Attribute not found. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class BufferError(StandardError):
    """ Buffer error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Exception import Exception

class Warning(Exception):
    """ Base class for warning categories. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class BytesWarning(Warning):
    """
    Base class for warnings about bytes and buffer related problems, mostly
    related to conversion from str or comparing to str.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class DeprecationWarning(Warning):
    """ Base class for warnings about deprecated features. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class EnvironmentError(StandardError):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    errno = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception errno

    :type: int
    """

    filename = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception filename

    :type: string
    """

    strerror = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception strerror

    :type: int
    """



from StandardError import StandardError

class EOFError(StandardError):
    """ Read beyond end of file. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from ArithmeticError import ArithmeticError

class FloatingPointError(ArithmeticError):
    """ Floating point operation failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class FutureWarning(Warning):
    """
    Base class for warnings about constructs that will change semantically
    in the future.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from BaseException import BaseException

class GeneratorExit(BaseException):
    """ Request that a generator exit. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class ImportError(StandardError):
    """ Import can't find module, or can't find name in module. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class ImportWarning(Warning):
    """ Base class for warnings about probable mistakes in module imports """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class SyntaxError(StandardError):
    """ Invalid syntax. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    filename = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception filename

    :type: string
    """

    lineno = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception lineno

    :type: int
    """

    msg = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception msg

    :type: string
    """

    offset = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception offset

    :type: int
    """

    print_file_and_line = property(lambda self: True, lambda self, v: None, lambda self: None)
    """exception print_file_and_line

    :type: bool
    """

    text = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception text

    :type: string
    """



from SyntaxError import SyntaxError

class IndentationError(SyntaxError):
    """ Improper indentation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class LookupError(StandardError):
    """ Base class for lookup errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from LookupError import LookupError

class IndexError(LookupError):
    """ Sequence index out of range. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from EnvironmentError import EnvironmentError

class IOError(EnvironmentError):
    """ I/O operation failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from BaseException import BaseException

class KeyboardInterrupt(BaseException):
    """ Program interrupted by user. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from LookupError import LookupError

class KeyError(LookupError):
    """ Mapping key not found. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


from StandardError import StandardError

class MemoryError(StandardError):
    """ Out of memory. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class NameError(StandardError):
    """ Name not found globally. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class RuntimeError(StandardError):
    """ Unspecified run-time error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from RuntimeError import RuntimeError

class NotImplementedError(RuntimeError):
    """ Method or function hasn't been implemented yet. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from EnvironmentError import EnvironmentError

class OSError(EnvironmentError):
    """ OS system call failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from ArithmeticError import ArithmeticError

class OverflowError(ArithmeticError):
    """ Result too large to be represented. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class PendingDeprecationWarning(Warning):
    """
    Base class for warnings about features which will be deprecated
    in the future.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class ReferenceError(StandardError):
    """ Weak ref proxy used after referent went away. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class RuntimeWarning(Warning):
    """ Base class for warnings about dubious runtime behavior. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Exception import Exception

class StopIteration(Exception):
    """ Signal the end from iterator.next(). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class SyntaxWarning(Warning):
    """ Base class for warnings about dubious syntax. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class SystemError(StandardError):
    """
    Internal error in the Python interpreter.
    
    Please report this to the Python maintainer, along with the traceback,
    the Python version, and the hardware/OS platform and version.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from BaseException import BaseException

class SystemExit(BaseException):
    """ Request to exit from the interpreter. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)


from IndentationError import IndentationError

class TabError(IndentationError):
    """ Improper mixture of spaces and tabs. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class TypeError(StandardError):
    """ Inappropriate argument type. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from NameError import NameError

class UnboundLocalError(NameError):
    """ Local name referenced but not bound to a value. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from StandardError import StandardError

class ValueError(StandardError):
    """ Inappropriate argument value (of correct type). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from ValueError import ValueError

class UnicodeError(ValueError):
    """ Unicode related error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from UnicodeError import UnicodeError

class UnicodeDecodeError(UnicodeError):
    """ Unicode decoding error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception encoding"""

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception end"""

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception object"""

    reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception reason"""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception start"""



from UnicodeError import UnicodeError

class UnicodeEncodeError(UnicodeError):
    """ Unicode encoding error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    encoding = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception encoding

    :type: string
    """

    end = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception end

    :type: int
    """

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)
    reason = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception reason

    :type: string
    """

    start = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception start

    :type: int
    """



from UnicodeError import UnicodeError

class UnicodeTranslateError(UnicodeError):
    """ Unicode translation error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    encoding = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception encoding

    :type: string
    """

    end = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception end

    :type: int
    """

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)
    reason = property(lambda self: '', lambda self, v: None, lambda self: None)
    """exception reason

    :type: string
    """

    start = property(lambda self: 0, lambda self, v: None, lambda self: None)
    """exception start

    :type: int
    """



from Warning import Warning

class UnicodeWarning(Warning):
    """
    Base class for warnings about Unicode related problems, mostly
    related to conversion problems.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from Warning import Warning

class UserWarning(Warning):
    """ Base class for warnings generated by user code. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


from OSError import OSError

class WindowsError(OSError):
    """ MS-Windows OS system call failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""

    winerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Win32 exception code"""



from ArithmeticError import ArithmeticError

class ZeroDivisionError(ArithmeticError):
    """ Second argument to a division or modulo operation was zero. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


