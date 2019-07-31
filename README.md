Robotframework-MongoDB-Library
==============================

A library for interacting with MongoDB from RobotFramework.

Uses pymongo.

License
-------
See LICENSE file for updated license information

Install
-------
You can install by pulling down source and executing the following:

'''
sudo python setup.py install
'''


$ pip install -U setuptools wheel 
$ python setup.py sdist bdist_wheel 
$ pip install twine 

$ python3 setup.py sdist bdist_wheel

chmod 600 ~/.pypirc

twine upload --repository testpypi dist/* 
twine upload --repository pypi dist/* 
