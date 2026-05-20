# Reproduce The Analysis

This repository is a code-focused reproducibility repository. It does not track manuscript source files, submitted PDFs, generated figures, or figure-rendering assets.

## Rerun From Raw Public Data

This is an advanced workflow rather than a one-click capsule.

Requirements:

- Linux is strongly recommended.
- Public OpenNeuro data staged under `/project_data/openneuro`.
- DataLad and `git-annex`.
- A CUDA-capable GPU is recommended for the mechanism and normative modules.
- Enough local storage for staged datasets, feature caches, and run outputs.

The exact public data registry is in `DATA_ACCESS.md`.

## Create The Environment

```bash
conda env create -f environment.yml
conda activate p3-load-boundary-map
```

## Stage The Datasets

For the main paper dataset set:

```bash
cd analysis_pipeline

bash 00_stage_data.sh \
  --config configs/datasets_paper_main.yaml \
  --openneuro_root /project_data/openneuro \
  --manifest_out /project_runs/paper_main_staging_manifest.json
```

For the broader exploratory audit:

```bash
cd analysis_pipeline

bash 00_stage_data.sh \
  --config configs/datasets_paper_extended.yaml \
  --openneuro_root /project_data/openneuro \
  --manifest_out /project_runs/paper_extended_staging_manifest.json
```

## Run The Canonical Audit Pass

```bash
cd analysis_pipeline

python scripts/nn_final_mega_v2_bio_runner.py \
  --out_root /project_runs/canonical_v2 \
  --data_root /project_data/openneuro \
  --datasets_config configs/datasets_paper_extended.yaml \
  --resume false
```

If you prefer the wrapper script:

```bash
cd analysis_pipeline

bash scripts/nn_final_mega_v2_bio_autorun_fixloop.sh \
  --out_root /project_runs/canonical_v2 \
  --data_root /project_data/openneuro \
  --datasets_config configs/datasets_paper_extended.yaml
```

## Run The Tightened Clinical Freeze

```bash
cd analysis_pipeline

python scripts/nn_final_master_v1_runner.py \
  --out_root /project_runs/final_master_v1 \
  --data_root /project_data/openneuro \
  --canonical_root /project_runs/canonical_v2 \
  --resume false
```

## Run The Post-Final Tightening Pass

```bash
cd analysis_pipeline

python scripts/postfinal_tighten_runner.py \
  --out_root /project_runs/postfinal_tighten \
  --data_root /project_data/openneuro \
  --canonical_root /project_runs/final_master_v1 \
  --resume false
```

## What To Compare

The code-facing audit sources included here are:

- `provenance/canonical_v2/*`
- `provenance/final_master_v1/*`

If your goal is to verify the submitted figures and tables directly, use the reviewer-facing submission bundle supplied through the journal system. This repository duplicates the source-data CSVs and support scripts, but it intentionally does not track manuscript source files, submitted PDFs, rendered figure PDFs, or table-source files.

## Practical Scope

- The raw-data rerun path is compute-heavy and may require manual repair of annexed files for some datasets, as reflected in the included provenance snapshots.
- The journal submission bundle is the authoritative source for submitted manuscript files, table-source files, rendered display items, and the exact reviewer-facing Supplementary Software zip.
