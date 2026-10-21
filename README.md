<div align="center">

# 🌿 EcoGrid Qatar (`Q-Carbon API`)

**An open-source, developer-friendly REST API for hyper-local carbon and desalinated water footprint calculations calibrated specifically for Qatar and the GCC region.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0%2B-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/)

</div>

---

## 📌 Overview

Standard global carbon calculators rely on Western energy baselines and European/North American seasonal climates. They fail to reflect the environmental reality of the Arabian Gulf, particularly:
* **Extreme Seasonal HVAC Loads:** Summer air conditioning accounts for up to 60-70% of total household power consumption in Qatar.
* **Energy-Intensive Desalination:** Municipal water production relies heavily on thermal and Reverse Osmosis (RO) seawater desalination processes powered by the Kahramaa grid.
* **Local Fuel Dynamics:** Distinct regional transport and consumption profiles.

**EcoGrid Qatar** provides a lightweight, open-source backend microservice to power sustainability apps, academic research, and community eco-literacy initiatives aligned with **Qatar National Vision 2030** and climate advocacy frameworks.

---

## ✨ Key Features

- **GCC-Calibrated Calculations:** Uses region-specific grid emission factors ($0.512 \text{ kg CO}_2\text{e/kWh}$) and desalination impact ratios ($4.2 \text{ kg CO}_2\text{e/m}^3$).
- **HVAC Share Modeling:** Calculates seasonal AC isolation metrics to highlight power efficiency opportunities.
- **Production-Ready FastAPI:** Auto-generates interactive Swagger/OpenAPI documentation.
- **CI/CD Integrated:** Automated GitHub Actions pipeline ensuring code quality and test passes on every commit.

---

## ⚡ Quick Start

### Prerequisites
* Python 3.9+ installed on your system.
* `git` installed.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ecogrid-qatar.git](https://github.com/YOUR_USERNAME/ecogrid-qatar.git)
   cd ecogrid-qatar
