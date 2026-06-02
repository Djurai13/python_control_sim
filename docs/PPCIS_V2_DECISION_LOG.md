# PPCIS v2.0 Decision Log

Status: ACTIVE

---

# Decision 001

Date: 2026-06-02

Title:
Preserve PPCIS v1.0 Strategic Assets

Decision:
Do not rewrite functioning strategic assets.

Reason:
Existing simulation and forecasting capabilities represent core intellectual property.

Impact:
PPCIS v2.0 will evolve from PPCIS v1.0 rather than replace it.

Status:
APPROVED

---

# Decision 002

Date: 2026-06-02

Title:
Progressive Evolution Strategy

Decision:
Use incremental enhancement rather than full-system redesign.

Reason:
Reduces risk and protects existing value.

Impact:
All future work must follow phased implementation.

Status:
APPROVED

---

# Decision 003

Date: 2026-06-02

Title:
Repository Branch Strategy

Decision:

master

* Stable

release/v1

* PPCIS v1 maintenance

development

* PPCIS v2 integration

feature/*

* Active development

Status:
APPROVED

---

# Decision 004

Date: 2026-06-02

Title:
Create release/v1 Branch

Decision:
Preserve PPCIS v1.0 as a protected baseline.

Impact:
Future v2 work cannot accidentally alter v1 history.

Status:
APPROVED

---

# Decision 005

Date: 2026-06-02

Title:
PostgreSQL + PostGIS Platform

Decision:
Adopt PostgreSQL with PostGIS as the official database platform.

Reason:
Supports spatial intelligence and long-term scalability.

Status:
APPROVED

---

# Decision 006

Date: 2026-06-02

Title:
Dockerized Database Strategy

Decision:
Run PostgreSQL/PostGIS using Docker.

Reason:
Environment consistency and deployment portability.

Status:
APPROVED

---

# Decision 007

Date: 2026-06-02

Title:
Simulation Persistence Phase

Decision:
Add a dedicated Simulation Persistence Platform phase.

Reason:
Simulation history is a strategic capability and should not be embedded inside other phases.

Status:
APPROVED

---

# Decision 008

Date: 2026-06-02

Title:
Forecast Intelligence Before GIS Intelligence

Decision:
Move Forecast Intelligence ahead of GIS Intelligence.

Reason:
Forecasting is a Tier 1 strategic asset.

Status:
APPROVED

---

# Decision 009

Date: 2026-06-02

Title:
Testing Is Cross-Cutting

Decision:
Testing is integrated into every phase.

Reason:
Quality must be built continuously.

Status:
APPROVED

---

# Decision 010

Date: 2026-06-02

Title:
Program Governance Framework

Decision:
Create formal governance documents for PPCIS v2.0.

Documents:

* PPCIS_V2_PROGRAM_CONTROL.md
* PPCIS_V2_PROJECT_STATUS.md
* PPCIS_V2_DECISION_LOG.md
* PPCIS_V2_SPRINT_LOG.md
* PPCIS_V2_MASTER_PLAN.md
* PPCIS_V2_EXECUTION_ROADMAP_V2.md

Status:
APPROVED
