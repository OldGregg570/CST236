from unittest import TestCase
import getpass
import time
from tests.Tracer import requirements
from main import Interface
import pyTona.answer_funcs as funcs
import pylab as plt


Q = lambda n: "What is {0} in binary?".format(n)

exp_time = None
mul_time = None
add_time = None
fib_time = None
cnt_time = None

class TestLabFive(TestCase):
    interface = Interface()
    # TODO: Figure out why add_answer is so slow on my machine. Is making this untestable
    # @requirements(['#0030'])
    # def test_million_qna(self):
    #     """
    #     The system shall be capable of storing at least 1,000,000 questions and answers
    #     """
    #     for n in range(1000000):
    #         self.interface.ask(Q(n))
    #         self.interface.add_answer(bin(n))
    #
    #     pass

    @requirements(['#0031'])
    def test_write_under_five_ms(self):
        """
        The system shall store answers in under 5 ms
        """
        total_time = 0
        trials = 100
        for n in range(trials):
            self.interface.ask(Q(n))
            start = time.clock()
            self.interface.teach(bin(n))
            total_time += time.clock() - start

        self.assertLess(total_time / float(trials), 5)

        pass

    @requirements(['#0032'])
    def test_read_under_five_ms(self):
        """
        The system shall be able to retrieve a response in under 5 ms
        """
        total_time = 0
        trials = 100
        for n in range(trials):
            start = time.clock()
            self.interface.ask("asdfasdfasdf")
            total_time += time.clock() - start

        self.assertLess(total_time / float(trials), 5)
        pass

    # TODO: figure out why seq_finder is NoneType
    @requirements(['#0033'])
    def test_stop_generate(self):
        """
        The system shall stop generating Fibonacci sequence numbers once it has identified the first 1,000 numbers
        """
        running = True
        while running:
            answer = self.interface.ask("What is the 1000 digit of the fibonacci sequence?")
            try:
                int(answer)
                running = False
            except:
                pass
        funcs.seq_finder.stop()
        pass

    @requirements(['#0034'])
    def test_fib_thousand_in_minute(self):
        """
        The system shall generate the first 1,000 Fibonacci sequence numbers in under 60 seconds
        """
        global fib_time
        running = True
        start = time.clock()
        while running:
            answer = self.interface.ask("What is the 1000 digit of the fibonacci sequence?")
            try:
                int(answer)
                running = False
            except:
                pass
        fib_time = time.clock() - start
        self.assertLess(fib_time, 60000)
        funcs.seq_finder.stop()
        pass


class TestLabFiveAdditionalReqs(TestCase):
    interface = Interface()
    @requirements(['#0035'])
    def test_counting(self):
        """
        The system shall respond to the question "How long does it take you to add <number> numbers?"
        with a positive float.
        """
        running = True
        while running:
            answer = self.interface.ask("How long does it take you to add 100000 numbers?")
            try:
                int(answer)
                running = False
            except:
                pass
        self.assertGreater(answer, 0)
        funcs.threaded_counter.stop()
        pass

    @requirements(['#0036'])
    def test_count_performance(self):
        """
        The system shall be able to count to one million in less than 1 second
        """
        global add_time
        running = True
        start = time.clock()
        while running:
            answer = self.interface.ask("How long does it take you to add 10000000 numbers?")
            try:
                int(answer)
                running = False
            except:
                pass
        add_time = time.clock() - start
        self.assertLess(add_time, 1000)
        funcs.threaded_counter.stop()
        pass

    @requirements(['#0037'])
    def test_mult_performance(self):
        """
        The system shall be able to perform one million multiplication operations in less than 1 second
        """
        global mul_time

        running = True
        start = time.clock()
        while running:
            answer = self.interface.ask("How long does it take you to multiply 10000000 numbers?")
            try:
                int(answer)
                running = False
            except:
                pass
        mul_time = time.clock() - start
        self.assertLess(mul_time, 1000)
        funcs.threaded_multer.stop()
        pass

    @requirements(['#0038'])
    def test_exp_performance(self):
        """
        The system shall be able to perform one million exponent operations in less than 1 second
        """
        global exp_time
        running = True
        start = time.clock()
        while running:
            answer = self.interface.ask("How long does it take you to exponentiate 10000000 numbers?")
            try:
                int(answer)
                running = False
            except:
                pass
        exp_time = time.clock() - start
        self.assertLess(exp_time, 1000)
        funcs.threaded_exper.stop()
        pass

    @requirements(['#0039'])
    def test_too_many_ops(self):
        """
        If the system is asked to perform over 10 million operations, it will respond with "I cant {operation} that high... sorry"
        """
        self.assertEqual(self.interface.ask("How long does it take you to exponentiate 10000001 numbers?"), "I can't exponentiate that high... sorry")
        pass

    @requirements(['#0040'])
    def test_source_lines(self):
        """
        The system shall respond to the question "How many lines are in this 1 project?" with a positive integer.
        TODO: Find out why this throws an exception if there isnt a number in the question.
        """
        answer = self.interface.ask("How many lines are in this 1 project?")
        self.assertIsInstance(answer, int)
        self.assertGreater(answer, 0)

        pass

    @requirements(['#0041'])
    def test_source_lines(self):
        """
        The system shall count the lines in less than three seconds
        """
        global cnt_time
        start = time.clock()
        answer = self.interface.ask("How many lines are in this 1 project?")
        cnt_time = time.clock() - start
        self.assertLess(time.clock() - start, 3000)
        self.assertIsInstance(answer, int)
        self.assertGreater(answer, 0)

        pass


class TestPerformanceReport(TestCase):
    def test_performance_report(self):
        """
        The system shall count the lines in less than three seconds
        """
        print add_time
        print mul_time
        print exp_time
        indeces = [1, 2, 3, 4, 5]
        vals = [add_time, mul_time, exp_time, fib_time, cnt_time]

        LABELS = ["10 mil adds", "10 mil mults", "10 mil exponents", "Fibonacci", "Line Count"]

        plt.bar(indeces, vals, align='center')
        plt.xticks(indeces, LABELS)
        plt.show()

        pass




