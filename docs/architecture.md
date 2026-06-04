# PPCIS Architecture

## Python Population Control Intelligence System

### Ecological Decision Support System (EDSS)

---

# 1. System Overview

The Python Population Control Intelligence System (PPCIS) is an Ecological Decision Support System (EDSS) designed to support invasive species management through simulation, analytics, geospatial intelligence, forecasting, and operational decision support.

The platform combines multiple subsystems into a unified operational environment:

```text
Simulation Engine
        │
        ▼
Optimization Engine
        │
        ▼
GIS Intelligence
        │
        ▼
Operations Dashboard
        │
        ▼
Analytics Engine
        │
        ▼
Prediction Engine
        │
        ▼
Operational Intelligence
```

---

# 2. High-Level Architecture

```text
+------------------------------------------------------+
|              PPCIS Dashboard Platform                |
+------------------------------------------------------+

 Operations Center
 Analytics Engine
 GIS Intelligence
 Prediction Engine

+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|             Operational Intelligence                 |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|               Prediction Engine                      |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|                Analytics Engine                      |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|                 GIS Intelligence                     |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|              Adaptive Optimization                   |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|             Detection & Suppression                  |
+------------------------------------------------------+

                ▲
                │

+------------------------------------------------------+
|               Ecological Simulation                  |
+------------------------------------------------------+
```

---

# 3. Core Components

## 3.1 Simulation Engine

Primary File:

```text
simulation.py
```

Responsibilities:

* Manage simulation lifecycle
* Execute simulation steps
* Coordinate agents
* Update environment state
* Track removals
* Manage hunter deployment

Outputs:

* Population State
* Removal Metrics
* Hotspots
* Hunter Status

---

## 3.2 Python Agents

Primary File:

```text
python_agent.py
```

Responsibilities:

* Movement
* Reproduction
* Mortality
* Habitat Selection

Agent Attributes:

* Position
* Life State
* Reproductive Capability

---

## 3.3 Environment Model

Primary File:

```text
environment.py
```

Responsibilities:

* Habitat Suitability
* Vegetation Layers
* Density Tracking
* Environmental Constraints

Environmental factors influence:

* Agent movement
* Detection probability
* Population growth

---

## 3.4 Hunter Teams

Primary File:

```text
hunter.py
```

Responsibilities:

* Target Pursuit
* Detection
* Removal Operations
* Suppression Activities

Hunter Metrics:

* Removals
* Position
* Target Assignment

---

## 3.5 Optimization Engine

Primary File:

```text
optimizer.py
```

Responsibilities:

* Hotspot Detection
* Priority Assignment
* Hunter Allocation
* Resource Optimization

Outputs:

* Active Hotspots
* Hunter Targets
* Suppression Priorities

---

# 4. GIS Intelligence

Primary File:

```text
gis.py
```

Technology:

```text
Folium
Leaflet
```

Responsibilities:

* Coordinate Conversion
* Hotspot Mapping
* Hunter Mapping
* Operational Visualization

Outputs:

* Interactive GIS Maps
* Spatial Intelligence Layers

Current Limitation:

* Tile rendering issue under certain local environments

---

# 5. Dashboard Architecture

Technology:

```text
Streamlit
```

Structure:

```text
dashboard/

├── app.py
├── simulation_manager.py
└── pages/
```

---

## Operations Center

Responsibilities:

* Execute simulation
* Monitor population
* Monitor hotspots
* Monitor removals
* Manage simulation controls

---

## Analytics Engine

Responsibilities:

* Population Trends
* Removal Trends
* Hotspot Trends
* Historical Analysis

Technology:

```text
Plotly
Pandas
```

---

## GIS Intelligence

Responsibilities:

* Embed GIS Maps
* Display Operational Geography

---

## Prediction Engine

Responsibilities:

* Forecast Population Growth
* Assess Risk
* Support Decision Making

---

# 6. Data Pipeline

```text
Simulation Step
        │
        ▼
State Collection
        │
        ▼
History Storage
        │
        ▼
Analytics Dataset
        │
        ▼
Prediction Dataset
        │
        ▼
Operational Intelligence
```

---

# 7. Prediction Architecture

Current Model:

```text
Linear Forecasting
```

Technology:

```text
NumPy
```

Forecast Horizons:

* 50 Steps
* 100 Steps
* 200 Steps

Outputs:

* Future Population
* Risk Assessment

Future Models:

* Scikit-Learn
* Random Forest
* Time Series Models

---

# 8. Operational Intelligence

Responsibilities:

* Risk Assessment
* Hunter Recommendations
* Suppression Evaluation
* Resource Planning

Current Outputs:

* Recommended Hunters
* Additional Hunters Required
* Suppression Effectiveness

---

# 9. Future Architecture

Version 2.0 Planned Enhancements:

## Advanced GIS

* Wetlands
* Waterways
* Roads
* Sector Management

## Advanced Forecasting

* Machine Learning Models
* Risk Forecasting
* Scenario Simulation

## Reinforcement Learning

* Autonomous Hunter Allocation
* Adaptive Suppression Policies

## Drone Surveillance

* Drone Agents
* Coverage Planning
* Aerial Detection

---

# 10. Architectural Summary

PPCIS has evolved from a standalone ecological simulation into a multi-layer Ecological Decision Support System integrating:

* Simulation
* Optimization
* GIS Intelligence
* Analytics
* Forecasting
* Operational Recommendations

The architecture is designed to support future expansion into machine learning, reinforcement learning, and advanced geospatial intelligence systems.
