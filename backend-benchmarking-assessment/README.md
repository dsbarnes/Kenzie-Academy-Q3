# Assessment: I don't have time for this

Imagine that you've been working on this program on a team of developers. You've
done all the right things up until now, including writing [doctests](https://docs.python.org/2.7/library/doctest.html) and [unittests](tests/test_anagrams.py).

Unfortunately, a previous teammate not only committed code that made the benchmarking tests fail, but they force-pushed to master after rewriting history, so you can't simply go back in the git history to fix things. Especially since, in the process of ruining the timings, the developer _did_ manage to implement features that weren't there before.

Your task is to modify [anagrams.py](anagrams.py) such that the tests pass again. If the problem isn't obvious to you by visually examining the `anagrams.py` module, consider using the profiling techniques that you learned about in the lesson to pin down the problem. Using a debugger may also help you to get a handle on exactly _why_ things are slow.

## Skipped unit test
If you look at the test case, you'll notice that the `test_long` unit test is currently being skipped. That's because if it were to run with the current implementation of `find_anagrams` it would take several minutes to complete. We suggest that you try and get the `test_short` to pass first, then remove the `@skip` line and ensure that the tests still pass.

You can run the doctests with the following command:
```console
$ python -m doctest -v anagrams.py words/short.txt
```
You can also run the tests with the unittest framework. From the top level of the assignment, use the following command:
```console
$ python -m unittest discover
```

Good Luck!
