#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def setUp(self):
        self.parser = echo.create_parser()

    def test_upper_short(self):
        test_args = ['-u', 'dsbarnes']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.upper)

        result = echo.main(test_args)
        self.assertEquals(result, 'DSBARNES')

    def test_upper_long(self):
        test_args = ['--upper', 'dsbarnes']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.upper)

        result = echo.main(test_args)
        self.assertEquals(result, 'DSBARNES')

    def test_lower_short(self):
        test_args = ['-l', 'DSBARNES']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.lower)

        result = echo.main(test_args)
        self.assertEquals(result, 'dsbarnes')

    def test_lower_long(self):
        test_args = ['--lower', 'DSBARNES']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.lower)

        result = echo.main(test_args)
        self.assertEquals(result, 'dsbarnes')

    def test_title_short(self):
        test_args = ['-t', 'ds barnes']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.title)

        result = echo.main(test_args)
        self.assertEquals(result, 'Ds Barnes')

    def test_title_long(self):
        test_args = ['--title', 'ds barnes']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.title)

        result = echo.main(test_args)
        self.assertEquals(result, 'Ds Barnes')

    def test_all_args_short(self):
        test_args = ['-tul', 'ds barnes']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.title)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)

        result = echo.main(test_args)
        self.assertEquals(result, 'Ds Barnes')

    def test_upper_vs_lower_short(self):
        test_args = ['-ul', 'DSBARNES']
        ns = self.parser.parse_args(test_args)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.upper)

        result = echo.main(test_args)
        self.assertEquals(result, 'dsbarnes')

    def test_no_args(self):
        test_args = ['DsBarneS']
        ns = self.parser.parse_args(test_args)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.title)

        result = echo.main(test_args)
        self.assertEquals(result, 'DsBarneS')


if __name__ == '__main__':
    unittest.main()
