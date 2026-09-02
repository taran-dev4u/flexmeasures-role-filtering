# FlexMeasures Contributions — RBAC & Multi-Commodity Scheduler

Engineering contributions to the open-source **FlexMeasures** energy flexibility engine ([FlexMeasures/flexmeasures](https://github.com/FlexMeasures/flexmeasures)).

## Key Contributions

- **Multi-Tenant Account Role Filtering (PR #2353):** Implemented role-based access control across API endpoints and UI views.
- **Multi-Commodity Cost Breakdown Export (PR #2448):** Added per-commodity cost export from linear/highspy optimization solvers in `StorageScheduler` outputs and persisted in job metadata.
- **Plugin Loader CWD Isolation (PR #2443):** Resolved module shadowing when local directories match installed plugin names.
