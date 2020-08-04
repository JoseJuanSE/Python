from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler 
import os
import json

class MyHandler(FileSystemEventHandler):
        def on_modified(self,event):
                for filename in os.listdir(folder_to_track):
                        src = folder_to_track + "/" + filename
                        new_destination = folder_destination + "/" + filename
                        os.rename(src,new_destination)

folder_to_track = 'C:/Users/FSE/Desktop/new'
folder_destination = 'C:/Users/FSE/Desktop/old'
event_hadler = MyHandler()
observer = Observer()
observer.schedule(event_hadler,folder_to_track, recursive = True)
observer.start()

try: 
        while True:
                time.sleep(10)
except KeyboardInterrupt:
        observer.stop()
observer.join()