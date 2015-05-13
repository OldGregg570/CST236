import getpass
import random
import socket
import subprocess
import threading
import time
import os

seq_finder = None
threaded_counter = None
threaded_multer = None
threaded_exper = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "unknown"

    if not output:
        return "unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "unknown"

    if not output:
        return "unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes < 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.001)


def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]


class Counter(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.MAX = 10000000
        super(Counter, self).__init__(*args, **kwargs)
        self.count = 0
        self.val = 0
        self._stop = threading.Event()
        self.times = [0]

    def timed_func(self):
        self.val = 10 + 2

    def stop(self):
        self._stop.set()

    def run(self):
        start_time = time.clock()
        while not self._stop.isSet() and self.count < self.MAX:
            self.count += 1
            self.timed_func()
            self.times.append(time.clock() - start_time)


def count_time(index):
    index = int(index)
    global threaded_counter

    if threaded_counter is None:
        threaded_counter = Counter()
        threaded_counter.start()


    if index > threaded_counter.MAX:
        return "I can't count that high... sorry"
    if index > threaded_counter.count:
        return "Still counting..."

    else:
        return threaded_counter.times[index]


class MultTimer(Counter):
    def __init__(self, *args, **kwargs):
        super(MultTimer, self).__init__(*args, **kwargs)
        self.val = 2

    def timed_func(self):
        self.val = 10*2


class ExpTimer(Counter):
    def __init__(self, *args, **kwargs):
        super(ExpTimer, self).__init__(*args, **kwargs)
        self.val = 2

    def timed_func(self):
        self.val = 10**2





def square_time(index):
    index = int(index)
    global threaded_multer

    if threaded_multer is None:
        threaded_multer = MultTimer()
        threaded_multer.start()

    if index > threaded_multer.MAX:
        return "I can't multiply that high... sorry"
    if index > threaded_multer.count:
        return "Still multiplying..."

    else:
        return threaded_multer.times[index]


def exp_time(index):
    index = int(index)
    global threaded_exper

    if threaded_exper is None:
        threaded_exper = ExpTimer()
        threaded_exper.start()

    if index > threaded_exper.MAX:
        return "I can't exponentiate that high... sorry"
    if index > threaded_exper.count:
        return "Still exponentiating..."

    else:
        return threaded_exper.times[index]





def lc_recurse(directory):
    count = 0
    for d in os.listdir(directory):
        if not d == '.git':
            if not os.path.isdir(os.path.join(directory, d)):
                with open(directory + '/' + d, 'r') as f:
                    for line in f.readlines():
                            count += 1
            else:
                count += lc_recurse(directory + '/' + d)
    return count


def line_count(val):
    return lc_recurse('./')
