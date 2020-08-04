from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import time
import os
import json

def ext(st):
        r=""
        for i in range(len(st)-1,0,-1):
                if st[i]=='.': 
                        r+=st[i]
                        break
                r+=st[i]
        return r[::-1]

class MyHandler(FileSystemEventHandler):
        i=1
        def on_modified(self,event):
                for filename in os.listdir(folder_to_track):
                        new_name = "archivo" + str(self.i) + ext(filename)
                        exist = os.path.isfile(folder_destination +'/'+new_name)
                        while exist:
                                self.i+=1
                                new_name = "archivo" + str(self.i) + ext(filename)
                                exist = os.path.isfile(folder_destination +'/'+new_name)
                        
                        src = folder_to_track + "/" + filename
                        new_destination = folder_destination + "/" + new_name
                        os.rename(src,new_destination)

#here your folders directions
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
