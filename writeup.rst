What are five examples of other testing(nose2) plugins that might be useful?
    Plugin that asserts image equality with an CV engine.
    Plugin that outputs a BDD feature file.
    Plugin that filters the tests that are to be run in some user-defined way.
    Plugin that outputs test output to a file.
    Plugin that outputs test info via a dynamic html page.


Do you plan to create any of these plugins for your term project?
    I plan on making the CV plugin for my project.

What is the hardest part of this lab?
    The hardest part of this lab was understanding whether the test or the
    code was broken. In some places, it seemed ambiguous because the req would
    say to enter a query without a question mark at the end, but it still
    called it a "question"

Did the code fully and completely implement the requirements? Explain
    No. Some of the tests failed because the question mark character is set to ">" (chr(0x3E)
    and not chr(0x3F))

Was the requirements complete? Explain
    What is this question? Does this mean "Was there code implemented that was not covered by the req?"
    From this statement in the lab instructions "Remember from lecture, no matter how correct the
    code might look, the requirement is always the definitive answer." The answer could be thought of as
    "Of course the requirements are complete. They are the de facto definitions of what the code should be.
    That is why they are called 'requirements'"

    All red-highlighted code in the coverage report looks like it is still based on the req, so the req
    seems to be "complete" if our definition of "complete" is the same.

Why are requirements tracing so important?
    Tracing requirements is important because it lets the developer exhaustively test code based on the
    demands of the user rather than testing assuming the code is already correct.

How long did it take to complete this lab?
    Three hours


For each bug you found in the source code enter a "Bug Request" in your write up following
this template. You should consider bugs to be not following the requirements, inaccurate
requirements, or code that has no reason for existing (not covered by the requirements):

ISSUE Number: 0

BRIEF: "Was that a question?" response to valid query

Steps to reproduce:
    >>> import Interface
    >>> i = Interface()
    >>> i.ask("What is your name?")
    "Was that a question?"
    >>> i.teach("computer")
    "Please ask question first"

Comments: Expected output not to equal "Was that a question". Also, last_question is not being set
as shown by the "Pleas ask question first" output

Time Spent: 3 hours


Question: This bug is pretty much causing all of the failing tests to fail. Do I report one bug for
every failing req? or one bug for every single actual code issue that exists?
In this instance, I can't tell if other parts of the code are working because of the chr(0x3E) issue.
What were you expecting here?
