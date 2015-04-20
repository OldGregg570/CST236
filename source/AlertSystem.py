import Queue
import logging


class Event():
    def __init__(self, message, source=None, level='info'):
        self._message = message
        self._source = source
        self._level = level

    @property
    def message(self):
        return self._message

    @property
    def level(self):
        return self._level

    @property
    def source(self):
        return self._source

    def to_string(self):
        ret_val = self._message

        if self._source:
            ret_val += ' from ' + str(self._source)

            if self._source.position and self._source.destination:
                ret_val += '\n Pos:  ' + self._source.position
                ret_val += '\n Dest: ' + self._source.destination


        return ret_val


class AlertSystem():
    """
    Alert system class
    """
    def __init__(self):
        self.__alerts = Queue.Queue()

    def put(self, event):
        if 'X' == event.message:
            self.quit()
        else:
            self.__alerts.put(event)

    def get(self):
        if not self.__alerts.empty():
            return self.__alerts.get()

    def quit(self):
        logging.info('exiting the game')
        self._log_dump()

    def _log_dump(self, src_filter=None):
        while not self.__alerts.empty():
            e = self.__alerts.get()
            if type(e.source) == src_filter:
                if e.level == 'info':
                    log = logging.info
                if e.level == 'warning':
                    log = logging.warn

                log(e.to_string())



