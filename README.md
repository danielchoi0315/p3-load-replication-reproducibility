# P3 Load Replication and Generalization Code Repository

This repository contains the analysis code and audit lineage for the paper on the bounded P3-load effect in Sternberg-family working memory. Manuscript source files, submitted PDFs, generated figures, and journal-specific submission materials are not tracked here.

## Public Reproducibility Files

- `DATA_ACCESS.md`
  Exact OpenNeuro accessions, DOI snapshots, access date, and pinned commits used by the public paper configs.
- `REPRODUCE.md`
  Supported raw-data rerun and audit-comparison workflow.
- `environment.yml`
  Conda environment for the public analysis stack.
- `source_data/`
  Figure source-data CSV files used to generate or audit the submitted display items.
- `support_scripts/`
  Small support scripts for assembling source-data files into display-ready inputs.

## Repository Layout

- `analysis_pipeline/`
  Python pipeline for staging data, preprocessing EEG, extracting features, running mechanism and normative models, and assembling audit outputs.
- `provenance/`
  Frozen audit summaries and file fingerprints linking the reported results to the run lineage.
- `source_data/`
  Submitted figure source-data CSV files.
- `support_scripts/`
  Reviewer-facing support scripts that do not require raw EEG data.

## Running The Analysis

The analysis code defaults to generic project paths rather than private machine paths:

- `PROJECT_ROOT=/project_root/analysis_pipeline`
- `DATA_ROOT=/project_data/openneuro`
- `CLINICAL_BIDS_ROOT=/project_data/clinical_bids`
- `FEATURES_ROOT=/project_cache/features`
- `OUT_ROOT=/project_runs/<timestamp>`
- `LOG_ROOT=/project_logs`

The recommended paper-level dataset configs are:

- `analysis_pipeline/configs/datasets_paper_main.yaml`
- `analysis_pipeline/configs/datasets_paper_extended.yaml`

See `REPRODUCE.md` for the raw-data staging and rerun workflow.

## Provenance

Two frozen audit snapshots are included:

- `provenance/canonical_v2/`
  Broader canonical run used as the earlier baseline.
- `provenance/final_master_v1/`
  Later tightened run used for the final clinical freeze and final audit summaries.

For reported numerical summaries, compare regenerated outputs against the audit files under `provenance/` and the figure source-data files under `source_data/`.

## Not Included

- Raw OpenNeuro dataset payloads
- Large intermediate run trees and scratch outputs
- Manuscript source files, submitted PDFs, rendered figure PDFs, and figure-rendering assets
- Temporary submission-staging material
- Embedded git state from the original working copy
