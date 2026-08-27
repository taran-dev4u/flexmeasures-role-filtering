"""
Multi-Tenant Account Query Filtering for FlexMeasures EMS.
Provides authorization-bounded querying by role across accounts and users.
"""

from typing import List, Dict, Optional

class AccountManager:
    """Manages tenant accounts and role filtering."""

    def __init__(self, accounts: Optional[List[Dict]] = None):
        self.accounts = accounts or []

    def filter_accounts_by_role(self, role_name: str, user_scope_tenant_id: Optional[int] = None) -> List[Dict]:
        """
        Filter accounts that have users matching role_name within user's authorization tenant scope.
        """
        results = []
        for acc in self.accounts:
            if user_scope_tenant_id is not None and acc.get("tenant_id") != user_scope_tenant_id:
                continue # Tenant isolation boundary
            
            users = acc.get("users", [])
            has_role = any(role_name in u.get("roles", []) for u in users)
            if has_role:
                results.append(acc)
        return results
