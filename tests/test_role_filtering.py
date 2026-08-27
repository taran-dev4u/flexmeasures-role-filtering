"""Unit tests for FlexMeasures multi-tenant role filtering."""

import unittest
from flexmeasures_rbac.accounts import AccountManager

class TestAccountRoleFiltering(unittest.TestCase):
    def setUp(self):
        self.accounts_data = [
            {
                "id": 1,
                "name": "Grid Operator A",
                "tenant_id": 100,
                "users": [{"name": "Alice", "roles": ["admin", "operator"]}]
            },
            {
                "id": 2,
                "name": "Battery Storage B",
                "tenant_id": 100,
                "users": [{"name": "Bob", "roles": ["viewer"]}]
            },
            {
                "id": 3,
                "name": "Solar Farm C",
                "tenant_id": 200,
                "users": [{"name": "Charlie", "roles": ["admin"]}]
            }
        ]
        self.manager = AccountManager(self.accounts_data)

    def test_filter_by_admin_role_unscoped(self):
        res = self.manager.filter_accounts_by_role("admin")
        self.assertEqual(len(res), 2)
        self.assertEqual([a["id"] for a in res], [1, 3])

    def test_filter_by_admin_role_tenant_scoped(self):
        res = self.manager.filter_accounts_by_role("admin", user_scope_tenant_id=100)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["id"], 1)

    def test_filter_by_nonexistent_role(self):
        res = self.manager.filter_accounts_by_role("super_user")
        self.assertEqual(len(res), 0)

if __name__ == "__main__":
    unittest.main()
