## Cleanup on aisle 5: PEP8ify
For this assessment, you'll be cleaning up a program that functions properly,
but doesn't conform to the [PEP8](https://www.python.org/dev/peps/pep-0008/)
style guide. 

Your task is to update the program so that it is PEP 8 compliant. 

## Guidelines

- You should *not* remove comments. If a comment is too long, simply break it up into multiple lines.

- While there are several other PEP8 violations, we are only concerned with those reported by [flake8](http://flake8.pycqa.org/en/latest/)

- Do *not* modify anything in the `tests` directory

- The test suite (see below) must pass all tests.

## Running the test suite
There are several ways to run the test suite:

- Use automatic[ _test discovery_ within VSCode](https://code.visualstudio.com/docs/python/unit-testing).  You must enable this feature in your IDE.

- You can use [rerun](https://pypi.org/project/rerun/) run continually run unit tests:

```console
$ rerun "python -m unittest discover"
```

If you don't have rerun installed, you can run the test suite by itself:
```console
$ python -m unittest discover
```

## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
