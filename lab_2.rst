=============
Lab 2 Writeup
=============

1. Explain the major differences between TDD and BDD
	In TDD, the specifications are written by someone who generally understands the system, while in BDD,  the spec is written as a .feature file
	In BDD, the .feature file explicitly defines test cases and structure. In TDD, the cases and structure are up to the developer.
	TDD gives the developer more control over what is being tested and in my opinion offers more flexibility for test cases.

2. What is a mixin, what challenges can occur when testing them? What order are they initialized in
	A mixin is an inheritable class type where multiple mixins can be inherited by one class. This lets us use multiple inheritance in python.
	Mixins can be challenging to test because a mixin changes the class of an object, so one must keep a close eye on all of their object types.

3. In python what does "super" do?
	In python, super makes a call to the base class. super can be used to call a base class' inherited method from a child class.


4. Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?
	Yes. I used my best judgement in this case.


5. Which model did you find most challenging? Why?
	The AlertSystem model was the most challenging because it took a while to realize that it would best be implemented as an event queue. These are the types of implementation details where it would be handy to know before implementing. This seems to be one of the challlenges of TDD/BDD.


6. Which model did you find easiest to update/maintain?
	The Orc model was the easiest to update because I think inheritance is simple in python


7. How did you test that logging occurred only when desired?
	I mocked the logging function. This makes it so I can check if the function was called and it lets me know what arguments it was called with.