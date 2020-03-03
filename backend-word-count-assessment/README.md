# WordCount

In this assignment you will use your knowledge of Python basic strings,
arithmetic, file reading, and dicts to create a command line utility to count
the words in a text file ([small.txt](./small.txt) and [alice.txt](./alice.txt)).

Complete the command-line python program named `wordcount.py` so that it will count the number of words in a text file, and also handle optional flags named `--count` and `--topcount`. The assignment instructions are also found within the `wordcount.py` file in this repo.

## Example
```console
$ python wordcount.py --count alice.txt
"'tis : 1
"--said : 1
"come : 2
"coming : 1
"edwin : 1
"french, : 1
"he's : 1
"how : 2
"i : 8
"i'll : 2
"it" : 2
"keep : 1
"let : 1
"much : 1
"poison" : 1
"purpose"?' : 1
```

```console
$ python wordcount.py --topcount alice.txt
Top 20 most frequent words in alice.txt
the : 1605
and : 766
to : 706
a : 614
she : 518
of : 493
said : 421
it : 362
in : 352
was : 333
you : 265
i : 261
as : 249
that : 222
alice : 221
her : 208
at : 206
had : 176
with : 169
all : 155
```

## Part A
For the `--count` flag, implement a `print_words(filename)` function that counts how often each word appears in the text and prints:

    word1 : count1
    word2 : count2
    ...
  
Print the above list in order, sorted alphabetically by word (Python will sort punctuation to come before letters which is fine). Store all the words as lowercase, so 'The' and 'the' count as the same word.

## Part B
For the `--topcount` flag, implement a `print_top()` function which is similar to `print_words()` but which prints just the top 20 most common words sorted so the **most common** word is first, then the next most common, and so on.


# Debugging
Use your VSCode IDE to set up a debug session, and single-step your `wordcount.py` -- Create two debug launch.json configurations: One with optional `--count` argument and one with `--topcount` argument.

## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
