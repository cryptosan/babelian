"""
Babelian
--------

Babelian is a dictionary on command-line.
You can search some words/phrases/examples without running WebBrowser.
This program will help Developers/Students/Teachers,
or who learns 2nd languages.

Links
`````
* Guide  : https://github.com/memnoth/babelian
* Github : https://github.com/memnoth/babelian
"""
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

ext_path = os.path.join(os.path.dirname(__file__), 'bin/wrds')
ver_line = [line for line in open(ext_path) if line.startswith('__version__')]
__ver__ = ver_line[0].split('=')[1].strip().replace('\'', '')

setup(
    name='Babelian',
    version=__ver__,
    url='https://github.com/memnoth/babelian',
    license='MIT',
    author='Yi Soo, (Jeff) An',
    author_email='yisooan@gmail.com',
    description='Babelian is a dictionary on command-line.',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    packages=['babelian'],
    scripts=['bin/wrds'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Education',
    ],
)
