#!/usr/bin/env python


"""Setup script for Robot's MongoDB Library distributions"""

import setuptools

import sys, os

sys.path.insert(0, os.path.join('src', 'MongoDBLibrary'))

from version import VERSION

requirements = [
    'tox>=3.0.0',
    'coverage',
    'robotframework>=3.0',
    'pymongo>=3.8.0',
    'bson>=0.5.8'
]

test_requirements = [
    # TODO: put package test requirements here
]

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]


def main():
    setuptools.setup(name='robotframework-mongodb-library',
                     version=VERSION,
                     description='Mongo Database utility library for Robot Framework',
                     author='Akkharaphon Tangpaopong',
                     author_email='akkharaphon.tpp@gmail.com',
                     url='https://github.com/robotframework-thailand/robotframework-mongodb-library',
                     keywords=['mongodb', 'robotframework', 'robotframework-mongodb-library', 'MongoDBLibrary'],
                     package_dir={'': 'src'},
                     packages=['MongoDBLibrary'],
                     include_package_data=True,
                     install_requires=requirements,
                     zip_safe=False,
                     classifiers=CLASSIFIERS.splitlines(),
                     test_suite='tests',
                     tests_require=test_requirements
                     )


if __name__ == "__main__":
    main()
