# Supplementary Software 1

This archive contains a reviewer-facing snapshot of the analysis code/provenance repository plus source-data CSV files for the submitted manuscript.

## Contents

- `analysis_pipeline/`: Python analysis pipeline and dataset/configuration files.
- `provenance/`: Frozen audit summaries and run-fingerprint files used to verify reported numerical results.
- `source_data/`: CSV files used to generate or audit the submitted display items.
- `support_scripts/assemble_main_figures.py`: Support script for assembling figure-level source data into display-ready inputs.
- `environment.yml`: Conda environment definition.
- `DATA_ACCESS.md`: Public OpenNeuro accessions, DOI snapshots, access date, and frozen commit references.
- `REPRODUCE.md`: Raw-data rerun and audit-comparison workflow.
- `LICENSE`: MIT license for the code snapshot.

## Scope

Raw OpenNeuro datasets and large intermediate processing outputs are not bundled here. The raw datasets are public and are identified in `DATA_ACCESS.md`. Manuscript PDFs, LaTeX source files, and rendered figure PDFs are provided as separate journal-submission files, not inside this software archive.

The matching public project repository is available at:

https://github.com/danielchoi0315/p3-load-replication-reproducibility

The journal package cites the version-specific Zenodo record that archives this software snapshot.

Internal code comments sometimes use the label `Law-C`; this denotes the locked confirmatory P3-load audit used for the manuscript, not a separate manuscript claim.
