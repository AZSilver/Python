# encoding: utf-8
# module zmq.backend.cython.utils
# from C:\test.env\lib\site-packages\zmq\backend\cython\utils.pyd
# by generator 1.135
""" 0MQ utils. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import zmq.error as __zmq_error


# functions

def curve_keypair(*args, **kwargs): # real signature unknown
    """
    generate a Z85 keypair for use with zmq.CURVE security
        
        Requires libzmq (≥ 4.0) to have been linked with libsodium.
        
        .. versionadded:: libzmq-4.0
        .. versionadded:: 14.0
        
        Returns
        -------
        (public, secret) : two bytestrings
            The public and private keypair as 40 byte z85-encoded bytestrings.
    """
    pass

def _check_rc(rc, errno=None): # reliably restored by inspect
    """
    internal utility for checking zmq return condition
        
        and raising the appropriate Exception class
    """
    pass

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
        
        raises ZMQVersionError if current zmq version is not at least min_version
        
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

# classes

from object import object

class Stopwatch(object):
    """
    Stopwatch()
    
        A simple stopwatch based on zmq_stopwatch_start/stop.
    
        This class should be used for benchmarking and timing 0MQ code.
    """
    def sleep(self, seconds): # real signature unknown; restored from __doc__
        """
        s.sleep(seconds)
        
                Sleep for an integer number of seconds.
        """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        s.start()
        
                Start the stopwatch.
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """
        s.stop()
        
                Stop the stopwatch.
                
                Returns
                -------
                t : unsigned long int
                    the number of microseconds since ``start()`` was called.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


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
    'curve_keypair',
    'Stopwatch',
]

__test__ = {}

