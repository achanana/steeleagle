import threading
import ctypes

class Task(threading.Thread):

    def __init__(self, drone, cloudlet, **kwargs):
        threading.Thread.__init__(self)
        self.drone = drone
        self.cloudlet = cloudlet
        self.kwargs = kwargs

    # Run is already an abstract method derived from Runnable.
    # It will be implemented separately by each task.
    
    def pause(self):
        pass

    def stop(self):
        thread_id = self.get_ident()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            raise RuntimeError('Error killing task thread')

    def resume(self):
        pass
