python based web frontend test
==============================

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ashishb/python_based_web_frontend_test/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


A testing framework for testing (and ensuring) that all web based end points are tested (at least once).

To use this framework

1. Instead of inheriting from unittest.TestCase inherit from frontend_testing_helper.FrontendTestBase

2. Declare which method tests which end point by applying the decorator FrontendTestBase.Tests('/url-endpoint/') to test method.

See [sample code](https://github.com/ashishb/python_based_web_frontend_test/blob/master/samples/flask_sample_code_test.py) as an example.



