from unittest import TestCase
from ReqTracer import requirements
from main import Interface
import getpass
#from  plugins.tracer import Tracer

QUESTION_MARK = chr(0x3E)

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
        self.assertIsInstance(self.interface.ask("Howdy"), str)
        self.assertIsInstance(self.interface.ask("What's up"), str)
        self.assertIsInstance(self.interface.ask("Where are you"), str)
        self.assertIsInstance(self.interface.ask("Why"), str)
        self.assertIsInstance(self.interface.ask("Whoah"), str)

    @requirements(['#0003', '#0004'])
    def test_invalid_question(self):
        """
        If the system does not detect a valid question keyword it shall return
        "Was that a question?"

        If the system does not detect a question mark at end of the string it
        shall return "Was that a question?"
        """
        self.assertNotEqual(self.interface.ask("What Why Who How{0}".format(QUESTION_MARK)), "Was that a question?")
        self.assertEqual(self.interface.ask("Where{0}".format(QUESTION_MARK)), "Was that a question?")
        self.assertEqual(self.interface.ask("is I be good at grammar"), "Was that a question?")
        pass


class DeterminingAnswers(TestCase):
    interface = Interface()

    @requirements(['#0005'])
    def test_question_breakdown(self):
        """
        The system shall break a question down into words separated by space
        """
        # Impossible req
        self.assertEqual(self.interface.ask("Whatdoesthisreqmean{0}".format(QUESTION_MARK)), "What does this req mean")
        pass

    @requirements(['#0006'])
    def test_match_tolerance(self):
        """
        The system shall determine an answer to a question as a correct if
        the keywords provide a 90% match and return the answer

        TODO: Note: Don't understand how to do this test with the provided documentation
        """
        self.interface.correct(self.interface.ask("Who invented Pyrthon{0}".format(QUESTION_MARK)))
        pass

    @requirements(['#0007'])
    def test_number_exclude(self):
        """
        The system shall exclude any number value from match code and provide
        the values to generator function (if one exists)
        """
        self.interface.ask("Who invented Python 2{0}".format(QUESTION_MARK))
        pass

    @requirements(['#0008'])
    def test_valid_match(self):
        """
        When a valid match is determined the system shall return the answer
        """
        self.assertEqual(self.interface.ask("How many seconds since{0}".format(QUESTION_MARK)), "42 seconds")
        pass


    @requirements(['#0009'])
    def test_unknown_valid_question(self):
        """
        When no valid match is determined the system shall return
        "I don't know, please provide the answer"
        """
        self.assertEqual(self.interface.ask("Who won the 2011 superbowl{0}".format(QUESTION_MARK)), "I don't know, please provide the answer")
        pass


class ProvidingAnswers(TestCase):
    interface = Interface()

    @requirements(['#0010'])
    def test_previously_asked(self):
        """
        The system shall provide a means of providing an answer to the
        previously asked question.
        """
        result_a = self.interface.ask("Who invented Python{0}".format(QUESTION_MARK))
        result_b = self.interface.ask(str(self.interface.last_question + QUESTION_MARK))

        self.assertEqual(result_a, result_b)
        pass

    @requirements(['#0011'])
    def test_teach_previous_question(self):
        """
        The system shall accept and store answers to previous questions in the
        form of a string or a function pointer and store it as the
        generator function.
        """
        self.assertEqual(self.interface.ask("Who won the twenty-eleven superbowl{0}".format(QUESTION_MARK)), "I don't know, please provide the answer")
        self.assertEqual(None, self.interface.teach("Packers"))
        self.assertEqual(self.interface.ask("Who won the twenty-eleven superbowl{0}".format(QUESTION_MARK)), "Packers")

        self.interface.ask("What is n times twenty{0}".format(QUESTION_MARK))
        self.interface.teach(lambda n: n * 20)
        self.assertEqual(self.interface.ask("What is 2 times twenty{0}".format(QUESTION_MARK)), 40)
        pass

    @requirements(['#0012'])
    def test_null_prev_question(self):
        """
        If no previous question has been asked the system shall respond with
        "Please ask a question first"
        """
        # Re-init the interface to clear interface.last_question
        self.interface = Interface()
        self.assertEqual(self.interface.teach("Test"), "Please ask a question first")
        pass

    @requirements(['#0013'])
    def test_update_no_teach(self):
        """
        If an attempt is made to provide an answer to an already answered
        question the system shall respond with "I don't know about that.
        I was taught differently" and not update the question
        """
        self.interface.ask("Who invented Python{0}".format(QUESTION_MARK))
        self.assertEqual(self.interface.teach("I did!"), "I don't know about that. I was taught differently")

        # make sure that didn't update the question
        self.assertEqual(self.interface.ask("Who invented Python{0}".format(QUESTION_MARK)), "Guido Rossum(Benevolent Dictator For Life)")
        pass


class CorrectingAnswers(TestCase):
    interface = Interface()

    @requirements(['#0014', '#0015'])
    def test_store_answer(self):
        """
        The system shall provide a means of updating an answer to the previously
        asked question.

        The system shall accept and store answers to previous questions in the form
        of a string or a function pointer and store it as the generator function.
        """
        self.interface.ask("What is my birthday{0}".format(QUESTION_MARK))
        self.interface.teach("December 6th, 1991")
        self.assertEqual(self.interface.ask("What is my birthday{0}".format(QUESTION_MARK)), "December 6th, 1991")

        self.interface.ask("What is n times twenty{0}".format(QUESTION_MARK))
        self.interface.teach(lambda n: n * 20)
        self.assertEqual(self.interface.ask("What is 2 times twenty{0}".format(QUESTION_MARK)), 40)
        pass

    @requirements(['#0016'])
    def test_init_teach(self):
        """
        If no previous question has been asked the system shall respond with
        "Please ask a question first"
        """
        self.interface = Interface()
        self.assertEqual(self.interface.teach("ASDF"), "Please ask a question first")
        pass


class InitialAnswersProvided(TestCase):
    interface = Interface()

    @requirements(['#0017'])
    def test_feet_to_miles(self):
        """
        The system shall respond to the question "What is <float> feet in miles"
        with the the float value divided by 5280 and append "miles" to the end
        of the return.
        """
        expected_answer_val = 20000.0 / 5280.0
        actual_val = float(self.interface.ask("What is 20000.0 feet in miles{0}".format(QUESTION_MARK))[:len(" miles")])
        self.assertAlmostEqual(expected_answer_val, actual_val, 2)
        pass

    @requirements(['#0018'])
    def test_datetime(self):
        """
        The system shall respond to the question "How many seconds since <date time>"
        with the number of seconds from that point of day till now.
        """
        pass

    @requirements(['#0019'])
    def test_valid_match_guido(self):
        """
        The system shall respond to the question "Who invented Python" with
        "Guido Rossum(BFDL)"
        """
        self.assertEqual(self.interface.ask("Who invented Python{0}".format(QUESTION_MARK)), "Guido Rossum(BFDL)")
        pass

    @requirements(['#0020'])
    def test_why_no_understand_me_you_guys(self):
        """
        The system shall respond to the question "Why don't you understand me"
        with "Because you do not speak 1s and 0s"
        """
        self.assertEqual(self.interface.ask("Why don't you understand me{0}".format(QUESTION_MARK)), "Because you do not speak 1s and 0s")
        pass

    @requirements(['#0021'])
    def test_hal_close_the_bay_doors(self):
        """
        The system shall respond to the question "Why don't you shutdown" with
        "I'm afraid I can't do that <username>"
        """
        expected = "I'm afraid I can't do that {0}".format(getpass.getuser())
        self.assertEqual(self.interface.ask("Why don't you shutdown{0}".format(QUESTION_MARK)), expected)
        pass