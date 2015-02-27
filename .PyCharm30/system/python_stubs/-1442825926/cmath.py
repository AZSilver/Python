# encoding: utf-8
# module cmath
# from (built-in)
# by generator 1.135
"""
This module is always available. It provides access to mathematical
functions for complex numbers.
"""
# no imports

# Variables with simple values
e = 2.718281828459045

pi = 3.141592653589793

# functions

def acos(x): # real signature unknown; restored from __doc__
    """
    acos(x)
    
    Return the arc cosine of x.
    """
    pass

def acosh(x): # real signature unknown; restored from __doc__
    """
    acosh(x)
    
    Return the hyperbolic arccosine of x.
    """
    pass

def asin(x): # real signature unknown; restored from __doc__
    """
    asin(x)
    
    Return the arc sine of x.
    """
    pass

def asinh(x): # real signature unknown; restored from __doc__
    """
    asinh(x)
    
    Return the hyperbolic arc sine of x.
    """
    pass

def atan(x): # real signature unknown; restored from __doc__
    """
    atan(x)
    
    Return the arc tangent of x.
    """
    pass

def atanh(x): # real signature unknown; restored from __doc__
    """
    atanh(x)
    
    Return the hyperbolic arc tangent of x.
    """
    pass

def cos(x): # real signature unknown; restored from __doc__
    """
    cos(x)
    
    Return the cosine of x.
    """
    pass

def cosh(x): # real signature unknown; restored from __doc__
    """
    cosh(x)
    
    Return the hyperbolic cosine of x.
    """
    pass

def exp(x): # real signature unknown; restored from __doc__
    """
    exp(x)
    
    Return the exponential value e**x.
    """
    pass

def isfinite(z): # real signature unknown; restored from __doc__
    """
    isfinite(z) -> bool
    Return True if both the real and imaginary parts of z are finite, else False.
    """
    return False

def isinf(z): # real signature unknown; restored from __doc__
    """
    isinf(z) -> bool
    Checks if the real or imaginary part of z is infinite.
    """
    return False

def isnan(z): # real signature unknown; restored from __doc__
    """
    isnan(z) -> bool
    Checks if the real or imaginary part of z not a number (NaN)
    """
    return False

def log(x, base=None): # real signature unknown; restored from __doc__
    """
    log(x[, base]) -> the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.
    """
    pass

def log10(x): # real signature unknown; restored from __doc__
    """
    log10(x)
    
    Return the base-10 logarithm of x.
    """
    pass

def phase(z): # real signature unknown; restored from __doc__
    """
    phase(z) -> float
    
    Return argument, also known as the phase angle, of a complex.
    """
    return 0.0

def polar(z): # real signature unknown; restored from __doc__
    """
    polar(z) -> r: float, phi: float
    
    Convert a complex from rectangular coordinates to polar coordinates. r is
    the distance from 0 and phi the phase angle.
    """
    pass

def rect(r, phi): # real signature unknown; restored from __doc__
    """
    rect(r, phi) -> z: complex
    
    Convert from polar coordinates to rectangular coordinates.
    """
    pass

def sin(x): # real signature unknown; restored from __doc__
    """
    sin(x)
    
    Return the sine of x.
    """
    pass

def sinh(x): # real signature unknown; restored from __doc__
    """
    sinh(x)
    
    Return the hyperbolic sine of x.
    """
    pass

def sqrt(x): # real signature unknown; restored from __doc__
    """
    sqrt(x)
    
    Return the square root of x.
    """
    pass

def tan(x): # real signature unknown; restored from __doc__
    """
    tan(x)
    
    Return the tangent of x.
    """
    pass

def tanh(x): # real signature unknown; restored from __doc__
    """
    tanh(x)
    
    Return the hyperbolic tangent of x.
    """
    pass

# classes

from .object import object

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """ Load a built-in module. """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

