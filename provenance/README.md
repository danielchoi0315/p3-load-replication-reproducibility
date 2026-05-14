# Provenance Guide

This folder documents frozen run summaries and file fingerprints for the analysis code in this repository.

## Folders

- `canonical_v2/`
  Summary files from the broader canonical baseline run.
- `final_master_v1/`
  Summary files from the later tightened run used for the final clinical freeze.

## How To Read This

The Python code in `analysis_pipeline/` is the analysis codebase used to generate these runs.

The reports here are kept to preserve audit lineage and file fingerprints across the two frozen run generations. Submitted manuscript files, figures, and figure source-data CSVs are intentionally kept in the journal submission bundle rather than duplicated in this code repository.
