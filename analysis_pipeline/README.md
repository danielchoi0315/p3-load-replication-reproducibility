# P3 Load Analysis Pipeline

This directory contains the full Python pipeline used to stage datasets, preprocess EEG, extract features, run the mechanism and normative modules, and assemble audit outputs for the paper.

## Main Entry Points

- `00_stage_data.py` and `00_stage_data.sh`
  Stage pinned OpenNeuro snapshots with strict BIDS validation.
- `01_preprocess_CPU.py`
  Preprocess EEG and build derivatives.
- `02_extract_features_CPU.py`
  Extract locked ERP and behavioural features.
- `03_bayesian_mechanism_GPU.py`
  Run the pupil-linked mechanism module.
- `04_normative_clinical_GPU.py`
  Run normative and clinical deviation models.
- `05_audit_lawc.py`
  Assemble Law-C audit summaries.
- `aggregate_results.py`
  Combine seeded outputs into run-level summaries.

## Default Project Paths

The public copy uses generic placeholder paths that can be overridden from the CLI:

- `PROJECT_ROOT=/project_root/analysis_pipeline`
- `DATA_ROOT=/project_data/openneuro`
- `CLINICAL_BIDS_ROOT=/project_data/clinical_bids`
- `FEATURES_ROOT=/project_cache/features`
- `OUT_ROOT=/project_runs/<timestamp>`
- `LOG_ROOT=/project_logs`

## Setup

```bash
cd /project_root/analysis_pipeline

python -m venv .venv
source .venv/bin/activate

sudo apt-get update
sudo apt-get install -y datalad git-annex

pip install -r requirements.txt
```

## Stage Data

Pinned datasets and commit hashes are listed in `configs/datasets.yaml`.

```bash
cd /project_root/analysis_pipeline
source .venv/bin/activate

bash 00_stage_data.sh \
  --config configs/datasets.yaml \
  --openneuro_root /project_data/openneuro \
  --manifest_out /project_runs/staging_manifest.json
```

## Run The Main Pipeline

```bash
cd /project_root/analysis_pipeline
source .venv/bin/activate

bash scripts/run_all.sh \
  --data_root /project_data/openneuro \
  --features_root /project_cache/features \
  --log_root /project_logs \
  --clinical_bids_root /project_data/clinical_bids \
  --config configs/default.yaml \
  --datasets_config configs/datasets.yaml \
  --seeds "0,1,2,3,4"
```

Optional severity table for clinical regression:

```bash
bash scripts/run_all.sh \
  --severity_csv /project_data/clinical_bids/clinical_severity.csv
```

## Resumability

The pipeline is designed to resume safely:

- Data staging resumes partial downloads.
- Preprocessing and feature extraction skip completed outputs.
- Seeded GPU modules reuse checkpoints and completed seeds.

Useful flags:

```bash
bash scripts/run_all.sh --no-resume
bash scripts/run_all.sh --skip_stage
```

## Outputs

Each run under `OUT_ROOT` writes:

- `derivatives/`
- `aggregate_results.json`
- `AUDIT_SUMMARY.md`
- `gpu_util.csv`

Seeded modules also write seed-specific reports under their run directories.

## Additional Runners

Several dataset-specific runners are included under `scripts/` for the canonical, clinical, and tightening passes used during the paper audit. Those scripts now default to the same generic project-path scheme described above.
