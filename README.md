# Python Flask web frontend test checker [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


A testing framework for testing (and ensuring) that all web based end points are tested (at least once).

To use this framework

1. Instead of inheriting from unittest.TestCase inherit from frontend_testing_helper.FrontendTestBase

2. Declare which method tests which end point by applying the decorator FrontendTestBase.Tests('/url-endpoint/') to test method.

See [sample code](https://github.com/ashishb/python_based_web_frontend_test/blob/master/samples/flask_sample_code_test.py) as an example.



