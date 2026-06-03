# PPCIS v2.0 Import Architecture

Version: 1.0

Status: Approved

Source:

Phase 3 – Data Import Platform

Coverage:

Sprint 3.1 through Sprint 3.6A

---

# Purpose

The PPCIS Import Platform provides a standardized framework for importing, validating, scoring, auditing, and approving ecological and operational datasets.

The architecture supports:

* CSV Imports
* Excel Imports
* GeoJSON Imports

Future support:

* API Imports
* XML Imports
* Parquet Imports

---

# Phase 3 Objective

Enable PPCIS to ingest real-world ecological and operational data.

---

# Architecture Principles

1. Source Agnostic

All import sources follow the same workflow.

2. Validation First

Data must be validated before acceptance.

3. Quality Assessment

Validation alone is insufficient.

4. Full Auditability

All imports must be traceable.

5. Extensible Design

New import types can be added without redesign.

6. Staging Before Production

Imported data must never enter production directly.

---

# Import Platform Overview

Import Source
↓
Import Engine
↓
Validation Engine
↓
Quality Engine
↓
Staging Area
↓
Approval Workflow
↓
Persistence Layer

---

# Sprint 3.1

# Import Architecture

Purpose:

Provide a unified architecture for all import operations.

---

## Core Components

### Import Controller

Responsibilities:

* Receive import requests
* Route files
* Trigger import workflows

---

### Import Service

Responsibilities:

* Coordinate imports
* Execute workflows
* Manage lifecycle

---

### Import Registry

Responsibilities:

* Register supported import types
* Route handlers

Example:

CSV → CSV Import Handler

Excel → Excel Import Handler

GeoJSON → GeoJSON Import Handler

---

### Import Staging Layer

Purpose:

Temporary storage before approval.

Characteristics:

* Non-production
* Auditable
* Reversible

---

### Import Audit Layer

Purpose:

Record every import activity.

---

# Sprint 3.2

# CSV Import Framework

Purpose:

Import structured tabular datasets.

Supported Examples:

* Observations
* Surveys
* Population Counts
* Operational Data

---

## CSV Workflow

CSV File
↓
Parser
↓
Schema Mapping
↓
Validation
↓
Quality Assessment
↓
Staging

---

## Components

### CSV Parser

Responsibilities:

* Header detection
* Row parsing
* Encoding handling

---

### Schema Mapper

Responsibilities:

* Map columns to PPCIS entities
* Handle aliases
* Normalize names

Example:

population_count
↓

population_estimate

---

## Error Handling

Supported:

* Missing columns
* Invalid types
* Empty files
* Encoding issues

---

# Sprint 3.3

# Excel Import Framework

Purpose:

Import spreadsheet-based datasets.

Supported Formats:

* XLSX
* XLS

---

## Excel Workflow

Excel File
↓
Workbook Reader
↓
Worksheet Selection
↓
Schema Mapping
↓
Validation
↓
Quality Assessment
↓
Staging

---

## Components

### Workbook Reader

Responsibilities:

* Open workbook
* Enumerate worksheets

---

### Worksheet Processor

Responsibilities:

* Select active worksheet
* Extract rows

---

### Schema Mapper

Shared with CSV framework.

---

## Error Handling

Supported:

* Missing worksheets
* Empty worksheets
* Invalid workbook structure

---

# Sprint 3.4

# GeoJSON Import Framework

Purpose:

Import spatial datasets.

Supported Objects:

* Point
* LineString
* Polygon
* MultiPolygon

---

## GeoJSON Workflow

GeoJSON
↓
Parser
↓
Geometry Validation
↓
Attribute Validation
↓
Quality Assessment
↓
Staging

---

## Components

### GeoJSON Parser

Responsibilities:

* Parse FeatureCollections
* Parse Features
* Extract Geometry

---

### Geometry Validator

Responsibilities:

* Geometry integrity
* Topology validation
* Coordinate validation

---

### CRS Validator

Responsibilities:

* Validate coordinate system
* Normalize projections

---

## Spatial Rules

Latitude:

-90 to 90

Longitude:

-180 to 180

---

# Sprint 3.5

# Validation Engine

Purpose:

Determine whether imported data is acceptable.

---

# Validation Architecture

Import Source
↓
Validation Engine
↓
Validation Results
↓
Staging

---

## Validation Layers

### Layer 1

Structural Validation

Checks:

* Required fields
* Required columns
* Schema presence

---

### Layer 2

Data Type Validation

Checks:

* Integer
* Float
* Date
* Boolean
* String
* Geometry

---

### Layer 3

Range Validation

Checks:

* Latitude range
* Longitude range
* Numeric limits

---

### Layer 4

Business Validation

Checks:

* Future dates
* Negative populations
* Invalid species

---

### Layer 5

Spatial Validation

Checks:

* Geometry validity
* CRS validity
* Topology

---

### Layer 6

Relationship Validation

Checks:

* Region existence
* Species existence
* Survey existence

---

### Layer 7

Freshness Validation

Checks:

* Dataset age
* Data currency

---

### Layer 8

Schema Drift Validation

Checks:

* Added fields
* Removed fields
* Changed types

---

# Validation Rule Registry

## validation_rules

Stores:

* Rule ID
* Rule Name
* Rule Type
* Severity
* Expression
* Version

---

## Validation Severity Model

INFO

WARNING

ERROR

CRITICAL

---

## Validation Execution Model

Record-Level

Example:

Single observation failure

---

Dataset-Level

Example:

Missing required column

---

## Validation Results

Stores:

* Rule
* Severity
* Message
* Record Reference
* Timestamp

---

# Sprint 3.5A

# Validation Review Outcomes

Approved Enhancements:

* Rule Classification
* Rule Lifecycle Management
* Validation Short-Circuiting
* Temporal Validation
* Remediation Guidance
* Validation Metrics
* Approval Workflow

---

# Sprint 3.6

# Data Quality Scoring

Purpose:

Measure quality of valid data.

Validation answers:

"Is data valid?"

Quality answers:

"How good is the data?"

---

# Quality Dimensions

## Completeness

Measures:

* Missing values
* Null values

---

## Validity

Measures:

* Validation pass rate

---

## Consistency

Measures:

* Duplicate values
* Contradictions

---

## Reference Compliance

Measures:

* Registry compliance
* Reference integrity

---

## Freshness

Measures:

* Data age
* Update frequency

---

## Spatial Quality

Measures:

* Geometry quality
* Coverage quality

---

# Composite Quality Score

Produces:

Overall Quality Score

Range:

0–100

---

## Quality Classes

Platinum

95–100

---

Gold

85–94

---

Silver

70–84

---

Bronze

50–69

---

Reject

Below 50

---

# Quality Reports

Every import produces:

* Overall Score
* Dimension Scores
* Warnings
* Recommendations

---

# Sprint 3.6A

# Quality Review Outcomes

Approved Enhancements:

* Dataset-Specific Profiles
* Freshness Policies
* Critical Quality Gates
* Quality Explanation Reports
* Source Reliability Index
* Dataset-Specific Thresholds

---

# Audit Architecture

Every import operation must record:

* Import Job
* Source Type
* Filename
* Timestamp
* User
* Validation Outcome
* Quality Outcome
* Approval Decision

---

# Approval Workflow

Import
↓
Validation
↓
Quality Assessment
↓
Staging
↓
Review
↓
Approval
↓
Persistence

---

# Error Handling Framework

Categories:

Validation Error

Quality Error

Import Error

Parser Error

System Error

---

# Database Integration

Primary Tables:

* import_jobs

* import_files

* import_batches

* import_audit_log

* validation_rules

* validation_profiles

* validation_results

* quality_assessments

* quality_dimension_scores

---

# Future Expansion

Planned Support:

* REST APIs
* XML Imports
* Parquet Imports
* Streaming Data
* Sensor Feeds

No architectural redesign required.

---

# Phase 3 Deliverables

Completed Architecture Deliverables:

✓ Import Center

✓ Import Audit Trail

✓ Validation Framework

✓ Quality Assessment Engine

---

# Implementation Mapping

IW0.2

Import Center Build

Implements:

* Import Controller
* Import Service
* Import Registry
* Import Staging

---

IW0.3

Validation Engine Build

Implements:

* Validation Pipeline
* Validation Registry
* Validation Results

---

IW0.4

Quality Engine Build

Implements:

* Quality Scoring
* Quality Profiles
* Quality Reports

---

# Architecture Status

Phase 3:

DESIGN COMPLETE

Implementation Status:

PENDING

Approved For:

Implementation Wave 0
