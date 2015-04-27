import logging
import os
from .. import ReqTracer

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.traceability')


class Tracer(Plugin):
    configSection = 'tracer'
    commandLineSwitch = (None, 'trace', 'Req Tracer plugin')

    def __init__(self):
        print "running"

    def stopTestRun(self, event):
        with open('req_out.txt', 'w') as f:
            for id, req in ReqTracer.Requirements.iteritems():
                f.writelines(id + '\t' + req.req_text)