# encoding: utf-8
# module zmq.backend.cython._device
# from C:\test.env\lib\site-packages\zmq\backend\cython\_device.pyd
# by generator 1.135
""" Python binding for 0MQ device function. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# functions

def device(device_type, frontend, backend): # real signature unknown; restored from __doc__
    """
    device(device_type, frontend, backend)
    
        Start a zeromq device.
        
        .. deprecated:: libzmq-3.2
            Use zmq.proxy
    
        Parameters
        ----------
        device_type : (QUEUE, FORWARDER, STREAMER)
            The type of device to start.
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
    """
    pass

def proxy(frontend, backend, capture): # real signature unknown; restored from __doc__
    """
    proxy(frontend, backend, capture)
        
        Start a zeromq proxy (replacement for device).
        
        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0
        
        Parameters
        ----------
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
        capture : Socket (optional)
            The Socket instance for capturing traffic.
    """
    pass

# no classes
# variables with complex values

__all__ = [
    'device',
    'proxy',
]

__test__ = {}

