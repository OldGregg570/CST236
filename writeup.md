#. What bugs did you find?

I found the following bugs:

Bug 1:

"Ask" on a string with characters after the ?

Bug 2:

"Ask": Any string that is a length multiple of five

Bug 3:

"Ask": Any string of length 52

Bug 4:

"Teach" on a string with characters after the ?

Usually takes 10 seconds before it happens. Otherwise it is a "Bug 7"

Other Workflow (cant recreate this)
    ...
    Ask: T7t12YiXnnm
    Correct: nXb EWGHuJ?bLbgHbMTh2eZBBF3
    Ask: LaaPAdNO yUuxSpLJDnhIWXEe?z
    Teach: 0Mm5mUZpiWnJfFoO6pOhgOOgBUgFMb6Ma4W2K5sR85MBCljnvbgk

Bug 5: (On a fresh start)
"Ask": "What is the answer to everything?"
"Correct": Antything that isn't a number

Bug 6:
Unable to reproduce

Bug 7:
"Teach" on a string with characters after the ?

#. What are the advantages and disadvantages of fuzz testing?

The advantages of fuzz testing are that you might hit some obscure corner case involving odd user workflow that you might not have
hit otherwise. The disadvantage is that is is probabilistic, and can be complicated to filter the logs.

#. What was the hardest part of this lab?

Filtering through the logs to the console was the hardest. This type of testing would probably be more efficient if
there were some complicated logging logic.

#. How would you apply the concept of fuzz testing to testing a phone? a webpage? a library?

On a phone, I would test different switches between applications to test the application lifecycle and stack.
I belive there already exists some lib called monkey for either android that does what Gremlins.js does.

On a webpage, I would test all REST methods continuously and in different random orders.

For a library, I would test similarly to how I tested for this lab.

#. How could throttling fuzz test scripts help with finding bugs?

If there were some graphics application, throttling fuzz testing could be used to find artifacts and bugs that would otherwise not be
able to be found at 60fps. Throttling in this application could be used to get a better view of the log, though I personally think
simple log filtering would be the better approach here.

#. What is Delta Debugging and how would it help with fuzz testing?

Delta debugging involves continuously removing properties from a state that makes a system fail in such a way
a minimal set of failure-inducing circumstances is acquired. This can be used with fuzz testing to narrow down what
is actually making a program crash vs what is irrelevant to a bug.

#. If steps 1-20 were to produce an error using delta debugging what are the steps that would arrive at steps 8, 12, 13, 19 and 20 being necessary to reproduce the error?

Isolate 1 - 20:

    Check second half: 11 - 20 pass
    
        Add  half of the first skipped portion: (11 - 1) / 2 = 5
        
    5 - 20 fail

Isolate 5 - 20:

    8 - 20 fail
    
Isolate 8 - 20:

    10 - 20 pass
    
    9 - 20 pass


We now know by binary search what section the error is in. Now we just test the remaining sections
in binary order.