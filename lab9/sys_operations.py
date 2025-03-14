import os
import sys
import platform
import socket
import multiprocessing as mp

def child_process():
    """Function for the child process."""
    print("Child process ID:", os.getpid())

def child_file_process(fd):
    """Function for file handling in the child process."""
    print("Child Process ID:", os.getpid())
    os.lseek(fd, 0, os.SEEK_SET)
    print("File content (child process):", os.read(fd, 100).decode())
    os.close(fd)

def main():
    """Main function to handle system operations."""
    print("Machine type:", platform.machine())
    print("Processor type:", platform.processor())

    # Set socket timeout
    socket.setdefaulttimeout(50)
    print("Default socket timeout:", socket.getdefaulttimeout())

    print("Operating System:", os.name)
    print("Current Process ID:", os.getpid())

    # Forking a new process (Only for Unix-based systems)
    if os.name != 'nt':  # Unix-based systems
        pid = os.fork()
        if pid == 0:
            print("Child process ID:", os.getpid())
            os._exit(0)
        else:
            print("Parent process ID:", os.getpid())
            os.wait()
    else:
        # Windows alternative using multiprocessing
        context = mp.get_context('spawn')
        p = context.Process(target=child_process)
        p.start()
        p.join()

    # File handling using `os`
    file_name = "fdpractice.txt"

    # Open file for writing and reading
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

    # Write to the file
    os.write(fd, b"Some string to write to the file\n")

    # Fork a new process (Unix) or use multiprocessing (Windows)
    if os.name != 'nt':  # Unix-based systems
        pid = os.fork()
        if pid == 0:
            print("Child Process ID:", os.getpid())
            os.lseek(fd, 0, os.SEEK_SET)  # Move file pointer to start
            print("File content (child process):", os.read(fd, 100).decode())
            os.close(fd)
            os._exit(0)
        else:
            print("Parent Process ID:", os.getpid())
            os.wait()
            os.close(fd)
    else:  # Windows multiprocessing approach
        p = context.Process(target=child_file_process, args=(fd,))
        p.start()
        p.join()
        os.close(fd)

if __name__ == '__main__':
    main()
