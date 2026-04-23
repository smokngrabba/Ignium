import os, sys, time
from utils.builder import build

if __name__ == "__main__":
    try:
        build()
    except KeyboardInterrupt:
        print(f"\n                 \033[31m[\033[0m$\033[31m]\033[0m Aborted.")
    
    sys.stdout.write("\033[?25l")
    for i in range(8, 0, -1):
        sys.stdout.write(f"\r                     \033[37m>\033[0m \033[37mExiting in {i}\033[0m")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\033[?25h")
    sys.exit()
