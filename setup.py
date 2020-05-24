#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'PyYAML==5.3.1',
    'jsonschema==3.2.0'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ayush Pallav",
    author_email='ayushpallav@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An intelligent general purpose automation system.",
    entry_points={
        'console_scripts': [
            'anthill=anthill.src.cli.core:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description="",
    include_package_data=True,
    keywords='anthill',
    name='anthill',
    packages=find_packages(include=['anthill', 'anthill.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ayushpallav/anthill',
    version='1.0.3',
    zip_safe=False,
)
