# FlexMeasures — Multi-Tenant Account Role Filtering & Access-Scoped UI

[![CI](https://github.com/taran-dev4u/flexmeasures-role-filtering/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/flexmeasures-role-filtering/actions/workflows/ci.yml)
[![Upstream PR](https://img.shields.io/badge/FlexMeasures-PR%20%232353%20Merged-green?logo=github)](https://github.com/FlexMeasures/flexmeasures/pull/2353)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-206%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/FlexMeasures/flexmeasures)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Production open-source feature implementation extending [FlexMeasures](https://github.com/FlexMeasures/flexmeasures), the intelligent Energy Management System (EMS).

---

## 🎯 Background & Problem Statement

In multi-tenant energy asset operations, tenant administrators require the ability to query, filter, and inspect accounts and users by specific assigned roles (e.g. `Account Admin`, `Asset Operator`, `Viewer`) through both REST API endpoints and web UI dropdown selectors without crossing tenant isolation security boundaries.

---

## 💡 Solution Architecture

- **Authorization-Bounded Queries:** Added role-based filtering to Accounts API endpoints with explicit tenant isolation guards.
- **Access-Scoped UI Selector:** Implemented UI role selector component in Jinja2 / TypeScript.
- **Automated Regression Test Suite:** Validated multi-role users, pagination edges, and tenant boundaries across 66+ focused test cases.
- **OpenAPI Schema Generation:** Updated Marshmallow schemas and generated OpenAPI v3 documentation.

---

## 🏛️ Upstream Merged Pull Request

- **Repository:** [FlexMeasures/flexmeasures](https://github.com/FlexMeasures/flexmeasures)
- **Pull Request:** [#2353 — Filter organisations by account role](https://github.com/FlexMeasures/flexmeasures/pull/2353)
- **Status:** **Merged upstream** by Seita Energy / FlexMeasures maintainers.

---

## 📄 License

Licensed under the Apache License, Version 2.0.
