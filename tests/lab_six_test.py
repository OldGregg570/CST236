from pywinauto import application
from unittest import TestCase
from ReqTracer import requirements
import time

def before_each():
    app = application.Application()
    app.start('./sharpTona.exe')
    time.sleep(0.0625)
    return app


def after_each(app):
    app.sharpTona.Close()


class LabSixTests(TestCase):
    @requirements(['#0001'])
    def test_window_title(self):
        """
        #0001 The system window shall have a title of "SharpTona"
        """
        app = before_each()
        self.assertIsNotNone(app.SharpTona)
        after_each(app)
        pass

    @requirements(['#0002'])
    def test_labels(self):
        """
        The system shall provide labels "Question:" and "Answer:"
        """
        app = before_each()
        self.assertIsNotNone(app.SharpTona['Question'])
        self.assertIsNotNone(app.SharpTona['Answer'])
        after_each(app)
        pass

    @requirements(['#0003'])
    def test_ask(self):
        """
        The system shall allow the user to enter a question and press the "Ask" button to receive an answer.
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("Is this a question?")
        app.sharpTona['Ask'].Click()

        self.assertIsInstance(app.sharpTona['Answer:Edit'].Texts()[0], unicode)
        after_each(app)
        pass

    @requirements(['#0004'])
    def ask_answer_to_everything(self):
        """
        The system shall have a default question/answer of "What is the answer to
        everything?": "42"
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], '42')
        after_each(app)
        pass

    @requirements(['#0005'])
    def test_disabled_fields(self):
        """
        The system by default shall disable the answer box, "Teach" button and "Correct" button
        """
        app = before_each()
        self.assertFalse(app.sharpTona['Correct'].GetProperties()['IsEnabled'])
        self.assertFalse(app.sharpTona['Answer:Edit'].GetProperties()['IsEnabled'])
        self.assertFalse(app.sharpTona['Teach'].GetProperties()['IsEnabled'])
        after_each(app)
        pass

    @requirements(['#0006'])
    def test_answer_display(self):
        """
        The system shall display answers in the Answer Text Box
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], '42')
        after_each(app)
        pass

    @requirements(['#0007'])
    def test_no_question_ask(self):
        """
        If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in
        the answer box
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], 'Was that a question?')
        after_each(app)
        pass

    @requirements(['#0008'])
    def test_ask_answer(self):
        """
        If the "Ask" button is pushed and the question is known the answer box shall display the answer and
        enable user input.
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], '42')
        app.sharpTona['Question:Edit'].SetText("")
        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], '42')
        after_each(app)
        pass

    @requirements(['#0009'])
    def test_correct(self):
        """
        If the "Correct" button is pushed the system shall update the answer to the given question and disable the
        answer box, teach button and correct button
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()
        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], '42')

        app.sharpTona['Answer:Edit'].SetText("bacon and cheese")
        app.sharpTona['Correct'].Click()

        self.assertFalse(app.sharpTona['Correct'].GetProperties()['IsEnabled'])
        self.assertFalse(app.sharpTona['Answer:Edit'].GetProperties()['IsEnabled'])
        self.assertFalse(app.sharpTona['Teach'].GetProperties()['IsEnabled'])

        app.sharpTona['Question:Edit'].SetText("What is the answer to everything?")
        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], "bacon and cheese")


        after_each(app)
        pass

    @requirements(['#0010'])
    def test_teach(self):
        """
        If the "Ask button is pushed and the question is not known then the answer box shall display
        "I don't know please teach me." and the "Teach" button will be enabled
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("Who am I?")

        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], "I don't know please teach me.")

        app.sharpTona['Teach'].Click()
        after_each(app)
        pass

    @requirements(['#0011'])
    def test_teach_disable(self):
        """
        If the "Teach button is pushed the system shall store the answer to the given question and disable the answer
        box, teach button and correct button
        """
        app = before_each()
        app.sharpTona['Question:Edit'].SetText("Who am I?")

        app.sharpTona['Ask'].Click()

        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], "I don't know please teach me.")
        app.sharpTona['Answer:Edit'].SetText("Batman")

        app.sharpTona['Teach'].Click()


        app.sharpTona['Question:Edit'].SetText("Who am I?")

        app.sharpTona['Ask'].Click()
        self.assertEqual(app.sharpTona['Answer:Edit'].Texts()[0], "Batman")

        after_each(app)
        pass


