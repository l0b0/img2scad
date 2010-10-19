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
import unittest

from img2scad import img2scad

EXAMPLE_BIG = join(dirname(__file__), './example_big.png')
EXAMPLE_SMALL = join(dirname(__file__), './example_1px.png')


class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""
    # pylint: disable-msg=R0904

    def test_small(self):
        """Check that a single pixel image gives output."""
        result = img2scad.img2scad(open(EXAMPLE_SMALL), 0)
        self.assertNotEqual(
            result,
            '')
        self.assertNotEqual(
            result,
            'module qrcode() {\n}\nqrcode();')


    def test_big(self):
        """Check that a big image gives output."""
        result = img2scad.img2scad(open(EXAMPLE_BIG), 1)
        self.assertNotEqual(
            result,
            '')
        self.assertNotEqual(
            result,
            'module qrcode() {\n}\nqrcode();')


    def test_zero(self):
        """Check that if the minimum is shifted sufficiently, the result is
        empty."""
        result = img2scad.img2scad(open(EXAMPLE_SMALL), -152)
        self.assertEqual(
            result,
            'module topography() {\n}\ntopography();')


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
