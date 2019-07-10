# coding: utf-8


__all__ = ["TestCase"]


import os
import sys
import unittest

# adjust the path to import publab
base = os.path.normpath(os.path.join(os.path.abspath(__file__), "../.."))
sys.path.append(base)


class TestCase(unittest.TestCase):

    def test_nothing(self):
        self.assertTrue(True)
