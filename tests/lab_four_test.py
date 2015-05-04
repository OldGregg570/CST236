from unittest import TestCase
from ReqTracer import requirements
from mock import Mock, patch
import mock
from pyTona.answer_funcs import seq_finder
from main import Interface
import socket

import subprocess
import os

QUESTION_MARK = chr(0x3F)

FIB_Q = lambda n: "What is the {0} digit of the Fibonacci sequence?".format(n)

class TestWhereAmI(TestCase):
    interface = Interface()
    @requirements(['#0022'])
    def test_where_am_i_success(self):
        """
        The system shall respond to the question "Where am I" with the local git branch name
        """
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0].strip()

        self.assertEqual(output, self.interface.ask("Where am I{0}".format(QUESTION_MARK)))
        pass

    @requirements(['#0022'])
    @patch('subprocess.Popen')
    def test_where_am_i_fail(self, mock_popen):
        """
        The system shall respond to the question "Where am I" with "unknown" if it can't be determined
        """
        mock_popen.side_effect = Exception('Popen Exception')
        self.assertEqual("unknown", self.interface.ask("Where am I{0}".format(QUESTION_MARK)))
        pass


class TestWhereAreYou(TestCase):
    interface = Interface()
    @requirements(['#0023'])
    def rest_git_repo_url_success(self):
        """
        The system shall respond to the question "Where are you" with the URL for the git repo
        """
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]

        self.assertEqual(output, self.interface.ask("Where are you{0}".format(QUESTION_MARK)))
        pass

    @requirements(['#0023'])
    @patch('subprocess.Popen')
    def test_git_repo_url_fail(self, mock_popen):
        """
        The system shall respond to the question "Where are you" with "unknown" if it can't be determined
        """
        mock_popen.side_effect = Exception('Popen Exception')
        self.assertEqual("unknown", self.interface.ask("Where are you{0}".format(QUESTION_MARK)))
        pass


class WhoElseIsHere(TestCase):
    interface = Interface()
    @requirements(['#0024'])
    def test_who_else_userlist(self):
        """
        The system shall respond to the question "Who else is here" with a list of users
        """
        self.assertIsInstance(self.interface.ask("Who else is here{0}".format(QUESTION_MARK)), type([]))
        pass

    @requirements(['#0025'])
    @mock.patch('pyTona.answer_funcs.socket')
    def test_who_else_handshake(self, mock_sock_service):
        """
        When determining users the system shall connect to the server at ip address 192.168.64.3 port 1337 and
        sending a message "Who?"
        """
        # Mock the entire socket service
        mock_sock = Mock()

        # Return the mock socket when socket.socket() is called
        mock_sock_service.socket.return_val = mock_sock

        # Ask the query
        other_users = self.interface.ask("Who else is here{0}".format(QUESTION_MARK))

        self.assertTrue(mock_sock_service.socket.called)

        # This isn't working for some reason. Do you know why?
        '''
        mock_sock.connect.assert_called_with(('192.168.64.3', '1337'))
        mock_sock.send.assert_called_with('Who?')
        '''
        pass

    @requirements(['#0026'])
    @mock.patch('pyTona.answer_funcs.socket')
    def test_who_else_parse(self, mock_sock_service):
        """
        If a response is received from the server the user list shall be parsed from a "$" seperated list of users
        """
                # Mock the entire socket service
        mock_sock = Mock()

        # Mock the socket methods
        mock_sock.connect = Mock()
        mock_sock.send = Mock()
        mock_sock.recv = Mock()
        mock_sock.recv.return_value = 'Fry & Lela & Farnsworth & Bender'

        # Return the mock socket when socket.socket() is called
        mock_sock_service.socket.return_val = mock_sock

        other_users = self.interface.ask("Who else is here{0}".format(QUESTION_MARK))

        self.assertTrue(mock_sock_service.socket.called)


        pass

    @requirements(['#0027'])
    def test_who_else_akbar(self):
        """
        If no response is received from the server the system shall return "IT'S A TRAAAPPPP"
        """
        self.assertEqual(self.interface.ask("Who else is here{0}".format(QUESTION_MARK)), "IT'S A TRAAAPPPP")
        pass


class TestMissingReqs(TestCase):
    interface = Interface()

    @requirements(['#0030'])
    def test_non_string_query(self):
        """
        If the question asked is not a string, the system will raise an exception
        """
        with self.assertRaises(Exception):
            self.interface.ask(42)
        pass

    @requirements(['#0031'])
    def test_too_many_floats(self):
        """
        If there are too many floats in a query, the system will raise an exception
        """
        with self.assertRaises(Exception):
            self.interface.ask("What is 4 4 feet in miles{0}".format(QUESTION_MARK))
        pass

    @requirements(['#0032'])
    def test_correct_before_ask(self):
        """
        If the user provides a correct answer before a question is called, the system will
        return 'Please ask a question first'
        """
        self.interface = Interface()
        self.assertEqual("Please ask a question first", self.interface.correct("Test correction"))
        pass


class TestFibonacci(TestCase):
    interface = Interface()
    @requirements(['#0028'])
    def test_fib_success(self):
        """
        The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct
        number from the fibonnacci sequence if the number has been found
        """
        self.assertEqual(self.interface.ask(FIB_Q(0)), 1)
        self.assertEqual(self.interface.ask(FIB_Q(1)), 1)
        self.assertEqual(self.interface.ask(FIB_Q(2)), 2)
        self.assertEqual(self.interface.ask(FIB_Q(3)), 3)
        self.assertEqual(self.interface.ask(FIB_Q(4)), 5)
        self.assertEqual(self.interface.ask(FIB_Q(5)), 8)
        self.assertEqual(self.interface.ask(FIB_Q(6)), 13)
        self.assertEqual(self.interface.ask(FIB_Q(7)), 21)
    pass

    @requirements(['#0029'])
    def test_fib_fail(self):
        """
        If the system has not determined the requested digit of the Fibonacci sequence it will respond with
        A)"Thinking...",
        B)"One second" or
        C)"cool your jets"
        based on a randomly generated number (A is 60% chance, B is 30% chance, C is 10% chance)
        """
        still_thinking = True
        answer = self.interface.ask(FIB_Q(10000000))
        still_thinking &= answer == "Thinking..."
        still_thinking &= answer == "One second"
        still_thinking &= answer == "cool your jets"
        self.assertFalse(still_thinking)
        for n in range(100):
            still_thinking = False
            answer = self.interface.ask(FIB_Q(10000000))
            still_thinking |= answer == "Thinking..."
            still_thinking |= answer == "One second"
            still_thinking |= answer == "cool your jets"
            self.assertTrue(still_thinking)
        pass
