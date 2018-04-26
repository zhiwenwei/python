import time
import threading
def _demon():
    for i in range(1,10):
        print(i)
        time.sleep(1)
t1 = threading.Thread(target=_demon)
t1.setDaemon(True)
t1.start()
print("main thread end")