# Associations Project ANLP 2025

This repository contains utilities and notebooks to **clean**, **standardize**, and **analyze** free‑association datasets (e.g., SWOW and LLM‑generated FA data), plus simple training/evaluation notebooks for downstream modeling.

---

## Repo Contents

### 1) `FA_data_Cleaning.py`
End‑to‑end **data cleaning pipeline** used to process human SWOW data and multiple LLM free‑association (FA) datasets into clean, aligned CSVs and a summary table.
This script was downloaded from the LWOW repo: https://github.com/LLMWorldOfWords/LWOW

---

### 2) `second_preprocessing.py`
A lightweight, task‑focused preprocessor for SWOW CSVs with columns `cue`, `R1`, `R2`, `R3`. It cleans, filters, and downsamples to exactly 80 rows per cue, then writes the result to an Excel file.

---

### 3) `ANLP_training.ipynb`
A **training notebook** (Jupyter) that demonstrates how to train a model using the cleaned FA datasets.

---

### 4) `ANLP_metrics.ipynb`
An **evaluation/metrics notebook** (Jupyter) for analyzing model outputs.*

---

### 5) `ANLP_benchmarks.ipynb`


---
