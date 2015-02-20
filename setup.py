#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = '''Wrapper for Python Selenium client.
Includes a base PageObject class for extending.'''

setup(
    name='selwrap',
    version='0.1.0',

    description='Wrapper for Python Selenium client',
    long_description=long_description,

    author='jlas',
    author_email='juan.lasheras@gmail.com',

    url='http://www.juanl.org',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    license='MIT',
    platforms='any',

    install_requires=['selenium'],

    packages=find_packages(),
)