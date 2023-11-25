import time
import random

def binary_effect():
    for _ in range(10):
        binary_string = ''.join(random.choice('01') for _ in range(50))
        print(binary_string)
        time.sleep(0.1)
    print('\n')

def cool_terminal_start():
    print("=============================================")
    print("|                                           |")
    print("|          Welcome to the Cool Terminal!    |")
    print("|                                           |")
    print("=============================================")
    print("\nInitializing coolness...")

    for _ in range(10):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print('\n')

def cool_terminal_finish():
    for _ in range(10):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print('\n')

    print("=============================================")
    print("|                                           |")
    print("|          Hello world                      |")
    print("|                                           |")
    print("=============================================")


def cool_init():
    cool_terminal_start()
    
    start_time = time.time()

    while time.time() - start_time < 3: 
        binary_effect()
    
    cool_terminal_finish()

if __name__ == "__main__":
    cool_init()