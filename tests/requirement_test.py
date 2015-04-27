from unittest import TestCase
from ReqTracer import requirements
from main import Interface
from  plugins.tracer import Tracer


class AcceptableAnswers(TestCase):
    interface = Interface()
    @requirements(['#0001'])
    def test_generic_string(self):
        """
        The system shall accept questions in the form of strings and attempt to answer them
        """
        self.assertIsInstance(self.interface.ask("a string"), str)

    @requirements(['#0002'])
    def test_start_with_keywords(self):
        """
        The system shall answer questions that begin with one of the following valid
        question keywords: "How", "What", "Where", "Why" and "Who"
        """
        self.assertIsInstance(self.interface.ask("How"), str)
        self.assertIsInstance(self.interface.ask("What"), str)
        self.assertIsInstance(self.interface.ask("Where"), str)
        self.assertIsInstance(self.interface.ask("Why"), str)
        self.assertIsInstance(self.interface.ask("Who"), str)

    @requirements(['#0003'])
    def test_ (self):
        """
        If the system does not detect a valid question keyword it shall return
        "Was that a question?"
        """
        pass

    @requirements(['#0004'])
    def test_ (self):
        """
        If the system does not detect a question mark at end of the string it
        shall return "Was that a question?"
        """
        pass

    @requirements(['#0005'])
    def test_ (self):
        """
        The system shall break a question down into words separated by space
        """
        pass

    @requirements(['#0006'])
    def test_ (self):
        """
        The system shall determine an answer to a question as a correct if
        the keywords provide a 90% match and return the answer
        """
        pass

    @requirements(['#0007'])
    def test_ (self):
        """
        The system shall exclude any number value from match code and provide
        the values to generator function (if one exists)
        """
        pass

    @requirements(['#0008'])
    def test_ (self):
        """
        When a valid match is determined the system shall return the answer
        """
        pass

    @requirements(['#0009'])
    def test_ (self):
        """
        When no valid match is determined the system shall return
        "I don't know, please provide the answer"
        """
        pass

    @requirements(['#0010'])
    def test_ (self):
        """
        The system shall provide a means of providing an answer to the
        previously asked question.
        """
        pass

    @requirements(['#0011'])
    def test_ (self):
        """
        The system shall accept and store answers to previous questions in the
        form of a string or a function pointer and store it as the
        generator function.
        """
        pass

    @requirements(['#0012'])
    def test_ (self):
        """
        If no previous question has been asked the system shall respond with
        "Please ask a question first"
        """
        pass

    @requirements(['#0013'])
    def test_ (self):
        """
        If an attempt is made to provide an answer to an already answered
        question the system shall respond with "I don't know about that.
        I was taught differently" and not update the question
        """
        pass

    @requirements(['#0014'])
    def test_ (self):
        """
        The system shall provide a means of updating an answer to the previously
        asked question.
        """
        pass

    @requirements(['#0015'])
    def test_ (self):
        """
        The system shall accept and store answers to previous questions in the form
        of a string or a function pointer and store it as the generator function.
        """
        pass

    @requirements(['#0016'])
    def test_ (self):
        """
        If no previous question has been asked the system shall respond with
        "Please ask a question first"
        """
        pass

    @requirements(['#0017'])
    def test_ (self):
        """
        The system shall respond to the question "What is <float> feet in miles"
        with the the float value divided by 5280 and append "miles" to the end
        of the return.
        """
        pass

    @requirements(['#0018'])
    def test_ (self):
        """
        The system shall respond to the question "How many seconds since <date time>"
        with the number of seconds from that point of day till now.
        """
        pass

    @requirements(['#0019'])
    def test_ (self):
        """
        The system shall respond to the question "Who invented Python" with
        "Guido Rossum(BFDL)"
        """
        pass

    @requirements(['#0020'])
    def test_ (self):
        """
        The system shall respond to the question "Why don't you understand me"
        with "Because you do not speak 1s and 0s"
        """
        pass

    @requirements(['#0021'])
    def test_ (self):
        """
        The system shall respond to the question "Why don't you shutdown" with
        "I'm afraid I can't do that <username>"
        """
        pass