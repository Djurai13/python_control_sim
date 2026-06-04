# PPCIS v2.0 Database Schema

Version: 1.0

Status: Approved Baseline

---

# Purpose

This document defines the baseline database schema for PPCIS v2.0.

The schema supports:

* Data Import Platform
* Simulation Persistence Platform
* Forecast Intelligence Platform
* GIS Intelligence Platform
* Security Foundation
* Operations Platform
* Reporting Platform

The schema is designed for PostgreSQL + PostGIS and implemented through SQLAlchemy 2.x and Alembic.

---

# Technology Stack

Database Engine:

PostgreSQL

Spatial Extension:

PostGIS

ORM:

SQLAlchemy 2.x

Migration Framework:

Alembic

---

# Schema Domains

The database is organized into the following domains:

1. Security
2. Import Management
3. Validation
4. Data Quality
5. Simulation
6. Scenario Management
7. Forecasting
8. GIS Intelligence
9. Operations
10. Reporting
11. Audit

---

# Common Audit Fields

All primary business entities shall contain:

created_at TIMESTAMP

updated_at TIMESTAMP

created_by UUID

updated_by UUID

---

# Security Domain

## users

Purpose:

Platform users.

Columns:

* id UUID PK
* username VARCHAR(100)
* email VARCHAR(255)
* password_hash TEXT
* is_active BOOLEAN
* last_login TIMESTAMP

Indexes:

* username
* email

---

## roles

Columns:

* id UUID PK
* role_name VARCHAR(100)
* description TEXT

Examples:

* Administrator
* Analyst
* Operator
* Viewer

---

## permissions

Columns:

* id UUID PK
* permission_name VARCHAR(150)
* description TEXT

---

## user_roles

Columns:

* user_id UUID FK users
* role_id UUID FK roles

Composite PK:

(user_id, role_id)

---

## role_permissions

Columns:

* role_id UUID FK roles
* permission_id UUID FK permissions

Composite PK:

(role_id, permission_id)

---

# Import Management Domain

## import_jobs

Purpose:

Tracks every import request.

Columns:

* id UUID PK
* source_type VARCHAR(50)
* filename VARCHAR(255)
* file_path TEXT
* import_status VARCHAR(50)
* started_at TIMESTAMP
* completed_at TIMESTAMP

Status Values:

* Pending
* Running
* Completed
* Failed

---

## import_batches

Purpose:

Logical grouping of imported records.

Columns:

* id UUID PK
* import_job_id UUID FK import_jobs
* batch_name VARCHAR(255)
* record_count INTEGER

---

## import_files

Columns:

* id UUID PK
* import_job_id UUID FK import_jobs
* original_filename VARCHAR(255)
* file_size BIGINT
* checksum VARCHAR(128)

---

## import_audit_log

Columns:

* id UUID PK
* import_job_id UUID FK import_jobs
* event_type VARCHAR(100)
* event_timestamp TIMESTAMP
* message TEXT

---

# Validation Domain

## validation_rules

Columns:

* id UUID PK
* rule_code VARCHAR(100)
* rule_name VARCHAR(255)
* rule_type VARCHAR(100)
* severity VARCHAR(50)
* expression TEXT
* version INTEGER
* is_active BOOLEAN

---

## validation_profiles

Columns:

* id UUID PK
* profile_name VARCHAR(255)
* description TEXT

Examples:

* Observation Profile
* Weather Profile
* Region Profile

---

## validation_profile_rules

Columns:

* profile_id UUID FK validation_profiles
* rule_id UUID FK validation_rules

---

## validation_results

Columns:

* id UUID PK
* import_job_id UUID FK import_jobs
* rule_id UUID FK validation_rules
* severity VARCHAR(50)
* record_reference VARCHAR(255)
* message TEXT
* validation_timestamp TIMESTAMP

---

# Data Quality Domain

## quality_assessments

Columns:

* id UUID PK
* import_job_id UUID FK import_jobs
* overall_score DECIMAL(5,2)
* quality_class VARCHAR(50)
* assessed_at TIMESTAMP

Quality Classes:

* Platinum
* Gold
* Silver
* Bronze
* Reject

---

## quality_dimension_scores

Columns:

* id UUID PK
* assessment_id UUID FK quality_assessments
* dimension_name VARCHAR(100)
* score DECIMAL(5,2)

Dimensions:

* Completeness
* Validity
* Consistency
* Reference Compliance
* Freshness
* Spatial Quality

---

# Simulation Domain

## simulation_runs

Purpose:

Represents a simulation execution.

Columns:

* id UUID PK
* simulation_name VARCHAR(255)
* started_at TIMESTAMP
* completed_at TIMESTAMP
* status VARCHAR(50)

Status:

* Running
* Completed
* Failed

---

## simulation_parameters

Columns:

* id UUID PK
* simulation_run_id UUID FK simulation_runs
* parameter_name VARCHAR(255)
* parameter_value TEXT

---

## simulation_results

Columns:

* id UUID PK
* simulation_run_id UUID FK simulation_runs
* result_name VARCHAR(255)
* result_value NUMERIC
* result_timestamp TIMESTAMP

---

# Scenario Management Domain

## scenarios

Columns:

* id UUID PK
* scenario_name VARCHAR(255)
* description TEXT
* scenario_status VARCHAR(50)

---

## scenario_versions

Columns:

* id UUID PK
* scenario_id UUID FK scenarios
* version_number INTEGER
* configuration_json JSONB

---

# Forecast Domain

## forecast_models

Columns:

* id UUID PK
* model_name VARCHAR(255)
* model_version VARCHAR(50)
* description TEXT

---

## forecast_runs

Columns:

* id UUID PK
* forecast_model_id UUID FK forecast_models
* run_timestamp TIMESTAMP

---

## forecast_results

Columns:

* id UUID PK
* forecast_run_id UUID FK forecast_runs
* forecast_period DATE
* forecast_value NUMERIC

---

# GIS Intelligence Domain

## regions

Columns:

* id UUID PK
* region_name VARCHAR(255)
* geometry GEOMETRY(MULTIPOLYGON,4326)

---

## spatial_layers

Columns:

* id UUID PK
* layer_name VARCHAR(255)
* layer_type VARCHAR(100)
* geometry GEOMETRY(GEOMETRY,4326)

---

## hotspots

Columns:

* id UUID PK
* hotspot_name VARCHAR(255)
* geometry GEOMETRY(POINT,4326)
* risk_score NUMERIC

---

## risk_maps

Columns:

* id UUID PK
* map_name VARCHAR(255)
* generated_at TIMESTAMP

---

# Operations Domain

## tasks

Columns:

* id UUID PK
* title VARCHAR(255)
* description TEXT
* status VARCHAR(50)
* due_date DATE

---

## task_assignments

Columns:

* id UUID PK
* task_id UUID FK tasks
* user_id UUID FK users
* assigned_at TIMESTAMP

---

## alerts

Columns:

* id UUID PK
* alert_type VARCHAR(100)
* alert_message TEXT
* alert_status VARCHAR(50)

---

# Reporting Domain

## reports

Columns:

* id UUID PK
* report_name VARCHAR(255)
* report_type VARCHAR(100)
* generated_at TIMESTAMP

---

## report_exports

Columns:

* id UUID PK
* report_id UUID FK reports
* export_format VARCHAR(50)
* file_path TEXT

Formats:

* PDF
* CSV

---

# Audit Domain

## audit_log

Purpose:

System-wide audit trail.

Columns:

* id UUID PK
* entity_name VARCHAR(255)
* entity_id UUID
* action_type VARCHAR(100)
* action_timestamp TIMESTAMP
* user_id UUID FK users
* details JSONB

---

# Indexing Strategy

Create indexes on:

* Foreign keys
* Import status
* Simulation status
* Forecast timestamps
* Audit timestamps

Create GIN indexes for:

* JSONB fields

Create GiST indexes for:

* Geometry fields

---

# Migration Strategy

All schema changes shall be managed through Alembic.

Rules:

1. No manual schema modification.
2. Every schema change requires migration.
3. Migrations must be version controlled.
4. Migrations must be reviewed before merge.

---

# Implementation Baseline

IW0.1 Database Foundation Build shall implement:

Phase 1 Tables:

* users
* roles
* permissions
* user_roles
* role_permissions

Phase 2 Tables:

* import_jobs
* import_batches
* import_files
* import_audit_log

Phase 3 Tables:

* validation_rules

* validation_profiles

* validation_results

* quality_assessments

* quality_dimension_scores

Simulation tables remain reserved for Phase 4 implementation.
