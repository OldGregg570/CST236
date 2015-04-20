import Queue
import logging


class Event():
    event_count = 0

    def __init__(self, message, source=None, level='info'):
        self._message = message
        self._source = source
        self._level = level
        self._id = Event.event_count

        Event.event_count += 1

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
                ret_val += '\n Pos:  ' + str(self._source.position) + ' ' + AlertSystem.units + ' units'
                ret_val += '\n Dest: ' + str(self._source.destination) + ' ' + AlertSystem.units + ' units'


        return ret_val


class AlertSystem():
    """
    Alert system class
    """
    units = 'Meters'
    def __init__(self, units='Meters'):
        logging.info('Initializing alert system')
        self.options_displayed = False
        self.__alerts = Queue.Queue()
        AlertSystem.units = units

    @property
    def options_displayed(self):
        return self.options_displayed

    def put(self, event):
        if 'ENTer the Trees' == event._message:
            self.kill_all_orcs()
        elif 'X' == event.message:
            self.quit()
        elif '?' == event.message:
            self.display_options()
        else:
            self.__alerts.put(event)

    def get(self):
        if not self.__alerts.empty():
            return self.__alerts.get()

    def quit(self):
        logging.info('exiting the game')
        self._log_dump()

    def kill_all_orcs(self):
        logging.info('killing all orcs')
        self._log_dump()

    def display_options(self):
        logging.info('displaying options')
        self.options_displayed = True

    def _log_dump(self, filter_predicate=None):
        logging.info('dumping Alert Queue ...')
        while not self.__alerts.empty():
            e = self.__alerts.get()
            if filter_predicate:
                if filter_predicate(e):
                    if e.level == 'info':
                        logging.info(e.to_string())
                    if e.level == 'warn':
                        logging.warn(e.to_string())




