**#0001: Window Title**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that the title of the window reads "SharpTona"



**#0002: Q and A labels**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that there is a label that reads "Question:"
#. Verify that there is a label that reads "Answer:"


**#0003: Asking a Question**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input a question in the input box labeled "Question"
#. Click the "Ask" button
#. Verify that text appears in the "Answer" text field


**#0004: Answer to everything**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input "What is the answer to everything?" into the "Question" text field.
#. Click the "Ask" button
#. Verify that the string "42" appears in the "Answer" text field
#. Repeat the first three steps to verify that user input is enabled


**#0005: correct**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input the string "What is the answer to everything?" in the "Question" text field
#. Click the "Ask" button
#. Type "Bacon and Cheese" into the "Answer" text field
#. Click the "Correct" button
#. Input the string "What is the answer to everything?" in the "Question" text field
#. Click the "Ask" button
#. Verify that the "Answer" field has a string value of "Bacon and cheese"


**#0006: Disabled fields**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that the "Answer" text field is greyed out and uneditable
#. Verify that the "Teach" and the "Correct" buttons are greyed out and unclickable


**#0007: I am batman**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that "I don't know please teach me" is in the "Answer" field
#. Replace the text with "Batman" in the "Answer" field
#. Click the "Teach" button
#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that "Batman" is in the "Answer" field


**#0008: No question error**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Click the "Ask" button
#. Verify that the "Answer" text field contains the string "Was that a question?"


**#0009: batman**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that "I don't know please teach me" is in the "Answer" field
#. Replace the text with "Batman" in the "Answer" field
#. Click the "Teach" button
#. Verify that the "Answer" text field is greyed out and uneditable
#. Verify that the "Teach" and the "Correct" buttons are greyed out and unclickable


**#0010: clickable teach button**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that "I don't know please teach me" is in the "Answer" field
#. Verify that the "Teach" button is clickable


**#0011: teach answer**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that "I don't know please teach me" is in the "Answer" field
#. Replace the text with "Batman" in the "Answer" field
#. Click the "Teach" button
#. Verify that the "Answer" text field is greyed out and uneditable
#. Verify that the "Teach" and the "Correct" buttons are greyed out and unclickable
#. Input the string "Who am I?" in the "Question" text field
#. Click the "Ask" button
#. Verify that the "Answer" text field value is "Batman"


Analysis Questions
******************

#. What are the advantages and disadvantages of manual testing?
The advantage of manual testing is that you don't have to rely on two pieces of code being correct. You can verify
that the application still looks like it should without having to worry about your actual test cases having bugs in them
that would tell you that something is okay when it actually isn't.
The main disadvantage of manual testing is the fact that it is manual. If testing is to be repeated each commit, or even
each day, manual testing can become a time-sink. Manual testing is valuable to perform at least a few times before shipping,
however.

#. What are the advantages and disadvantages of automated testing?
The advantage of automated testing is that you can let your tests run while you go grab a cup of coffee, or browse reddit,
or become more productive. The fact that the tests can be automated make your life easier.
The main disadvantage to automated testing is that the tests can be difficult to write sometimes, especially when
dealing with graphics. For instance, how would one test some kind of firework particle generator to make sure it actually
looks like fireworks? It would take way to long to get a computer to judge and recognize what a firework should
look like, so this task is easier to do manually.

#. What new bugs did you encounter with the new code?
I did not encounter any bugs with the code unless I am to interpret the requirements entirely robotically literally.

#. How many UI tests did you generate? How did you deteremine you had written enough?
I generated ten tests. I determined I had written enough when all of the requirements were covered.

#. How long did this lab take to accomplish?
This lab took three hours to finish. For some reason the app does not completely initialize before assertions are being made
in the automated tests so I had to add a time.sleep for each time I restarted the app. Is there a fix for this?