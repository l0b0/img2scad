#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""img2scad - Convert images to OpenSCAD structures
<http://github.com/l0b0/img2scad>

Default syntax:

img2scad [-b|--base=N] [-l|--log] < input_file

Description:

For each pixel in the input, it will create a cube in the output. The height of
the cube corresponds to the whiteness of the corresponding pixel.

If -b or --base is specified, all values will be shifted by that value. This
can be positive or negative. This can be used to output zero values.

If -l or --log is specified, the logarithm of the grey values will be used for the output.

Examples:

img2scad < example.png > example.scad
    Convert example.png to example.scad.

img2scad -b 1 < example.png > example.scad
    Convert example.png to example.scad, with a "bedrock" of height 1.

img2scad -b 2 -l < example.png > example.scad
    Convert example.png to example.scad, taking the logarithm for the height
    and preserving the black pixels.

<http://www.thingiverse.com/thing:4448>

Bugs:

Please submit bug reports at https://github.com/l0b0/img2scad/issues.
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010-2014 Victor Engmark'
__license__ = 'GPLv3'

from getopt import getopt, GetoptError
import math
from PIL import Image
from signal import signal, SIGPIPE, SIG_DFL
import sys

BLOCK_SIZE = 1
"""<http://www.denso-wave.com/qrcode/qrgene3-e.html> recommends at least four
dots per module, so with a 0.1mm accuracy you should use at least 0.4 +
BLOCK_OVERLAP.
"""

BLOCK_OVERLAP = 0.01
"""Cubes should overlap. Otherwise you will get the message "Object isn't a
valid 2-manifold!" on STL export (see
<http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/STL_Import_and_Export>)."""

BLOCK_SIDE = BLOCK_SIZE + BLOCK_OVERLAP
"""This is the actual side length of a block."""

signal(SIGPIPE, SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""


def img2scad(stream, base=0, log=False):
    """Convert pixels to OpenSCAD cubes."""

    img = Image.open(stream)

    # Convert to black and white 8-bit
    if img.mode != 'L':
        img = img.convert('L')

    width, height = img.size

    img_matrix = img.load()

    result = 'module topography() {\n'
    result += '    union() {\n'

    for row in range(height):
        for column in range(width):
            pixel = img_matrix[column, row] + base

            if log:
                # Skip unloggable values
                if pixel <= 0:
                    continue
                pixel = round(math.log(pixel, 2), 2)

            if 0 == pixel:
                continue

            # Center cubes in (x, y) plane
            result += '        translate([%(x)s, %(y)s, 0])' % {
                'x': BLOCK_SIZE * column - width / 2,
                'y': -BLOCK_SIZE * row + height / 2
            }
            result += 'cube('
            result += '[%(block_side)s, %(block_side)s, %(height)s]);\n' % {
                'block_side': BLOCK_SIDE,
                'height': pixel
            }

    result += '    }\n'
    result += '}\n'
    result += 'topography();'

    return result


def main(argv=None):
    """Argument handling."""

    if argv is None:
        argv = sys.argv

    # Defaults
    log = False
    base = 0

    try:
        opts, args = getopt(
            argv[1:],
            'b:l',
            ['base=', 'log'])
    except GetoptError, err:
        sys.stderr.write(str(err) + '\n')
        return 2

    for option, value in opts:
        if option in ('-b', '--base'):
            base = int(value)
        if option in ('-l', '--log'):
            log = True

    assert [] == args, 'There should be no arguments to this command'

    result = img2scad(sys.stdin, base, log)
    print result

if __name__ == '__main__':
    sys.exit(main())
