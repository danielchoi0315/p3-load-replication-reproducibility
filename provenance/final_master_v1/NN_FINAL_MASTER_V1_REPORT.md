# NN_FINAL_MASTER_V1 REPORT

- Output root: `/project_runs/final_master_v1`
- Canonical baseline reused: `/project_runs/canonical_v2`

## Stage status
| Stage | Status | Return code | Runtime (s) |
|---|---|---:|---:|
| preflight | PASS | 0 | 1.8 |
| compile_gate | PASS | 0 | 0.9 |
| stage_verify_ds004584_full | PASS | 0 | 392.8 |
| stage_verify_ds007020_full | PASS | 0 | 0.0 |
| clinical_ds004584_fullN_PDrest | PASS | 0 | 111.1 |
| clinical_ds007020_LEAPD_full | PASS | 0 | 147.0 |
| bio_ds004752_crossmodality_attempt | SKIP | 0 | 2.4 |

## ds004584 (PD vs CN)
- N_used: `123` (target>=140, hard minimum>=120)
- Exclusions: `/project_runs/final_master_v1/PACK_CLINICAL_PDREST_MASTER/EXCLUSIONS.csv`
- Primary endpoint (composite AUC): `{"ci95_hi": 0.5877926356589146, "ci95_lo": 0.3865768643345962, "covariates": "age;sex_num", "dataset_id": "ds004584", "endpoint": "AUC_PD_vs_CN", "estimate": 0.4892443463872035, "feature": "composite_deviation", "n": 123, "n_boot_done": 2000, "n_perm_done": 20000, "perm_p": 0.8383080845957702, "perm_q_within_ds004584": 0.9350032498375082, "type": "auc"}`

## ds007020 (Mortality LEAPD)
- N_used: `94`
- Finite beta count (baseline logistic): `5`
- LEAPD primary AUC (balanced LOOCV): `0.7871900826446281`
- LEAPD outputs: `/project_runs/final_master_v1/PACK_CLINICAL_MORTALITY_LEAPD/leapd_channel_results.csv`, `/project_runs/final_master_v1/PACK_CLINICAL_MORTALITY_LEAPD/leapd_truncation.csv`, `/project_runs/final_master_v1/PACK_CLINICAL_MORTALITY_LEAPD/leapd_out_of_sample.json`
- Baseline endpoint sample: `{"auc_flipped": 0.7222222222222222, "ci95_hi": 0.8540727654698244, "ci95_lo": 0.5681277056277056, "covariates": null, "dataset_id": "ds007020", "endpoint": "AUC_mortality", "estimate": 0.7222222222222222, "feature": "leapd_index_loocv", "model": "baseline_logit", "n": 94, "n_boot_done": 2000, "n_perm_done": 20000, "perm_p": 0.0015999200039998, "perm_q_within_ds007020": 0.015999200039998, "type": "auc"}`

## BIO / Workload attempts
- ds004752 status: `SKIP`
- ds007262 status: `PASS`
- ds004752 STOP (if skipped): `/project_runs/final_master_v1/PACK_BIO_CROSSMODALITY/BIO_D_cross_modality/STOP_REASON_ds004752.md`
- ds007262 STOP (if skipped): `/project_runs/final_master_v1/PACK_BIO_CROSSMODALITY/workload_ds007262/STOP_REASON_ds007262.md`

## Linkage to canonical
- Canonical packet: `/project_runs/canonical_v2/OUTZIP/NN_FINAL_MEGA_V2_BIO_SUBMISSION_PACKET.zip`

## Monitoring
- nvidia-smi summary: `{"mem_used_mb_mean": 40276.97747747748, "mem_used_mb_median": 40277.0, "power_w_mean": 74.8971921921922, "power_w_median": 74.905, "rows": 666, "util_gpu_mean": 0.0, "util_gpu_median": 0.0, "util_mem_mean": 0.0, "util_mem_median": 0.0}`
- NVML summary: `{"mem_used_mb_mean": 41379.29555120482, "mem_used_mb_median": 41379.312, "power_w_mean": 74.89727710843374, "power_w_median": 74.9045, "rows": 664.0, "util_gpu_mean": 0.0, "util_gpu_median": 0.0, "util_mem_mean": 0.0, "util_mem_median": 0.0}`
