# encoding: utf-8
# module zmq.backend.cython.context
# from C:\test.env\lib\site-packages\zmq\backend\cython\context.pyd
# by generator 1.135
""" 0MQ Context class. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import zmq.error as __zmq_error


# Variables with simple values

_instance = None

# no functions
# classes

from object import object

class Context(object):
    """
    Context(io_threads=1)
    
        Manage the lifecycle of a 0MQ context.
    
        Parameters
        ----------
        io_threads : int
            The number of IO threads.
    """
    def destroy(self, linger=None): # real signature unknown; restored from __doc__
        """
        ctx.destroy(linger=None)
                
                Close all sockets associated with this context, and then terminate
                the context. If linger is specified,
                the LINGER sockopt of the sockets will be set prior to closing.
                
                .. warning::
                
                    destroy involves calling ``zmq_close()``, which is **NOT** threadsafe.
                    If there are active sockets in other threads, this must not be called.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        ctx.get(option)
        
                Get the value of a context option.
        
                See the 0MQ API documentation for zmq_ctx_get
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
                    
                Returns
                -------
                optval : int
                    The value of the option as an integer.
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        ctx.set(option, optval)
        
                Set a context option.
        
                See the 0MQ API documentation for zmq_ctx_set
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
                
                optval : int
                    The value of the option to set.
        """
        pass

    def term(self): # real signature unknown; restored from __doc__
        """
        ctx.term()
        
                Close or terminate the context.
                
                This can be called to close the context by hand. If this is not called,
                the context will automatically be closed when it is garbage collected.
        """
        pass

    def __init__(self, io_threads=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq context"""

    _handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq context"""


    __pyx_vtable__ = None # (!) real value is ''


class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    errno = None


# variables with complex values

__all__ = [
    'Context',
]

__test__ = {}

