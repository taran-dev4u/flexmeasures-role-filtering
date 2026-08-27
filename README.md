# FlexMeasures — Multi-Tenant Account Role Filtering & Access-Scoped UI

[![CI](https://github.com/taran-dev4u/flexmeasures-role-filtering/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/flexmeasures-role-filtering/actions/workflows/ci.yml)
[![Upstream PR Merged](https://img.shields.io/badge/FlexMeasures-PR%20%232353%20Merged-green?logo=github)](https://github.com/FlexMeasures/flexmeasures/pull/2353)
[![Upstream PR Open](https://img.shields.io/badge/FlexMeasures-PR%20%232443-blue?logo=github)](https://github.com/FlexMeasures/flexmeasures/pull/2443)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-206%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/FlexMeasures/flexmeasures)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Production open-source package extending [FlexMeasures](https://github.com/FlexMeasures/flexmeasures), the intelligent Energy Management System (EMS).

---

## 🎯 Background & Problem Statement

1. **Multi-Tenant Account Role Filtering (PR #2353):** In multi-tenant energy asset operations, tenant administrators require the ability to query, filter, and inspect accounts and users by specific assigned roles through both REST API endpoints and web UI dropdown selectors without crossing tenant isolation security boundaries.
2. **Plugin Loader CWD Folder Shadowing (PR #2443):** When a plugin package is installed in the Python environment, but FlexMeasures is launched from a working directory containing a folder with the same name, the loader previously took the relative file path branch and re-executed `__init__.py`, disconnecting Blueprints and causing plugin routes to 404.

---

## 💡 Solution Architecture

- **Authorization-Bounded Queries:** Added role-based filtering to Accounts API endpoints with explicit tenant isolation guards.
- **Access-Scoped UI Selector:** Implemented UI role selector component in Jinja2 / TypeScript.
- **Plugin Loader Prioritization:** Differentiated explicit file paths from package names, prioritizing installed modules and preventing folder shadowing.
- **Automated Regression Test Suites:** Full test coverage across API filtering, tenant isolation, and plugin loader mechanics.

---

## 🏛️ Upstream Pull Requests

- **Repository:** [FlexMeasures/flexmeasures](https://github.com/FlexMeasures/flexmeasures)
- **Pull Request #2353:** [Filter organisations by account role](https://github.com/FlexMeasures/flexmeasures/pull/2353) — **Merged upstream** by Seita Energy / FlexMeasures maintainers.
- **Pull Request #2443:** [fix(plugin_utils): prioritize installed package import over relative cwd path in plugin loader](https://github.com/FlexMeasures/flexmeasures/pull/2443) — **Open / In Review**.

---

## 📄 License

Licensed under the Apache License, Version 2.0.

<!-- sync: 1787836796.695834 -->

<!-- priority_sync: 1787836823.3067534 -->

<!-- demo_verified_sync: 1787840484.6128848 -->
