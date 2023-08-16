from interfaces.Task import Task
import threading
import json
import time

class DetectTask(Task, threading.Thread):

    def __init__(self, drone, cloudlet, **kwargs):
        threading.Thread.__init__(self)
        super().__init__(drone, cloudlet, **kwargs)

    def run(self):
        try:
            self.cloudlet.switchModel(self.kwargs["model"])
            coords = json.loads(self.kwargs["coords"])
            self.drone.setGimbalPose(0.0, float(self.kwargs["gimbal_pitch"]), 0.0)
            hover_delay = int(self.kwargs["hover_delay"])
            for dest in coords:
                lng = dest["lng"]
                lat = dest["lat"]
                alt = dest["alt"]
                self.drone.moveTo(lat, lng, alt)
                time.sleep(hover_delay)
        except Exception as e:
            print(e)


