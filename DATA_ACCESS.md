# Data Access

This repository does not bundle raw OpenNeuro data. The paper used public OpenNeuro snapshots, and manuscript-facing exports are supplied with the journal submission bundle rather than tracked in this code repository.

For code-level audit, use the snapshot information below together with the summary files under `provenance/`.

If you want to rerun the analysis from raw data, stage the OpenNeuro snapshots listed below.

## Main Manuscript Datasets

These are the seven OpenNeuro datasets listed in Supplementary Table S7 and referenced by the final manuscript.

| Accession | Dataset title | Version / DOI | Access date | Frozen commit |
| --- | --- | --- | --- | --- |
| `ds003655` | VerbalWorkingMemory | `10.18112/openneuro.ds003655.v1.0.2` | `15 Mar 2026` | `4807ef6e9930eddb6baa531be18118035f3e827c` |
| `ds003838` | EEG, pupillometry, ECG and photoplethysmography, and digit span | `10.18112/openneuro.ds003838.v1.0.6` | `15 Mar 2026` | `2b2929557878cbd1278c7ef5281f6f875b74152a` |
| `ds004117` | EEG Sternberg Working Memory | `10.18112/openneuro.ds004117.v1.0.0` | `15 Mar 2026` | `065e38865296e7707166eb3b1b561044ac62ab4c` |
| `ds004504` | A dataset of EEG recordings from Alzheimer's disease, frontotemporal dementia and healthy subjects | `10.18112/openneuro.ds004504.v1.0.8` | `15 Mar 2026` | `73b1b04c0a8e45e96c6f0682cc077a7919480fc4` |
| `ds004584` | EEG Rest eyes open | `10.18112/openneuro.ds004584.v1.0.0` | `15 Mar 2026` | `261510fd9780d738a77fee52b906b3d56b69b74e` |
| `ds005095` | STERNBERG DIFFICULT | `10.18112/openneuro.ds005095.v1.0.0` | `15 Mar 2026` | `51de64a078faa54c5f62f1832e8afadb4137db57` |
| `ds007020` | EEG Mortality Dataset in Parkinson's Disease | `10.18112/openneuro.ds007020.v1.0.0` | `15 Mar 2026` | `b063f0d23e466fa4dfd77b6e4afaf6fb4f672a9a` |

## Optional Supplementary Exploratory Datasets

The broader audit code also references two public datasets used for optional supplementary exploratory outputs:

| Accession | Role in this repository | Frozen commit |
| --- | --- | --- |
| `ds004752` | Cross-modality exploratory audit | `234fd4c04dea66ab9b0fd5ddbf4ec51f56b6ad02` |
| `ds007262` | Workload exploratory audit | `5544e0ff41c4f1de8a571530996ea81f13dee311` |

These are not required for the central direct-replication rerun, but they are useful if you want to rerun the broader exploratory audit code.

## Staging Commands

The recommended public configs are:

- `analysis_pipeline/configs/datasets_paper_main.yaml`
  The seven manuscript datasets above.
- `analysis_pipeline/configs/datasets_paper_extended.yaml`
  The manuscript datasets plus the two optional supplementary exploratory datasets.

Example staging workflow:

```bash
cd analysis_pipeline

bash 00_stage_data.sh \
  --config configs/datasets_paper_main.yaml \
  --openneuro_root /project_data/openneuro \
  --manifest_out /project_runs/paper_main_staging_manifest.json
```

For the broader exploratory rerun:

```bash
cd analysis_pipeline

bash 00_stage_data.sh \
  --config configs/datasets_paper_extended.yaml \
  --openneuro_root /project_data/openneuro \
  --manifest_out /project_runs/paper_extended_staging_manifest.json
```

## Notes

- The frozen commit hashes above are taken from the manuscript bundle, dataset configs, and frozen provenance snapshots.
- The final paper does not require raw-data restaging if your goal is only to inspect the submitted figures and tables; those files are supplied with the journal submission bundle.
- The `ds004584` rest-stage in the frozen audit sometimes required explicit `datalad get` / `git annex get` repair of EEG files. That behavior is reflected in the included provenance notes.
