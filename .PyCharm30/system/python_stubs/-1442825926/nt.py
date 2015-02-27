# encoding: utf-8
# module nt
# from (built-in)
# by generator 1.135
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""
# no imports

# Variables with simple values

F_OK = 0

O_APPEND = 8
O_BINARY = 32768
O_CREAT = 256
O_EXCL = 1024
O_NOINHERIT = 128
O_RANDOM = 16
O_RDONLY = 0
O_RDWR = 2
O_SEQUENTIAL = 32

O_SHORT_LIVED = 4096

O_TEMPORARY = 64
O_TEXT = 16384
O_TRUNC = 512
O_WRONLY = 1

P_DETACH = 4
P_NOWAIT = 1
P_NOWAITO = 3
P_OVERLAY = 2
P_WAIT = 0

R_OK = 4

TMP_MAX = 32767

W_OK = 2

X_OK = 1

# functions

def abort(): # real signature unknown; restored from __doc__
    """
    abort() -> does not return!
    
    Abort the interpreter immediately.  This 'dumps core' or otherwise fails
    in the hardest way possible on the hosting operating system.
    """
    pass

def access(*args, **kwargs): # real signature unknown
    """
    Use the real uid/gid to test for access to a path.
    
      path
        Path to be tested; can be string, bytes, or open-file-descriptor int.
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.
    """
    pass

def chdir(path): # real signature unknown; restored from __doc__
    """
    chdir(path)
    
    Change the current working directory to the specified path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def chmod(path, mode, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
    
    Change the access permissions of a file.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chmod will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def close(fd): # real signature unknown; restored from __doc__
    """
    close(fd)
    
    Close a file descriptor (for low level IO).
    """
    pass

def closerange(fd_low, fd_high): # real signature unknown; restored from __doc__
    """
    closerange(fd_low, fd_high)
    
    Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    """
    pass

def cpu_count(): # real signature unknown; restored from __doc__
    """
    cpu_count() -> integer
    
    Return the number of CPUs in the system, or None if this value cannot be
    established.
    """
    return 0

def device_encoding(fd): # real signature unknown; restored from __doc__
    """
    device_encoding(fd) -> str
    
    Return a string describing the encoding of the device
    if the output is a terminal; else return None.
    """
    return ""

def dup(fd): # real signature unknown; restored from __doc__
    """
    dup(fd) -> fd2
    
    Return a duplicate of a file descriptor.
    """
    pass

def dup2(old_fd, new_fd): # real signature unknown; restored from __doc__
    """
    dup2(old_fd, new_fd)
    
    Duplicate file descriptor.
    """
    pass

def execv(path, args): # real signature unknown; restored from __doc__
    """
    execv(path, args)
    
    Execute an executable path with arguments, replacing current process.
    
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def execve(path, args, env): # real signature unknown; restored from __doc__
    """
    execve(path, args, env)
    
    Execute a path with arguments and environment, replacing current process.
    
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    
    On some platforms, you may specify an open file descriptor for path;
      execve will execute the program the file descriptor is open to.
      If this functionality is unavailable, using it raises NotImplementedError.
    """
    pass

def fstat(fd): # real signature unknown; restored from __doc__
    """
    fstat(fd) -> stat result
    
    Like stat(), but for an open file descriptor.
    Equivalent to stat(fd=fd).
    """
    pass

def fsync(fildes): # real signature unknown; restored from __doc__
    """
    fsync(fildes)
    
    force write of file with filedescriptor to disk.
    """
    pass

def getcwd(): # real signature unknown; restored from __doc__
    """
    getcwd() -> path
    
    Return a unicode string representing the current working directory.
    """
    pass

def getcwdb(): # real signature unknown; restored from __doc__
    """
    getcwdb() -> path
    
    Return a bytes string representing the current working directory.
    """
    pass

def getlogin(): # real signature unknown; restored from __doc__
    """
    getlogin() -> string
    
    Return the actual login name.
    """
    return ""

def getpid(): # real signature unknown; restored from __doc__
    """
    getpid() -> pid
    
    Return the current process id
    """
    pass

def getppid(): # real signature unknown; restored from __doc__
    """
    getppid() -> ppid
    
    Return the parent's process id.  If the parent process has already exited,
    Windows machines will still return its id; others systems will return the id
    of the 'init' process (1).
    """
    pass

def get_handle_inheritable(fd): # real signature unknown; restored from __doc__
    """
    get_handle_inheritable(fd) -> bool
    
    Get the close-on-exe flag of the specified file descriptor.
    """
    return False

def get_inheritable(fd): # real signature unknown; restored from __doc__
    """
    get_inheritable(fd) -> bool
    
    Get the close-on-exe flag of the specified file descriptor.
    """
    return False

def get_terminal_size(*args, **kwargs): # real signature unknown
    """
    Return the size of the terminal window as (columns, lines).
    
    The optional argument fd (default standard output) specifies
    which file descriptor should be queried.
    
    If the file descriptor is not connected to a terminal, an OSError
    is thrown.
    
    This function will only be defined if an implementation is
    available for this system.
    
    shutil.get_terminal_size is the high-level function which should 
    normally be used, os.get_terminal_size is the low-level implementation.
    """
    pass

def isatty(fd): # real signature unknown; restored from __doc__
    """
    isatty(fd) -> bool
    
    Return True if the file descriptor 'fd' is an open file descriptor
    connected to the slave end of a terminal.
    """
    return False

def kill(pid, sig): # real signature unknown; restored from __doc__
    """
    kill(pid, sig)
    
    Kill a process with a signal.
    """
    pass

def link(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
    
    Create a hard link to a file.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    If follow_symlinks is False, and the last element of src is a symbolic
      link, link will create a link to the symbolic link itself instead of the
      file the link points to.
    src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
      platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    """
    pass

def listdir(path='.'): # real signature unknown; restored from __doc__
    """
    listdir(path='.') -> list_of_filenames
    
    Return a list containing the names of the files in the directory.
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    
    path can be specified as either str or bytes.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    On some platforms, path may also be specified as an open file descriptor;
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.
    """
    pass

def lseek(fd, pos, how): # real signature unknown; restored from __doc__
    """
    lseek(fd, pos, how) -> newpos
    
    Set the current position of a file descriptor.
    Return the new cursor position in bytes, starting from the beginning.
    """
    pass

def lstat(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lstat(path, *, dir_fd=None) -> stat result
    
    Like stat(), but do not follow symbolic links.
    Equivalent to stat(path, follow_symlinks=False).
    """
    pass

def mkdir(path, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    mkdir(path, mode=0o777, *, dir_fd=None)
    
    Create a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    
    The mode argument is ignored on Windows.
    """
    pass

def open(path, flags, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    open(path, flags, mode=0o777, *, dir_fd=None)
    
    Open a file for low level IO.  Returns a file handle (integer).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def pipe(): # real signature unknown; restored from __doc__
    """
    pipe() -> (read_end, write_end)
    
    Create a pipe.
    """
    pass

def putenv(key, value): # real signature unknown; restored from __doc__
    """
    putenv(key, value)
    
    Change or add an environment variable.
    """
    pass

def read(fd, buffersize): # real signature unknown; restored from __doc__
    """
    read(fd, buffersize) -> bytes
    
    Read a file descriptor.
    """
    return b""

def readlink(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    readlink(path, *, dir_fd=None) -> path
    
    Return a string representing the path to which the symbolic link points.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def remove(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    remove(path, *, dir_fd=None)
    
    Remove a file (same as unlink()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def rename(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    
    Rename a file or directory.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def replace(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    
    Rename a file or directory, overwriting the destination.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def rmdir(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rmdir(path, *, dir_fd=None)
    
    Remove a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def set_handle_inheritable(fd, inheritable): # real signature unknown; restored from __doc__
    """
    set_handle_inheritable(fd, inheritable)
    
    Set the inheritable flag of the specified handle.
    """
    pass

def set_inheritable(fd, inheritable): # real signature unknown; restored from __doc__
    """
    set_inheritable(fd, inheritable)
    
    Set the inheritable flag of the specified file descriptor.
    """
    pass

def spawnv(mode, path, args): # real signature unknown; restored from __doc__
    """
    spawnv(mode, path, args)
    
    Execute the program 'path' in a new process.
    
        mode: mode of process creation
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def spawnve(mode, path, args, env): # real signature unknown; restored from __doc__
    """
    spawnve(mode, path, args, env)
    
    Execute the program 'path' in a new process.
    
        mode: mode of process creation
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    """
    pass

def startfile(filepath, operation=None): # real signature unknown; restored from __doc__
    """
    startfile(filepath [, operation]) - Start a file with its associated
    application.
    
    When "operation" is not specified or "open", this acts like
    double-clicking the file in Explorer, or giving the file name as an
    argument to the DOS "start" command: the file is opened with whatever
    application (if any) its extension is associated.
    When another "operation" is given, it specifies what should be done with
    the file.  A typical operation is "print".
    
    startfile returns as soon as the associated application is launched.
    There is no option to wait for the application to close, and no way
    to retrieve the application's exit status.
    
    The filepath is relative to the current directory.  If you want to use
    an absolute path, make sure the first character is not a slash ("/");
    the underlying Win32 ShellExecute function doesn't work if it is.
    """
    pass

def stat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path.
    
      path
        Path to be examined; can be string, bytes, or open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be a relative string; path will then be relative to
        that directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    It's an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    """
    pass

def stat_float_times(newval=None): # real signature unknown; restored from __doc__
    """
    stat_float_times([newval]) -> oldval
    
    Determine whether os.[lf]stat represents time stamps as float objects.
    If newval is True, future calls to stat() return floats, if it is False,
    future calls return ints. 
    If newval is omitted, return the current setting.
    """
    pass

def strerror(code): # real signature unknown; restored from __doc__
    """
    strerror(code) -> string
    
    Translate an error code to a message string.
    """
    return ""

def symlink(src, dst, target_is_directory=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    symlink(src, dst, target_is_directory=False, *, dir_fd=None)
    
    Create a symbolic link pointing to src named dst.
    
    target_is_directory is required on Windows if the target is to be
      interpreted as a directory.  (On Windows, symlink requires
      Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
      target_is_directory is ignored on non-Windows platforms.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def system(command): # real signature unknown; restored from __doc__
    """
    system(command) -> exit_status
    
    Execute the command (a string) in a subshell.
    """
    pass

def times(): # real signature unknown; restored from __doc__
    """
    times() -> times_result
    
    Return an object containing floating point numbers indicating process
    times.  The object behaves like a named tuple with these fields:
      (utime, stime, cutime, cstime, elapsed_time)
    """
    return times_result

def umask(new_mask): # real signature unknown; restored from __doc__
    """
    umask(new_mask) -> old_mask
    
    Set the current numeric umask and return the previous umask.
    """
    pass

def unlink(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unlink(path, *, dir_fd=None)
    
    Remove a file (same as remove()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def urandom(n): # real signature unknown; restored from __doc__
    """
    urandom(n) -> str
    
    Return n random bytes suitable for cryptographic use.
    """
    return ""

def utime(path, times=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)
    Set the access and modified time of path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    
    If times is not None, it must be a tuple (atime, mtime);
        atime and mtime should be expressed as float seconds since the epoch.
    If ns is not None, it must be a tuple (atime_ns, mtime_ns);
        atime_ns and mtime_ns should be expressed as integer nanoseconds
        since the epoch.
    If both times and ns are None, utime uses the current time.
    Specifying tuples for both times and ns is an error.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, utime will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path
      as an open file descriptor.
    dir_fd and follow_symlinks may not be available on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def waitpid(pid, options): # real signature unknown; restored from __doc__
    """
    waitpid(pid, options) -> (pid, status << 8)
    
    Wait for completion of a given process.  options is ignored on Windows.
    """
    pass

def write(fd, data): # real signature unknown; restored from __doc__
    """
    write(fd, data) -> byteswritten
    
    Write bytes to a file descriptor.
    """
    pass

def _exit(status): # real signature unknown; restored from __doc__
    """
    _exit(status)
    
    Exit to the system with specified status, without normal exit processing.
    """
    pass

def _getdiskusage(path): # real signature unknown; restored from __doc__
    """
    _getdiskusage(path) -> (total, free)
    
    Return disk usage statistics about the given path as (total, free) tuple.
    """
    pass

def _getfinalpathname(*args, **kwargs): # real signature unknown
    pass

def _getfullpathname(*args, **kwargs): # real signature unknown
    pass

def _getvolumepathname(*args, **kwargs): # real signature unknown
    """ Return volume mount point of the specified path. """
    pass

def _isdir(*args, **kwargs): # real signature unknown
    """ Return true if the pathname refers to an existing directory. """
    pass

# classes

from .Exception import Exception

class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""

    winerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Win32 exception code"""



from .tuple import tuple

class statvfs_result(tuple):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
    """
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

    f_bavail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_bfree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_bsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_favail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_ffree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_frsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_namemax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    n_fields = 10
    n_sequence_fields = 10
    n_unnamed_fields = 0


from .tuple import tuple

class stat_result(tuple):
    """
    stat_result: Result from stat, fstat, or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
    """
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

    st_atime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access"""

    st_atime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access in nanoseconds"""

    st_ctime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change"""

    st_ctime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change in nanoseconds"""

    st_dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """device"""

    st_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group ID of owner"""

    st_ino = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inode"""

    st_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """protection bits"""

    st_mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification"""

    st_mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification in nanoseconds"""

    st_nlink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of hard links"""

    st_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total size, in bytes"""

    st_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user ID of owner"""


    n_fields = 16
    n_sequence_fields = 10
    n_unnamed_fields = 3


from .tuple import tuple

class terminal_size(tuple):
    """ A tuple of (columns, lines) for holding terminal window size """
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

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the terminal window in characters"""

    lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the terminal window in characters"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0


from .tuple import tuple

class times_result(tuple):
    """
    times_result: Result from os.times().
    
    This object may be accessed either as a tuple of
      (user, system, children_user, children_system, elapsed),
    or via the attributes user, system, children_user, children_system,
    and elapsed.
    
    See os.times for more information.
    """
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

    children_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time of children"""

    children_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time of children"""

    elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """elapsed time since an arbitrary point in the past"""

    system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time"""

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


from .tuple import tuple

class uname_result(tuple):
    """
    uname_result: Result from os.uname().
    
    This object may be accessed either as a tuple of
      (sysname, nodename, release, version, machine),
    or via the attributes sysname, nodename, release, version, and machine.
    
    See os.uname for more information.
    """
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

    machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hardware identifier"""

    nodename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of machine on network (implementation-defined)"""

    release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system release"""

    sysname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system name"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system version"""


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

environ = {
    'ALLUSERSPROFILE': 'C:\\ProgramData',
    'ANT_HOME': 'C:\\apache-ant-1.8.4',
    'APPDATA': 'C:\\Users\\de\\AppData\\Roaming',
    'COMPUTERNAME': 'DE-PC',
    'ComSpec': 'C:\\Windows\\system32\\cmd.exe',
    'CommonProgramFiles': 'C:\\Program Files (x86)\\Common Files',
    'CommonProgramFiles(x86)': 'C:\\Program Files (x86)\\Common Files',
    'CommonProgramW6432': 'C:\\Program Files\\Common Files',
    'ExtraPuTTY': 'C:\\Program Files\\ExtraPuTTY\\Bin',
    'ExtraPuTTY_BOXSIZE': 'AUTO',
    'ExtraPuTTY_MODE': 'DIR_MODE',
    'FP_NO_HOST_CHECK': 'NO',
    'HOMEDRIVE': 'C:',
    'HOMEPATH': '\\Users\\de',
    'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.7.0_13',
    'LOCALAPPDATA': 'C:\\Users\\de\\AppData\\Local',
    'LOGONSERVER': '\\\\DE-PC',
    'MOZ_PLUGIN_PATH': 'C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\plugins\\',
    'NUMBER_OF_PROCESSORS': '8',
    'OS': 'Windows_NT',
    'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.RB;.RBW;.PY',
    'PROCESSOR_ARCHITECTURE': 'x86',
    'PROCESSOR_ARCHITEW6432': 'AMD64',
    'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel',
    'PROCESSOR_LEVEL': '6',
    'PROCESSOR_REVISION': '3a09',
    'PSModulePath': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\',
    'PUBLIC': 'C:\\Users\\Public',
    'Path': 'C:\\Python34;C:\\Program Files\\Common Files\\Microsoft Shared\\Windows Live;C:\\Program Files (x86)\\Common Files\\Microsoft Shared\\Windows Live;C:\\Program Files (x86)\\HP SimplePass\\x64;C:\\Program Files (x86)\\HP SimplePass\\;C:\\Ruby200-x64\\bin;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\HP SimplePass\\x64;C:\\Program Files (x86)\\HP SimplePass\\;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Broadcom\\Broadcom 802.11\\Driver;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\2.0\\bin\\x86;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\2.0\\bin\\x64;C:\\glassfish3\\jdk\\bin;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\2.0\\bin\\x86;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\2.0\\bin\\x64;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\apache-ant-1.8.4\\bin;C:\\Program Files\\MySQL\\MySQL Server 5.5\\bin;C:\\Program Files (x86)\\Livestreamer;C:\\Program Files (x86)\\Windows Live\\Shared;C:\\Program Files (x86)\\Git\\cmd',
    'ProgramData': 'C:\\ProgramData',
    'ProgramFiles': 'C:\\Program Files (x86)',
    'ProgramFiles(x86)': 'C:\\Program Files (x86)',
    'ProgramW6432': 'C:\\Program Files',
    'SESSIONNAME': 'Console',
    'SystemDrive': 'C:',
    'SystemRoot': 'C:\\Windows',
    'TEMP': 'C:\\Users\\de\\AppData\\Local\\Temp',
    'TMP': 'C:\\Users\\de\\AppData\\Local\\Temp',
    'USERDOMAIN': 'de-PC',
    'USERNAME': 'de',
    'USERPROFILE': 'C:\\Users\\de',
    'asl.log': 'Destination=file',
    'windir': 'C:\\Windows',
    'windows_tracing_flags': '3',
    'windows_tracing_logfile': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log',
}

_have_functions = [
    'MS_WINDOWS',
]

__spec__ = None # (!) real value is ''

