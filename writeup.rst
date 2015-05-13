Lab 5 Writeup
=============

#. What was the hardest part of this lab?

The hardest part of this lab was figuring out how to use Python globals. I have been using Python for three years now and
have never needed to use global. Just today I discovered that I have been using global wrong this whole time where I thought
I was using it correctly. Changing this up drastically sped up how fast I was able to get this lab complete.

#. What is the difference between performance testing and performance measurement?

Performance testing involves testing to make sure a system reaches some minimum requirement for performance. It has more
to do with requirements. Performance measurement is closely tied to performance testing since one must measure performance
in order to test performance. Performance measurement doesn't have to be for testing purposes, however. For example, performance
measurements can be made for marketing reasons.

#. What new bugs did you encounter with the new code?

I couldn't get interface.__add_answer to work. Not entirely sure how to call a private method of a module, so I made my
own public add_answer function. This function was still much too slow to be able to test effectively, so I ended up commenting
that one out.

#. Did you mock anything to speed up performance testing? Do you see any issues with this?

No I did not. It obviously doesn't make sense to mock the interface you are speed testing, but I do see an instance in which it
would be wise to mock out side effects of some interface if you just want to isolate the testing of a specific operation within a
routine. I can't imagine mocking any of the performance tests for this lab though. Are there any portions that you would mock?

#. Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)


#. Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?

Load Testing - Let's test under the expected load to make sure this solution will scale.
Example of where load testing could be used: twitter needs to simulate its servers at a superbowl half-time show scale (a time when a high volume of tweets might occur)

Stress Testing - Let's test the upper limits of our system.
Example: Fill the entire database and see how it performs. Send the maximum number of requests per second. Max things out.

Endurance Testing - Let's test to make sure the system can run for a long time under expected load.
Example: In some systems, make sure it behaves the same on startup and while it has been running.

Spike Testing - Let's test to make sure the system can handle large fluctuations in traffic.
Example: Make sure the system behaves well when traffic goes from low to high, or high to low.

Configuration Testing - Let's make sure there is no configuration of the system that will cause it to fail.
Example: Try configuring a system in such a way that it will break

Isolation Testing - Let's repeat a test execution that caused a system problem to see if it is the cause or if it is a side effect of some other component.
Example: Thread B doesn't work. It is running alongside Thread A. Let's see if Thread A is causing Thread B to not work by only running Thread B.


#. How long did this lab take to accomplish?
This lab took seven hours to complete. Three of those hours were spent trying to figure out why global wasn't working. And I also spent a couple hours
trying to resolve this GIT error (on git commit: "fatal: index file smaller than expected"). In the end, I had to delete
the branch and copy and paste everything back in. Fun stuff!