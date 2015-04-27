import logging
import os

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.helloworld')

class HelloWorld(Plugin):
    configSection = 'helloworld'
    commandLineSwitch = (None, 'hello-world', 'First plugin')

    def __init__(self):
        print "running"

    def stopTestRun(self, event):
        print "stopped"