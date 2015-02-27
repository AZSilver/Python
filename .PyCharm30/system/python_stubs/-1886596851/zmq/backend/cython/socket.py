# encoding: utf-8
# module zmq.backend.cython.socket
# from C:\test.env\lib\site-packages\zmq\backend\cython\socket.pyd
# by generator 1.135
""" 0MQ Socket class. """

# imports
import random as random # C:\Python27\Lib\random.pyc
import struct as struct # C:\Python27\Lib\struct.pyc
import zmq as zmq # C:\test.env\lib\site-packages\zmq\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import codecs as codecs # C:\test.env\lib\codecs.pyc
import cPickle as cPickle # <module 'cPickle' (built-in)>
import zmq.utils.jsonapi as jsonapi # C:\test.env\lib\site-packages\zmq\utils\jsonapi.pyc
import cPickle as pickle # <module 'cPickle' (built-in)>
import copy as copy_mod # C:\Python27\Lib\copy.pyc
import sys as sys # <module 'sys' (built-in)>
import zmq.backend.cython.constants as constants # C:\test.env\lib\site-packages\zmq\backend\cython\constants.pyd
import time as time # <module 'time' (built-in)>
import zmq.error as __zmq_error


# Variables with simple values

AFFINITY = 4

BACKLOG = 19

CONFLATE = 54

CONNECT_RID = -1

CURVE = 2

CURVE_PUBLICKEY = 48
CURVE_SECRETKEY = 49
CURVE_SERVER = 47
CURVE_SERVERKEY = 50

DEALER = 5

DELAY_ATTACH_ON_CONNECT = 39

DONTWAIT = 1
DOWNSTREAM = -1

EADDRINUSE = 156384717
EADDRNOTAVAIL = 156384718
EAFNOSUPPORT = 156384723
EAGAIN = 11

ECONNABORTED = 156384725
ECONNREFUSED = 156384719
ECONNRESET = 156384726

EFAULT = 14
EFSM = 156384763

EHOSTUNREACH = 156384729

EINPROGRESS = 156384720
EINVAL = 22

EMSGSIZE = 156384722
EMTHREAD = 156384766

ENETDOWN = 156384716
ENETRESET = 156384730
ENETUNREACH = 156384724
ENOBUFS = 156384715
ENOCOMPATPROTO = 156384764
ENODEV = 19
ENOMEM = 12
ENOTCONN = 156384727
ENOTSOCK = 156384721
ENOTSUP = 156384713

EPROTONOSUPPORT = 156384714

ETERM = 156384765
ETIMEDOUT = 156384728

EVENTS = 15

EVENT_ACCEPTED = 32

EVENT_ACCEPT_FAILED = 64

EVENT_ALL = 2047

EVENT_BIND_FAILED = 16

EVENT_CLOSED = 128

EVENT_CLOSE_FAILED = 256

EVENT_CONNECTED = 1

EVENT_CONNECT_DELAYED = 2
EVENT_CONNECT_RETRIED = 4

EVENT_DISCONNECTED = 512
EVENT_LISTENING = 8

EVENT_MONITOR_STOPPED = 1024

FAIL_UNROUTABLE = 33

FD = 14

FORWARDER = 2

HAUSNUMERO = 156384712

HWM = -1

IDENTITY = 5

IMMEDIATE = 39

IO_THREADS = 1

IO_THREADS_DFLT = 1

IPC_FILTER_GID = -1
IPC_FILTER_PID = -1
IPC_FILTER_UID = -1

IPC_PATH_MAX_LEN = 0

IPV4ONLY = 31
IPV6 = 42

LAST_ENDPOINT = 32

LINGER = 17

MAXMSGSIZE = 22

MAX_SOCKETS = 2

MAX_SOCKETS_DFLT = 1023

MCAST_LOOP = -1

MECHANISM = 43

MORE = 1

MULTICAST_HOPS = 25

NOBLOCK = 1

NULL = 0

PAIR = 0

PLAIN = 1

PLAIN_PASSWORD = 46
PLAIN_SERVER = 44
PLAIN_USERNAME = 45

POLLERR = 4
POLLIN = 1
POLLOUT = 2

PROBE_ROUTER = 51

PUB = 1
PULL = 7
PUSH = 8

QUEUE = 3

RATE = 8

RCVBUF = 12
RCVHWM = 24
RCVMORE = 13
RCVTIMEO = 27

RECONNECT_IVL = 18

RECONNECT_IVL_MAX = 21

RECOVERY_IVL = 9

RECOVERY_IVL_MSEC = -1

REP = 4
REQ = 3

REQ_CORRELATE = 52
REQ_RELAXED = 53

ROUTER = 6

ROUTER_BEHAVIOR = 33
ROUTER_HANDOVER = -1
ROUTER_MANDATORY = 33
ROUTER_RAW = 41

SNDBUF = 11
SNDHWM = 23
SNDMORE = 2
SNDTIMEO = 28

STREAM = 11
STREAMER = 1

SUB = 2
SUBSCRIBE = 6

SWAP = -1

TCP_ACCEPT_FILTER = 38

TCP_KEEPALIVE = 34

TCP_KEEPALIVE_CNT = 35
TCP_KEEPALIVE_IDLE = 36
TCP_KEEPALIVE_INTVL = 37

TOS = -1

TYPE = 16

UNSUBSCRIBE = 7

UPSTREAM = -1

VERSION = 40004

VERSION_MAJOR = 4
VERSION_MINOR = 0
VERSION_PATCH = 4

XPUB = 9

XPUB_VERBOSE = 40

XSUB = 10

ZAP_DOMAIN = 55

# functions

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
        
        raises ZMQVersionError if current zmq version is not at least min_version
        
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

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


from object import object

class Socket(object):
    """
    Socket(context, socket_type)
    
        A 0MQ socket.
    
        These objects will generally be constructed via the socket() method of a Context object.
        
        Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.
        
        Parameters
        ----------
        context : Context
            The 0MQ Context this Socket belongs to.
        socket_type : int
            The socket type, which can be any of the 0MQ socket types: 
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.
        
        See Also
        --------
        .Context.socket : method for creating a socket bound to a Context.
    """
    def bind(self, addr): # real signature unknown; restored from __doc__
        """
        s.bind(addr)
        
                Bind the socket to an address.
        
                This causes the socket to listen on a network port. Sockets on the
                other side of this connection will use ``Socket.connect(addr)`` to
                connect to this socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported include
                    tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def close(self, linger=None): # real signature unknown; restored from __doc__
        """
        s.close(linger=None)
        
                Close the socket.
                
                If linger is specified, LINGER sockopt will be set prior to closing.
        
                This can be called to close the socket by hand. If this is not
                called, the socket will automatically be closed when it is
                garbage collected.
        """
        pass

    def connect(self, addr): # real signature unknown; restored from __doc__
        """
        s.connect(addr)
        
                Connect to a remote 0MQ socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def disconnect(self, addr): # real signature unknown; restored from __doc__
        """
        s.disconnect(addr)
        
                Disconnect from a remote 0MQ socket (undoes a call to connect).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        s.get(option)
        
                Get the value of a socket option.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IDENTITY, HWM, LINGER, FD, EVENTS
        
                Returns
                -------
                optval : int or bytes
                    The value of the option as a bytestring or int.
        """
        pass

    def monitor(self, addr, flags): # real signature unknown; restored from __doc__
        """
        s.monitor(addr, flags)
        
                Start publishing socket events on inproc.
                See libzmq docs for zmq_monitor for details.
                
                While this function is available from libzmq 3.2,
                pyzmq cannot parse monitor messages from libzmq prior to 4.0.
                
                .. versionadded: libzmq-3.2
                .. versionadded: 14.0
                
                Parameters
                ----------
                addr : str
                    The inproc url used for monitoring.
                events : int [default: zmq.EVENT_ALL]
                    The zmq event bitmask for which events will be sent to the monitor.
        """
        pass

    def recv(self, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.recv(flags=0, copy=True, track=False)
        
                Receive a message.
        
                Parameters
                ----------
                flags : int
                    Any supported flag: NOBLOCK. If NOBLOCK is set, this method
                    will raise a ZMQError with EAGAIN if a message is not ready.
                    If NOBLOCK is not set, then this method will block until a
                    message arrives.
                copy : bool
                    Should the message be received in a copying or non-copying manner?
                    If False a Frame object is returned, if True a string copy of
                    message is returned.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                msg : bytes, Frame
                    The received message frame.  If `copy` is False, then it will be a Frame,
                    otherwise it will be bytes.
                    
                Raises
                ------
                ZMQError
                    for any of the reasons zmq_msg_recv might fail.
        """
        pass

    def send(self, data, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.send(data, flags=0, copy=True, track=False)
        
                Send a message on this socket.
        
                This queues the message to be sent by the IO thread at a later time.
        
                Parameters
                ----------
                data : object, str, Frame
                    The content of the message.
                flags : int
                    Any supported flag: NOBLOCK, SNDMORE.
                copy : bool
                    Should the message be sent in a copying or non-copying manner.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                None : if `copy` or not track
                    None if message was sent, raises an exception otherwise.
                MessageTracker : if track and not copy
                    a MessageTracker object, whose `pending` property will
                    be True until the send is completed.
                
                Raises
                ------
                TypeError
                    If a unicode object is passed
                ValueError
                    If `track=True`, but an untracked Frame is passed.
                ZMQError
                    If the send does not succeed for any reason.
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        s.set(option, optval)
        
                Set socket options.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD
                
                optval : int or bytes
                    The value of the option to set.
        """
        pass

    def unbind(self, addr): # real signature unknown; restored from __doc__
        """
        s.unbind(addr)
                
                Unbind from an address (undoes a call to bind).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def __init__(self, context, socket_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq socket"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


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


class ZMQBindError(__zmq_error.ZMQBaseError):
    """
    An error for ``Socket.bind_to_random_port()``.
        
        See Also
        --------
        .Socket.bind_to_random_port
    """
    def __init__(self, *args, **kwargs): # real signature unknown
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
    'Socket',
    'IPC_PATH_MAX_LEN',
]

__test__ = {}

