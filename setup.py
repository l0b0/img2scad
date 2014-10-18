#!/usr/bin/env python
from setuptools import find_packages, setup
from img2scad.img2scad import __doc__, __version__, __author__, __email__

setup(
    name='img2scad',
    version=__version__,
    description='Image to OpenSCAD converter',
    long_description=__doc__,
    url='http://github.com/l0b0/img2scad',
    keywords='image images height heightmap heightmaps elevation convert converter OpenSCAD SCAD',
    packages=find_packages(exclude=['tests']),
    install_requires=['Pillow==2.6.1'],
    entry_points={
        'console_scripts': ['img2scad=img2scad.img2scad:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
    ],
    test_suite='tests.tests',
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    download_url='http://github.com/l0b0/img2scad',
    platforms=['POSIX', 'Windows'],
    license='GPL v3 or newer')
