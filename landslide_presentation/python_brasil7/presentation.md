python - watchdog
================= 

-----
python - watchdog
=================

* https://github.com/gorakhargosh/watchdog

* Motivation: coffeescript, markdown, haml, etc 

* Python API library and shell utilities to monitor file system events.

* Cross platform API
    * mac/bsd : FSEvents, kqueue
    * linux: inotify
    * windows: ?? (but works)
    * fallback: polling (slow and not recommended)

-----
how to use
===========

* Create an instance of the watchdog.observers.Observer thread class.
* Implement a subclass of event handler (FileSystemEventHandler, LoggingEventHandler, etc)
* Schedule monitoring a path with the observer instance attaching the event handler.
* Start the observer thread and wait for it generate events.

* By default, an watchdog.observers.Observer instance will not monitor sub-directories.
* recursive=True in the call to watchdog.observers.Observer.schedule() to ensure monitoring entire directory trees.

------

example
=======

<br/><br/>

    !python
        import time
        from watchdog.observers import Observer
        from watchdog.events import LoggingEventHandler

        if __name__ == "__main__":
            event_handler = LoggingEventHandler()
            observer = Observer()
            observer.schedule(event_handler, path='.', recursive=True)
            observer.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()
            
--------

example - this presentation
===========================

    !python
        import time
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler, FileModifiedEvent
        import sys
        from subprocess import call

        class MdCompileHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if isinstance(event, FileModifiedEvent) and event.src_path.endswith('.md'):
                    print 'Change in %s detected... Recompiling markdown' % event.src_path.split('/')[-1]
                    call(['landslide', sys.argv[1]])

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
            
------

thanks =] !!  <br/><br/> github.com/gorakhargosh/watchdog
============             ================================