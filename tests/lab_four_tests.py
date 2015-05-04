from unittest import TestCase
from ReqTracer import requirements
from main import Interface

QUESTION_MARK = chr(0x3F)


class TestWhereAmI(TestCase):

    @requirements(['#0022'])
    def test_git_branch_succes(self):
        """
        The system shall respond to the question "Where am I" with the local git branch name
        """
        pass

    @requirements(['#0022'])
    def test_git_branch_fail(self):
        """
        The system shall respond to the question "Where am I" with "unknown" if it can't be determined
        """
        pass


class TestWhereAreYou(TestCase):

    @requirements(['#0023'])
    def rest_git_repo_url_success(self):
        """
        The system shall respond to the question "Where are you" with the URL for the git repo
        """
        pass

    @requirements(['#0023'])
    def test_git_repo_url_fail(self):
        """
        The system shall respond to the question "Where are you" with "unknown" if it can't be determined
        """
        pass


class WhoElseIsHere(TestCase):
    @requirements(['#0024'])
    def test_who_else_userlist(self):
        """
        The system shall respond to the question "Who else is here" with a list of users
        """
        pass

    @requirements(['#0025'])
    def test_who_else_handshake(self):
        """
        When determining users the system shall connect to the server at ip address 192.168.64.3 port 1337 and sending a message "Who?"
        """
        pass

    @requirements(['#0026'])
    def test_who_else_parse(self):
        """
        If a response is received from the server the user list shall be parsed from a "$" seperated list of users
        """
        pass

    @requirements(['#0027'])
    def test_who_else_akbar(self):
        """
        If no response is received from the server the system shall return "IT'S A TRAAAPPPP"
        """
        pass


class TestFibonacci(TestCase):
    @requirements(['#0028'])
    def test_func(self):
        """
        The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct number from the fibonnacci sequence if the number has been found
        """
        pass

    @requirements(['#0029'])
    def test_func(self):
        """
        If the system has not determined the requested digit of the Fibonacci sequence it will respond with A)"Thinking...", B)"One second" or C)"cool your jets" based on a randomly generated number (A is 60% chance, B is 30% chance, C is 10% chance)
        """
        pass

