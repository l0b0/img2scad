#!/usr/bin/env python
from setuptools import find_packages, setup
from img2scad.img2scad import __doc__ as module_doc

setup(
    name='img2scad',
    version='0.3',
    description='Image to OpenSCAD converter',
    long_description=module_doc,
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
    author='Victor Engmark',
    author_email='victor.engmark@gmail.com',
    maintainer='Victor Engmark',
    maintainer_email='victor.engmark@gmail.com',
    download_url='http://github.com/l0b0/img2scad',
    platforms=['POSIX', 'Windows'],
    license='GPL v3 or newer')
