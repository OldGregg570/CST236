Bug Report
----------

**ISSUE Number: 0**

**BRIEF:**
    "IT'S A TRAAAPPPP" response to "Who else?" query

**Steps to reproduce:**
    >>> import Interface
    >>> i = Interface()
    >>> i.ask("Who else is here?")
    "IT'S A TRAAAPPPP"

**Comments:**
    Expected output to be a list of users

**Time Spent:**
    10 minutes


**ISSUE Number: 1**

**BRIEF:**
    "unknown" response where "Unknown" is expected in get_repo_url_success

**Steps to reproduce:**
    >>> import Interface
    >>> i = Interface()
    >>> i.ask("Where are you?")
    "unknown"

**Comments:**
    Expected output to be "Unknown"

**Time Spent:**
    10 minutes


**ISSUE Number: 2**

**BRIEF:**
    "unknown" response where "Unknown" is expected in get_repo_branch_success

**Steps to reproduce:**
    >>> import Interface
    >>> i = Interface()
    >>> i.ask("Where am I?")
    "unknown"

**Comments:**
    Expected output to be "Unknown"

**Time Spent:**
    10 minutes


**ISSUE Number: 3**

**BRIEF:**
    Expected fibonacci(0) to equal 1, not zero.

**Steps to reproduce:**
    >>> import Interface
    >>> i = Interface()
    >>> i.ask("What is the 0 digit of the Fibonacci sequence?")
    0

**Comments:**
    Expected 0 to be 1

**Time Spent:**
    10 minutes

Writeup Questions
-----------------

#. What observations did you make while performing the analysis on the system?
    While performing analysis I noticed that it runs a lot more quickly than I would have imagined. All numbers are reported as grades. I was really just expecting some float value.

#. What are the advantages/disadvantages of performing this analysis
    Advantages:     This analysis can be useful where a developer needs to be able to show how mature a piece of software is to someone who may or may not understand the development process.
                    Easily inform stakeholders on status of a project.

    Disadvantages:  The grades/scores are based on heuristics that aren't entirely standardized; many ways to measure the same metric exist.


#. What are the advantages of data mutation? Did you use any of these tools?
    Data mutation will tell the test writer if their test is actually testing anything. Any test that is absolutely unable to fail is considered worthless. Data mutation checks to make sure a test can actually fail.

#. What did you use Mock for in this lab?
    I used mock mainly to stub out Popen functionality. I also used it to mock the socket.socket method in order to return an entirely mocked socket interface.
    In this interface, I mocked connect, send, and recv.

#. How long did this lab take to complete?
    It took two hours to fix mistakes from the previous lab. This lab alone took about four or five hours to complete.