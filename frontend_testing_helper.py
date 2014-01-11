"python based web frontend testing module."""

import unittest

_endpoints_testers = dict()


class FrontendTestBase(unittest.TestCase):
  """Tests the url calls directly."""

  @classmethod
  def setUpClass(cls):
    # A map of end point (url) to function name.
    FrontendTestBase._endpoints_testers_list = cls._GetEndpointsList()
    global _endpoints_testers
    for x in FrontendTestBase._endpoints_testers_list:
      if FrontendTestBase._endpoints_testers.get(x, None) is None:
        FrontendTestBase._endpoints_testers[x] = None

  def setUp(self):
    pass

  @classmethod
  def _GetEndpointsList(cls):
    """ Must be defined by child class to return a list/set of all url
    endpoints."""
    return list()

  @staticmethod
  def Tests(endpoint):
    """Use this decorator to map url endpoint to the testing method."""
    def decoratorFunc(function):
      global _endpoints_testers
      _endpoints_testers[endpoint] = function
      return function
    return decoratorFunc

  def test_allEndpointsAreCalled(self):
    global _endpoints_testers
    failed = False
    for x in self._GetEndpointsList():
      if _endpoints_testers.get(x, None) is None:
        print '%s is not tested.' % x
        failed = True
    self.assertFalse(failed, 'Some paths are missing tests.')
