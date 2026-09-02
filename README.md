# FlexMeasures — Energy Flexibility Engine, Role-Based Access Control & Multi-Commodity Scheduler

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask%20%7C%20SQLAlchemy-red.svg)](https://flask.palletsprojects.com/)
[![Energy](https://img.shields.io/badge/Domain-Smart%20Grid%20Flexibility-green.svg)](https://flexmeasures.io/)
[![Open Source](https://img.shields.io/badge/Open%20Source-Merged%20Contributions-blue.svg)](https://github.com/FlexMeasures/flexmeasures)

---

## 📌 Executive Summary & Open Source Contributions

**FlexMeasures** is an open-source intelligent energy management system (EMS) and multi-commodity flexibility optimization engine supporting battery storage, heat pumps, electric vehicles (EV), and industrial manufacturing dispatch.

This repository highlights **Upstream Engineering Contributions** authored by **Taran Mamidala** to the primary open-source platform ([`FlexMeasures/flexmeasures`](https://github.com/FlexMeasures/flexmeasures)).

---

## 🚀 Key Upstream Engineering Contributions

### 1. Multi-Tenant Role-Based Access Control (RBAC) & Account Role Filtering ([PR #2353](https://github.com/FlexMeasures/flexmeasures/pull/2353))
- Implemented robust multi-tenant role filtering across API endpoints and UI administrative views, ensuring user account actions and device controls respect strict organizational boundaries.

### 2. Multi-Commodity Scheduler Cost Breakdown Export ([PR #2448](https://github.com/FlexMeasures/flexmeasures/pull/2448))
- Solved an architectural gap where linear and highspy optimization solvers calculated per-commodity costs (`model.commodity_costs`), but `StorageScheduler` only exported flat `commitment_costs`.
- Emitted `commodity_costs` dictionary result for multi-commodity or non-default setups and persisted it in `rq_job.meta["scheduler_info"]["commodity_costs"]`.

### 3. Plugin Loader CWD Isolation ([PR #2443](https://github.com/FlexMeasures/flexmeasures/pull/2443))
- Investigated and resolved plugin loader current-working-directory folder shadowing defects by prioritizing `importlib.import_module` for installed plugins.

---

## 📂 Repository Structure

```
flexmeasures-role-filtering/
├── src/flexmeasures/
│   ├── data/models/planning/        # StorageScheduler and linear optimization models
│   ├── data/services/scheduling.py  # Asynchronous background job worker and meta persistence
│   └── auth/                        # RBAC decorators and role validation logic
├── tests/                           # Planning, commitments, and scheduling test suites
└── README.md                        # Documentation
```

---

## 👨‍💻 Author & Contributor
- **Author:** Taran Mamidala
- **Upstream Repository:** [FlexMeasures/flexmeasures](https://github.com/FlexMeasures/flexmeasures)
