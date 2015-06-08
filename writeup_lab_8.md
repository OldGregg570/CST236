#. How was this test useful?
This test could be useful to make sure everything in your modules is at least importable and reachable regardless of 
whether it is working as intended. This instance would be most useful when starting out a project. It would help you get
to know the modules you will be using, testinng against, and mocking. Sanity testing is best used to make sure you can
continue with normal testing.

#. How did you report errors found by this test? How difficult would it be for a developer to debug these errors
In my main.py (not using nose) there is a call to exit() that prints "Call to <function name> failed>"
It was harder to import modules since I was importing them with map. I couldn't find out how to otherwise dynamically
import modules.

#. What other things would be useful to have in a sanity test?
Open index.html and make sure there is no 404 error.
Send all REST requests and make sure there are no 404 errors.
Test all other urls for 404.
Servers in general.

#. How would you sanity test a UI? A database interface? a webpage? a C# program?
I would sanity test a UI by making sure the UI framework is importable and a base window can be drawn.
I would sanity test a database interface by making sure I can initialize a new database from my tests, and insert a test
table.
I would sanity test a webpage by checking all urls and requests for 404. I would check to make sure I can mock http requests.
I would also make sure I can mock WebSockets if I am using them.
