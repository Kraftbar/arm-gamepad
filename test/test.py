import time
import threading

def fun1():
    print("Hello")
    time.sleep(1)
    print("World")

# Create a new thread to run fun1 and start it
fun1_thread = threading.Thread(target=fun1)
fun1_thread.start()

# Continue with the rest of the code while fun1 runs in the background
print(" to everyone in the ")

# Optionally, wait for the fun1 thread to finish before moving on
fun1_thread.join()

