#0001 The system window shall have a title of "SharpTona"

**Window Title**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that the title of the window reads "SharpTona"


#0002 The system shall provide labels "Question:" and "Answer:"

**Q and A labels**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that there is a label that reads "Question:"
#. Verify that there is a label that reads "Answer:"

#0003 The system shall allow the user to enter a question and press the "Ask" button to receive an answer.

**Asking a Question**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input a question in the input box labeled "Question"
#. Click the "Ask" button
#. Verify that text appears in the "Answer" text field

#0004 The system shall have a default question/answer of "What is the answer to everything?": "42"
#0006 The system shall display answers in the Answer Text Box
#0008 If the "Ask" button is pushed and the question is known the answer box shall display the answer and enable user input.
**Answer to everything**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Input "What is the answer to everything?" into the "Question" text field.
#. Click the "Ask" button
#. Verify that the string "42" appears in the "Answer" text field
#. Repeat the first three steps to verify that user input is enabled

#0005 The system by default shall disable the answer box, "Teach" button and "Correct" button

**Disabled fields**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Verify that the "Answer" text field is greyed out and uneditable
#. Verify that the "Teach" and the "Correct" buttons are greyed out and unclickable


#0007 If no question is asked when the "Ask" button is pushed then "Was that a question?" shall be displayed in the answer box
**No question error**

*Setup*

#. Start the sharpTona.exe

*Procedure*

#. Click the "Ask" button
#. Verify that the "Answer" text field contains the string "Was that a question?"


#0009 If the "Correct" button is pushed the system shall update the answer to the given question and disable the answer box, teach button and correct button
**correct**

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

#0010 If the "Ask button is pushed and the question is not known then the answer box shall display "I don't know please teach me." and the "Teach" button will be enabled
**I am batman**

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

#0011 If the "Teach" button is pushed the system shall store the answer to the given question and disable the answer box, teach button and correct button

**<Test Name>**

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