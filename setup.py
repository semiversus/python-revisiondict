#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open('README.rst', 'rb') as readme_file:
    readme = readme_file.read().decode('utf-8')


setup(
    author='Günther Jena',
    author_email='guenther@jena.at',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description="RevisionDict works like an ordinary dictionary with " +
                "additional revision keeping of changes.",
    license='MIT license',
    long_description=readme,
    include_package_data=True,
    keywords='dict revision versioning',
    name='revisiondict',
    packages=find_packages(include=['revisiondict*']),
    url='https://github.com/semiversus/python-revisiondict',
    zip_safe=False,
)
