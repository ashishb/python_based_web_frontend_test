"""An example of using frontend_testing_helper with flask as a sample framework.

The code will work with any framework, just modify the _GetEndpointsList
accordingly.
"""

import unittest

import flask_sample_code
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from frontend_testing_helper import FrontendTestBase

class FlaskSampleCodeTest(FrontendTestBase):

  @classmethod
  def setUpClass(cls):
    FrontendTestBase.setUpClass()

  def setUp(self):
    super(FlaskSampleCodeTest, self).setUp()
    pass

  @classmethod
  def _GetEndpointsList(cls):
    """This must be over-ridden with framework specific code for extracting list
    of all url endpoints."""
    endpoint_list = list()
    for rule in flask_sample_code.app.url_map.iter_rules():
      if rule.endpoint != 'static':
        endpoint_list.append(rule.rule)
    return endpoint_list

  """
  Remove one or more of the tests listed below, to see failures.
  """

  @FrontendTestBase.Tests('/path1/')
  def test_path2(self):
    pass

  @FrontendTestBase.Tests('/path2/<ip>')
  def test_path1(self):
    pass


if __name__ == '__main__':
  unittest.main()
