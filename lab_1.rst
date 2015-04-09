=============
Lab 1 Writeup
=============

1. What was the hardest part of this lab?
-----------------------------------------

    The hardest part of this lab was learning git. I accidentally messed things up a few times somehow.

2. During the course of this lab, why did we exclude .pyc files?
----------------------------------------------------------------

    We exclude the .pyc files because they are compiled python. They are byte code that is
    executed by the Python virtual machine. A Python install is required to run code
    from the repository, so including the .pyc files is not necessary, as they can already
    be compiled by whoever clones the repo.

3. Name three files which would likely need to have a gitignore added?
----------------------------------------------------------------------

    .exe, .o, and .msi files should probably be ignored with gitignore.

4. What is a pyunit TestCase?
-----------------------------

    A pyunit TestCase is "a [Python] class whose instances are single test cases" (from the docs)

5. What is the difference between a git cherry pick and a rebase?
-----------------------------------------------------------------

    Rebase takes an entire branch's work of commits and applies the changes to main.
    Cherry-pick selects a single commit from a branch to apply to main.

6. How could you use git to print out just the author name of a given file for the current version of the repo?
--------------------------------------------------------------------------------

    This is what I came up with:

    >>> git show --summary --pretty=format:"Author: %aN"

7. During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class
--------------------------------------------------------------------------------

    No I did not, but I have used Tortoise SVN.

8. Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type?
--------------------------------------------------------------------------------

    Yes I did find the second issue. I ended up fixing the code in get_triangle_type.