import os
import multiprocessing

def child_process():
    print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=child_process)
    p.start()

    print(f"Parent process: PID = {os.getpid()}, Child PID = {p.pid}")

    p.join()
