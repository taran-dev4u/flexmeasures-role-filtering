"""Tenant permission boundary enforcement guards."""
from typing import Optional

def check_tenant_permission(requesting_tenant: int, target_tenant: int) -> bool:
    return requesting_tenant == target_tenant
