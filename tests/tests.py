#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
img2scad test suite

Default syntax:

./tests.py
    Run all unit tests
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

from doctest import testmod
from os.path import join, dirname
from re import search
import unittest

from img2scad import img2scad

EXAMPLE_BIG = join(dirname(__file__), './example_big.png')
EXAMPLE_BLACK = join(dirname(__file__), './example_black.png')
EXAMPLE_SMALL = join(dirname(__file__), './example_1px.png')


class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""

    def test_small(self):
        """A single pixel image gives one cube."""
        result = img2scad.img2scad(open(EXAMPLE_SMALL))
        self.assertTrue(search(r'translate.*cube', result))

    def test_black(self):
        """A black image gives no cubes."""
        result = img2scad.img2scad(open(EXAMPLE_BLACK))
        self.assertFalse(search(r'translate.*cube', result))

    def test_black_base(self):
        """A black image gives output if a base is applied."""
        result = img2scad.img2scad(
            open(EXAMPLE_BLACK),
            base=1)
        self.assertTrue(search(r'translate.*cube', result))

    def test_shift_to_zero(self):
        """A non-black pixel can be removed by the base offset."""
        result = img2scad.img2scad(
            open(EXAMPLE_SMALL),
            base=-152)
        self.assertFalse(search(r'translate.*cube', result))

    def test_log(self):
        """Non-black images should be loggable."""
        result = img2scad.img2scad(
            open(EXAMPLE_SMALL),
            log=True)
        self.assertTrue(search(r'translate.*cube', result))

    def test_log_one(self):
        """Log of 1 is zero."""
        result = img2scad.img2scad(
            open(EXAMPLE_BLACK),
            base=1,
            log=True)
        self.assertFalse(search(r'translate.*cube', result))

    def test_log_zero(self):
        """Log of 0 is undefined, so we skip those."""
        result = img2scad.img2scad(
            open(EXAMPLE_BLACK),
            log=True)
        self.assertFalse(search(r'translate.*cube', result))

    def test_big(self):
        """Check that a big image gives output."""
        result = img2scad.img2scad(
            open(EXAMPLE_BIG),
            base=5,
            log=True)
        self.assertTrue(search(r'translate.*cube', result))


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(testmod(img2scad)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
