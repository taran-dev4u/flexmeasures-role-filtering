"""Unit tests for tenant permissions."""
import unittest
from flexmeasures_rbac.permissions import check_tenant_permission

class TestPermissions(unittest.TestCase):
    def test_tenant_boundary(self):
        self.assertTrue(check_tenant_permission(10, 10))
        self.assertFalse(check_tenant_permission(10, 20))
