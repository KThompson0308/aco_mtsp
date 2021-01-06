#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Kevin Thompson, Lance Dacy, Shawn Jung, Reannan McDaniel",
    author_email='kthompson395@hotmail.com',
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
    description="Ant colony optimization for the multiple travelling salesman problem",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aco_mtsp',
    name='aco_mtsp',
    packages=find_packages(include=['aco_mtsp', 'aco_mtsp.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kthompson0308/aco_mtsp',
    version='0.1.0',
    zip_safe=False,
    ext_modules = cythonize(['aco_mtsp/Network.pyx',
                              'aco_mtsp/Solver.pyx',
                              'tests/Network_test.pyx', 
                              'tests/Solver_test.pyx'],
                            language_level=3,
                            compiler_directives={'binding':True})
)
