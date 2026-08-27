"""Marshmallow & OpenAPI schema definitions for Account Role filtering."""
from typing import Dict, Any

class AccountQuerySchema:
    @staticmethod
    def get_openapi_spec() -> Dict[str, Any]:
        return {
            "name": "role",
            "in": "query",
            "description": "Filter accounts by assigned user role",
            "required": False,
            "schema": {"type": "string"}
        }
