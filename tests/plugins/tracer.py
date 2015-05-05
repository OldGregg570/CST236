import logging
from .. import ReqTracer

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.traceability')


class Tracer(Plugin):
    configSection = 'tracer'
    commandLineSwitch = (None, 'tracer', 'Req Tracer plugin')

    uncovered_requirements = []

    def __init__(self):
        print "running"

    def stopTestRun(self, event):
        with open('req_out.txt', 'w') as f:
            for id, req in sorted(ReqTracer.Requirements.iteritems()):
                f.writelines("REQ ID: {0}\n".format(id))
                f.writelines("\tREQ:{0}".format(req.req_text))

                # if len(req.func_name) == 0:
                #     f.writelines("\t{{ REQUIREMENT NOT COVERED }}\n\n")
                #     self.uncovered_requirements.append(id)
                # else:
                f.writelines("\tCOVERED IN: {0}\n\n".format(req.func_name))

            l = len(ReqTracer.Requirements)
            f.writelines("{0} / {1} requirements covered ...\n".format(l - len(self.uncovered_requirements), l))

            if len(self.uncovered_requirements) == 0:

                f.writelines("Requirements completely covered")
            else:
                f.writelines("ERROR: Requirements not covered\n\tReq ids: {0}".format(str(self.uncovered_requirements)))