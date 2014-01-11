python_based_web_frontend_test
==============================

A testing framework for testing (and ensuring) that all web based end points are tested (at least once).

To use this framework

1. Instead of inheriting from unittest.TestCase inherit from frontend_testing_helper.FrontendTestBase
2. Declare which method tests which end point by applying the decorator FrontendTestBase.Tests('/url-endpoint/') to test method.

See samples/ dir for an example.
