# encoding: utf-8
# module _lsprof
# from (built-in)
# by generator 1.135
""" Fast profiler """
# no imports

# no functions
# classes

from .object import object

class Profiler(object):
    """
    Profiler(custom_timer=None, time_unit=None, subcalls=True, builtins=True)
    
        Builds a profiler object using the specified timer function.
        The default timer is a fast built-in one based on real time.
        For custom timer functions returning integers, time_unit can
        be a float specifying a scale (i.e. how long each integer unit
        is, in seconds).
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear()
        
        Clear all profiling information collected so far.
        """
        pass

    def disable(self): # real signature unknown; restored from __doc__
        """
        disable()
        
        Stop collecting profiling information.
        """
        pass

    def enable(self, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        """
        enable(subcalls=True, builtins=True)
        
        Start collecting profiling information.
        If 'subcalls' is True, also records for each function
        statistics separated according to its current caller.
        If 'builtins' is True, records the time spent in
        built-in functions separately from their caller.
        """
        pass

    def getstats(self): # real signature unknown; restored from __doc__
        """
        getstats() -> list of profiler_entry objects
        
        Return all information collected by the profiler.
        Each profiler_entry is a tuple-like object with the
        following attributes:
        
            code          code object
            callcount     how many times this was called
            reccallcount  how many times called recursively
            totaltime     total time in this entry
            inlinetime    inline time in this entry (not in subcalls)
            calls         details of the calls
        
        The calls attribute is either None or a list of
        profiler_subentry objects:
        
            code          called code object
            callcount     how many times this is called
            reccallcount  how many times this is called recursively
            totaltime     total time spent in this call
            inlinetime    inline time (not in further subcalls)
        """
        return []

    def __init__(self, custom_timer=None, time_unit=None, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


from .tuple import tuple

class profiler_entry(tuple):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this was called"""

    calls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """details of the calls"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time in this entry (not in subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time in this entry"""


    n_fields = 6
    n_sequence_fields = 6
    n_unnamed_fields = 0


from .tuple import tuple

class profiler_subentry(tuple):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """called code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time (not in further subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time spent in this call"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


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

