

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

# Decision 011

Date: 2026-06-02

Title:
Authoritative Roadmap Selection

Decision:

PPCIS_V2_EXECUTION_ROADMAP_V2.md is designated as the authoritative execution roadmap for PPCIS v2.0.

Reason:

Roadmap Revision 2 reflects the approved architecture review, revised phase ordering, Simulation Persistence Platform, Forecast Intelligence prioritization, and governance updates.

Impact:

All future planning and execution activities shall reference PPCIS_V2_EXECUTION_ROADMAP_V2.md.

PPCIS_V2_EXECUTION_ROADMAP.md is retained only as a historical artifact.

Status:
APPROVED

# Decision 012

Date: 2026-06-02

Title:
Governance Document Source Control Policy

Decision:

All PPCIS v2.0 governance artifacts must be maintained under the docs directory and committed to source control.

Required Governance Documents:

- PPCIS_V2_MASTER_PLAN.md
- PPCIS_V2_PROGRAM_CONTROL.md
- PPCIS_V2_EXECUTION_ROADMAP_V2.md
- PPCIS_V2_PROJECT_STATUS.md
- PPCIS_V2_DECISION_LOG.md
- PPCIS_V2_SPRINT_LOG.md

Reason:

Project governance documents represent the authoritative source of truth for architecture, planning, decision history, execution status, and sprint history.

Governance artifacts must be protected by version control to ensure:

- Traceability
- Auditability
- Team collaboration
- Historical reconstruction
- Disaster recovery

Impact:

Governance documents become first-class project artifacts and must be updated as part of normal project execution.

Future governance documents shall not remain as local-only files.

Status:
APPROVED

Date: 2026-06-02

Title:
Governance Document Source Control Policy

Decision:

All governance artifacts must be committed to source control and maintained under the docs directory.

Required Documents:

- PPCIS_V2_MASTER_PLAN.md
- PPCIS_V2_PROGRAM_CONTROL.md
- PPCIS_V2_EXECUTION_ROADMAP_V2.md
- PPCIS_V2

# Decision 013

Date: 2026-06-02

Title:
Schema Mapping Registry

Decision:

CSV imports shall use a schema mapping registry rather than relying on fixed column names.

Reason:

Real-world ecological datasets use inconsistent naming conventions.

Examples:

pop_count
population
count

may all represent the same concept.

Impact:

CSV imports become more resilient to external data sources.

Status:
APPROVED

# Decision 014

Date: 2026-06-02

Title:
Duplicate Detection Required

Decision:

All imports must pass through duplicate detection.

Reason:

Duplicate imports can corrupt:

- Forecasts
- Analytics
- GIS outputs
- Historical observations

Impact:

Import framework requires duplicate detection mechanisms.

Status:
APPROVED

# Decision 015

Date: 2026-06-02

Title:
Geographic Boundary Validation

Decision:

Spatial imports must be validated against supported geographic boundaries.

Reason:

Valid coordinates may still be ecologically invalid.

Impact:

PostGIS validation becomes part of the import framework.

Status:
APPROVED

# Decision 016

Date: 2026-06-02

Title:
Import Recovery Strategy

Decision:

Import jobs must support recovery and restart capabilities.

Statuses:

- PENDING
- PROCESSING
- FAILED
- RECOVERABLE
- COMPLETED

Reason:

Large imports may be interrupted.

Impact:

Import architecture must support resumable processing.

Status:
APPROVED

# Decision 017

Date: 2026-06-02

Title:
Official CSV Templates

Decision:

PPCIS shall provide official CSV templates for supported dataset types.

Templates:

- Population Observations
- Removal Events
- Region Data

Reason:

Reduces user error and simplifies validation.

Impact:

Template management becomes part of the import platform.

Status:
APPROVED

# Decision 018

Date: 2026-06-02

Title:
Worksheet Role Classification

Decision:

Excel worksheets shall be classified before import processing.

Roles:

- DATA
- REFERENCE
- SUMMARY
- SYSTEM
- UNKNOWN

Reason:

Not all worksheets contain importable datasets.

Impact:

Only DATA worksheets proceed to import processing.

Status:
APPROVED

# Decision 019

Date: 2026-06-02

Title:
Cross-Sheet Validation

Decision:

Excel imports shall support cross-sheet integrity validation.

Reason:

Workbook datasets may reference records located in other worksheets.

Impact:

Excel import framework requires cross-sheet validation capabilities.

Status:
APPROVED

# Decision 020

Date: 2026-06-02

Title:
Canonical Import Core

Decision:

CSV and Excel imports shall use a shared import core architecture.

Reason:

Avoid duplicate validation, staging, auditing, and quality assessment logic.

Impact:

Import adapters normalize source data before entering the shared import pipeline.

Status:
APPROVED

# Decision 021

Date: 2026-06-02

Title:
GeoJSON Canonical Import Architecture

Decision:

GeoJSON imports shall use the same canonical import architecture employed by CSV and Excel imports.

Processing Pipeline:

- Source Adapter
- Validation Engine
- Quality Assessment
- Duplicate Detection
- Staging Layer
- Import Audit Logging

Reason:

All import mechanisms must follow a consistent governance, validation, auditing, and recovery model.

Impact:

GeoJSON imports become fully integrated into the PPCIS Import Platform architecture.

Status:
APPROVED

# Decision 022

Date: 2026-06-02

Title:
Coordinate Reference System Validation

Decision:

All GeoJSON imports shall undergo Coordinate Reference System (CRS) validation before spatial processing.

Initial Supported CRS:

- EPSG:4326 (WGS84)

Future support may include:

- EPSG:3857
- National and regional CRS standards

Reason:

GeoJSON datasets may originate from multiple GIS platforms using different coordinate systems.

Without CRS validation, imported geometries may be stored in incorrect locations, resulting in invalid spatial analysis and reporting.

Impact:

The GeoJSON import framework shall include CRS detection, validation, and future transformation capabilities.

Status:
APPROVED

# Decision 023

Date: 2026-06-02

Title:
Spatial Similarity Detection

Decision:

GeoJSON imports shall support spatial similarity detection in addition to exact duplicate detection.

Validation shall consider:

- Geometry overlap percentage
- Centroid distance
- Area difference
- Shape similarity

Reason:

Two spatial features may represent the same real-world object while differing slightly in coordinates.

Exact geometry matching alone is insufficient.

Impact:

The import platform shall support advanced duplicate detection for spatial datasets.

Status:
APPROVED

# Decision 024

Date: 2026-06-02

Title:
Topology Validation Requirements

Decision:

Polygon and MultiPolygon imports shall undergo topology validation.

Validation shall include:

- Self-intersection detection
- Ring validation
- Gap detection
- Overlap detection
- Geometry integrity verification

Reason:

Topologically invalid geometries can corrupt GIS analysis and operational decision-making.

Impact:

Topology validation becomes a mandatory component of the GeoJSON import pipeline.

Status:
APPROVED

# Decision 025

Date: 2026-06-02

Title:
Spatial Metadata Registry

Decision:

All imported spatial datasets shall retain source metadata.

Required metadata includes:

- Source dataset
- Import date
- Original CRS
- Import version
- Validation version
- Geometry type
- Dataset owner

Reason:

Spatial datasets require traceability and auditability throughout their lifecycle.

Impact:

Spatial metadata shall be persisted alongside imported geometries.

Status:
APPROVED

# Decision 026

Date: 2026-06-02

Title:
Spatial Lineage Tracking

Decision:

PPCIS shall maintain lineage records for imported spatial features.

Lineage records shall identify:

- Source file
- Import job
- Source feature identifier
- Imported feature identifier
- Import timestamp

Reason:

Long-term ecological analysis requires traceability from imported geometry back to its original source.

Impact:

Spatial lineage tracking becomes part of the spatial import architecture.

Status:
APPROVED

Date: 2026-06-02

Title:
Template Versioning

Decision:

All official import templates shall be versioned.

Reason:

Template evolution must remain traceable and auditable.

Impact:

Import history stores template version information.

Status:
APPROVED

# Decision 027

Date: 2026-06-02

Title:
API Source Registry and Ownership Model

Decision:

All API integrations shall be registered in the API Source Registry.

Each source shall include:

- Business Owner
- Technical Owner
- Data Steward
- Support Contact
- Service Criticality

Reason:

External data sources require accountability and governance throughout their lifecycle.

Impact:

API imports cannot be deployed without ownership information.

Status:
APPROVED

# Decision 028

Date: 2026-06-02

Title:
Connector Version Registry

Decision:

Every API connector shall be versioned and tracked.

Tracked Information:

- Connector Version
- Supported API Version
- Compatibility Status
- Release Date

Reason:

External APIs evolve independently from PPCIS.

Impact:

Connector compatibility can be managed and audited.

Status:
APPROVED

# Decision 029

Date: 2026-06-02

Title:
Schema Drift Detection Engine

Decision:

The API Import Platform shall include automated schema drift detection.

Detection Scope:

- New Fields
- Removed Fields
- Renamed Fields
- Data Type Changes

Reason:

External APIs may change unexpectedly.

Impact:

Schema changes can be identified before corrupting imported datasets.

Status:
APPROVED

# Decision 030

Date: 2026-06-02

Title:
Data Freshness Validation

Decision:

All API imports shall undergo freshness validation.

Validation Criteria:

- Dataset Timestamp
- Last Updated Timestamp
- Expected Refresh Window

Reason:

Successful API responses may still contain stale data.

Impact:

Stale datasets can be detected before entering production workflows.

Status:
APPROVED

# Decision 031

Date: 2026-06-02

Title:
API Data Provenance Model

Decision:

PPCIS shall maintain provenance records for all API-imported data.

Tracked Information:

- Source API
- Endpoint
- Import Job
- Connector Version
- Transformation Version
- Import Timestamp

Reason:

Long-term auditability requires traceability back to the originating API source.

Impact:

Data provenance becomes part of the import platform architecture.

Status:
APPROVED

# Decision 031

Date: 2026-06-02

Title:
API Data Provenance Model

Decision:

PPCIS shall maintain provenance records for all API-imported data.

Tracked Information:

- Source API
- Endpoint
- Import Job
- Connector Version
- Transformation Version
- Import Timestamp

Reason:

Long-term auditability requires traceability back to the originating API source.

Impact:

Data provenance becomes part of the import platform architecture.

Status:
APPROVED

# Decision 032

Date: 2026-06-02

Title:
API Health Monitoring Framework

Decision:

The API Import Platform shall continuously monitor API health.

Metrics:

- Availability
- Response Time
- Failure Rate
- Uptime Percentage

Reason:

Import reliability depends on source availability and performance.

Impact:

Health metrics become part of operational monitoring.

Status:
APPROVED

# Decision 033

Date: 2026-06-02

Title:
Incremental Import Support

Decision:

The API Import Platform shall support:

- Full Imports
- Incremental Imports
- Delta Imports

Reason:

Large datasets make full synchronization inefficient.

Impact:

Import strategies can scale as dataset volume increases.

Status:
APPROVED

---

# Decision 034

Date: 2026-06-05

Title:
Application Data Access Pattern

Decision:

PPCIS shall implement the Repository Pattern for all persistence operations.

Repositories shall encapsulate:

- Create operations
- Read operations
- Update operations
- Delete operations
- Query logic

Services shall encapsulate:

- Business logic
- Validation
- Authorization checks
- Workflow orchestration
- Transaction management

Application components shall not directly access database persistence mechanisms outside approved repositories.

Reason:

Separation of concerns improves maintainability, testability, scalability, and governance compliance.

Impact:

All future PPCIS domains shall implement repositories before service-layer business logic is introduced.

Status:
APPROVED