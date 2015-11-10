#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clepy
----------------------------------

Tests for `clepy` module.
"""

import unittest

import clepy


class TestClepy(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(clepy.hello_world())
        pass

    def tearDown(self):
        pass
