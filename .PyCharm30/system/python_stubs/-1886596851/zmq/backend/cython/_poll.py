# encoding: utf-8
# module zmq.backend.cython._poll
# from C:\test.env\lib\site-packages\zmq\backend\cython\_poll.pyd
# by generator 1.135
""" 0MQ polling related functions and classes. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>

# functions

def zmq_poll(sockets, timeout=-1): # real signature unknown; restored from __doc__
    """
    zmq_poll(sockets, timeout=-1)
    
        Poll a set of 0MQ sockets, native file descs. or sockets.
    
        Parameters
        ----------
        sockets : list of tuples of (socket, flags)
            Each element of this list is a two-tuple containing a socket
            and a flags. The socket may be a 0MQ socket or any object with
            a ``fileno()`` method. The flags can be zmq.POLLIN (for detecting
            for incoming messages), zmq.POLLOUT (for detecting that send is OK)
            or zmq.POLLIN|zmq.POLLOUT for detecting both.
        timeout : int
            The number of milliseconds to poll for. Negative means no timeout.
    """
    pass

# no classes
# variables with complex values

int_t = (
    int,
    long,
)

__all__ = [
    'zmq_poll',
]

__test__ = {}

