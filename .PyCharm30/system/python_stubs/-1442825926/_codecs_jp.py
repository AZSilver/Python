# encoding: utf-8
# module _codecs_jp
# from (built-in)
# by generator 1.135
# no doc
# no imports

# functions

def getcodec(*args, **kwargs): # real signature unknown
    """  """
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

__map_cp932ext = None # (!) real value is ''

__map_jisx0208 = None # (!) real value is ''

__map_jisx0212 = None # (!) real value is ''

__map_jisx0213_1_bmp = None # (!) real value is ''

__map_jisx0213_1_emp = None # (!) real value is ''

__map_jisx0213_2_bmp = None # (!) real value is ''

__map_jisx0213_2_emp = None # (!) real value is ''

__map_jisx0213_bmp = None # (!) real value is ''

__map_jisx0213_emp = None # (!) real value is ''

__map_jisx0213_pair = None # (!) real value is ''

__map_jisxcommon = None # (!) real value is ''

__spec__ = None # (!) real value is ''

