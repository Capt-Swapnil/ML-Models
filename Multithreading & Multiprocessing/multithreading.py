import threading 
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_abc():
    for letter in "abc":
        time.sleep(2)
        print(f"Letter:{letter}")
#creating two threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_abc)



t = time.time()

t1.start()
t2.start()

#wait for threads to complete 
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)