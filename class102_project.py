import sys
import time 
import random, os, shutil, watchdog.observers 
import Observer, watchdog.events, FileSystemEventHandler

from_dir = "<Set path for tracking file system events>"

class FileEventHandler:
    def on_created():
        print("file created")
    def on_modified():
        print("file modified")
    def on_moved():
        print("file moved")
    def on_deleted():
        print("file deleted")

object 
eventhandler = FileEventHandler
observer = Observer
schedule(observer)
start(observer)