import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
import sys
from subprocess import call
from splinter.browser import Browser

firefox = Browser()

class MdCompileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if isinstance(event, FileModifiedEvent) and event.src_path.endswith('.md'):
            print 'Change in %s detected... Recompiling markdown' % event.src_path.split('/')[-1]
            call(['landslide', sys.argv[1]])
            firefox.visit('file:///' + event.src_path.replace('.md', '.html'))

if __name__ == "__main__":
    event_handler = MdCompileHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()