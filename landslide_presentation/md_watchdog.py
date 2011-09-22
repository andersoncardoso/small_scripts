import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
from subprocess import call

class MdCompileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print 'Change in %s detected... Recompiling markdown' % sys.argv[1]
        call(['landslide', sys.argv[1]])

if __name__ == "__main__":
    event_handler = MdCompileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=sys.argv[1], recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()