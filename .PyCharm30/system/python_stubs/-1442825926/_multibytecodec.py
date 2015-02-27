# encoding: utf-8
# module _multibytecodec
# from (built-in)
# by generator 1.135
# no doc
# no imports

# functions

def __create_codec(*args, **kwargs): # real signature unknown
    pass

# classes

from .object import object

class MultibyteIncrementalDecoder(object):
    # no doc
    def decode(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""



from .object import object

class MultibyteIncrementalEncoder(object):
    # no doc
    def encode(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""



from .object import object

class MultibyteStreamReader(object):
    # no doc
    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



from .object import object

class MultibyteStreamWriter(object):
    # no doc
    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def writelines(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



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

