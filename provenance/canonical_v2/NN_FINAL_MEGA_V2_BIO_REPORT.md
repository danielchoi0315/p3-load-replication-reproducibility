# NN_FINAL_MEGA_V2_BIO REPORT

- Output root: `/project_runs/canonical_v2`
- Run status: `PASS_STRICT`
- Resume: `True`
- Start: `2026-02-23T07:13:53.737865+00:00`
- End: `2026-02-23T07:19:18.913080+00:00`

## Stage status
| Stage | Status | Return code | Runtime (s) | Log | Summary |
|---|---|---:|---:|---|---|
| preflight | PASS | 0 | 2.3 | preflight.log | preflight_summary.json |
| compile_gate | PASS | 0 | 2.0 | compile_gate.log | compile_gate_summary.json |
| stage_datasets | PASS | 0 | 36.3 | stage_datasets.log | stage_datasets_summary.json |
| decode_mapping_all | PASS | 0 | 0.8 | decode_mapping_all.log | decode_mapping_all_summary.json |
| extract_features_all | PASS | 0 | 8.0 | extract_features_all.log | extract_features_all_summary.json |
| core_lawc_ultradeep | PASS | 0 | 2386.0 | core_lawc_ultradeep.log | core_lawc_ultradeep_summary.json |
| mechanism_deep | PASS | 0 | 942.8 | mechanism_deep.log | mechanism_deep_summary.json |
| normative_lodo_manyseed | PASS | 0 | 3.6 | normative_lodo_manyseed.log | normative_lodo_manyseed_summary.json |
| clinical_translation | PASS | 0 | 321.2 | clinical_translation.log | clinical_translation_summary.json |
| bio_A_topography | PASS | 0 | 0.6 | bio_A_topography.log | bio_A_topography_summary.json |
| bio_B_source_template | SKIP | 0 | 0.0 | bio_B_source_template.log | bio_B_source_template_summary.json |
| bio_C_arousal_regime | PASS | 0 | 0.7 | bio_C_arousal_regime.log | bio_C_arousal_regime_summary.json |
| bio_D_cross_modality_ds004752 | SKIP | 0 | 0.4 | bio_D_cross_modality_ds004752.log | bio_D_cross_modality_ds004752_summary.json |
| objective_guard | PASS | 0 | 0.0 | objective_guard.log | objective_guard_summary.json |

## Dataset hashes/commits
| Dataset | Commit | Event files | EEG files | Status | Reason |
|---|---|---:|---:|---|---|
| ds003655 | 4807ef6e9930eddb6baa531be18118035f3e827c | 156 | 312 | PASS |  |
| ds004117 | 065e38865296e7707166eb3b1b561044ac62ab4c | 85 | 170 | PASS |  |
| ds005095 | 51de64a078faa54c5f62f1832e8afadb4137db57 | 48 | 96 | PASS |  |
| ds003838 | 2b2929557878cbd1278c7ef5281f6f875b74152a | 380 | 130 | PASS |  |
| ds004796 | null | 156 | 312 | PASS |  |
| ds004504 | 73b1b04c0a8e45e96c6f0682cc077a7919480fc4 | 0 | 176 | PASS |  |
| ds004584 | 261510fd9780d738a77fee52b906b3d56b69b74e | 149 | 20 | PASS |  |
| ds007020 | b063f0d23e466fa4dfd77b6e4afaf6fb4f672a9a | 94 | 188 | PASS |  |
| ds004752 | 234fd4c04dea66ab9b0fd5ddbf4ec51f56b6ad02 | 136 | 68 | PASS |  |
| ds004469 | a4d940040422f4b3411eccaa286640a817d627e8 | 63 | 0 | SKIP | dataset not ready after staging |
| ds007262 | 5544e0ff41c4f1de8a571530996ea81f13dee311 | 18 | 36 | PASS |  |

## Decode mapping
| Dataset | Status | Candidate | Reason |
|---|---|---|---|
| ds003655 | PASS | predefined_locked |  |
| ds003838 | PASS | predefined_locked |  |
| ds004117 | PASS | predefined_locked |  |
| ds004469 | SKIP |  | dataset not staged PASS (status=SKIP) |
| ds004752 | PASS | dataset_decoder |  |
| ds004796 | PASS | predefined_locked |  |
| ds005095 | PASS | predefined_locked |  |
| ds007262 | PASS | dataset_decoder |  |

## Feature extraction
| Dataset | Status | Method | HDF5 files | Trials | Reason |
|---|---|---|---:|---:|---|
| ds003655 | PASS | reuse_symlink | 156 | 16371 | nan |
| ds003838 | PASS | reuse_symlink | 64 | 35798 | nan |
| ds004117 | PASS | reuse_symlink | 84 | 1666 | nan |
| ds004469 | SKIP | nan | 0 | 0 | dataset staging status=SKIP |
| ds004752 | SKIP | nan | 0 | 0 | feature extraction failed rc_pre=1 rc_extract=1 workers_last=16 |
| ds004796 | PASS | reuse_symlink | 73 | 6462 | nan |
| ds005095 | PASS | reuse_symlink | 41 | 5587 | nan |
| ds007262 | SKIP | nan | 0 | 0 | feature extraction failed rc_pre=1 rc_extract=1 workers_last=16 |
| ds004504 | SKIP | resting_path | 0 | 0 | resting dataset handled in clinical_translation stage |
| ds004584 | SKIP | resting_path | 0 | 0 | resting dataset handled in clinical_translation stage |
| ds007020 | SKIP | resting_path | 0 | 0 | resting dataset handled in clinical_translation stage |

## Core Law-C locked results
| Dataset | Median rho | p | q | X-control degrade | Y-control degrade |
|---|---:|---:|---:|---|---|
| ds003655 | 0.019577353652482594 | 0.024509754902450977 | 0.02450975490245098 | True | True |
| ds004117 | 0.06275770686011468 | 0.02134978650213498 | 0.02450975490245098 | True | True |
| ds005095 | 0.05606227306722261 | 0.0004899951000489995 | 0.0014699853001469984 | True | True |

## Law-C random-effects meta
- `{"I2": 0.0, "Q": 0.06281854727340744, "k": 3, "mu_fixed": 0.03008618055107838, "mu_random": 0.03008618055107838, "tau2": 0.0}`

## Core effect sizes
| Dataset | N subjects | Slope median [CI95] | Delta median [CI95] |
|---|---:|---|---|
| ds003655 | 156 | 0.1581630044711346 [-0.058413206716068, 0.325271287238138] | 0.3092825781110451 [-0.1405059917418665, 0.5763770442658194] |
| ds004117 | 22 | 0.0884543851498165 [-0.2262917421655404, 0.495329459226923] | 0.2524545271374219 [-0.9699093083289272, 1.7332690364213477] |
| ds004796 | 65 | -0.0160318052166985 [-0.1048620097421348, 0.0330933147552059] | -0.0570572900476091 [-0.5201284478137889, 0.0909251677122357] |
| ds005095 | 41 | 0.0906521159372965 [-0.0224687634423996, 0.1772244407523734] | 0.6397315926589074 [-0.5277603725468389, 1.7075896707799103] |

## Mechanism results
| Metric | Observed median | p | q | Control pupil degrade | Control load degrade |
|---|---:|---:|---:|---|---|
| a | -0.0034931608870981 | 0.8074192580741926 | 0.9268073192680732 | True | True |
| b | -0.3206871233798361 | 9.999000099990002e-05 | 0.0002499750024997 | True | True |
| c_prime | 0.0059907531316919 | 0.9268073192680732 | 0.9268073192680732 | False | True |
| ab | 0.0495452280483915 | 9.999000099990002e-05 | 0.0002499750024997 | True | True |
| interaction | -0.0192960298705643 | 0.5440455954404559 | 0.9067426590674266 | True | True |

## Normative LODO
- `{"compile_ok": false, "compile_reason": "fallback-eager:Too few parameters for <class 'torch._inductor.codegen.common.CSE'>; actual 1, expected 2", "datasets_used": ["ds003655", "ds004117", "ds004796", "ds005095"], "gpu_stage_util": {"pre_util_gpu_mean": 0.0, "stage_util_gpu_mean": 12.75, "stage_util_gpu_median": 12.5, "util_rise_confirmed": true}, "n_folds": 4, "n_seeds_completed": 500, "n_seeds_requested": 500, "n_trials_total": 30086, "preload_gpu_tensors": true, "status": "PASS"}`

## Clinical endpoints
| Dataset | Endpoint | Feature | N | Estimate | Perm p | Perm q(global) |
|---|---|---|---:|---:|---:|---:|
| ds004504 | AUC_AD_vs_CN | dev_z_theta_alpha_ratio | 65 | 0.7260536398467432 | 0.0021498925053747 | 0.0229321867239971 |
| ds004504 | AUC_FTD_vs_CN | dev_z_theta_alpha_ratio | 52 | 0.7616191904047976 | 0.0010999450027498 | 0.0175991200439978 |
| ds004504 | AUC_AD_vs_FTD | dev_z_theta_alpha_ratio | 59 | 0.5060386473429952 | 0.9443027848607568 | 1.0 |
| ds004504 | MMSE_regression_beta | dev_z_theta_alpha_ratio | 88 | -0.3337605093431102 | 0.6182690865456727 | 1.0 |
| ds004504 | AUC_AD_vs_CN | dev_z_rel_alpha | 65 | 0.318007662835249 | 0.0115994200289985 | 0.0927953602319884 |
| ds004504 | AUC_FTD_vs_CN | dev_z_rel_alpha | 52 | 0.2233883058470764 | 0.0004999750012499 | 0.015999200039998 |
| ds004504 | AUC_AD_vs_FTD | dev_z_rel_alpha | 59 | 0.5797101449275363 | 0.3112844357782111 | 0.8300918287418962 |
| ds004504 | MMSE_regression_beta | dev_z_rel_alpha | 88 | 0.0542331388805883 | 0.935103244837758 | 1.0 |
| ds004504 | AUC_AD_vs_CN | dev_z_spectral_slope | 65 | 0.5038314176245211 | 0.9634518274086296 | 1.0 |
| ds004504 | AUC_FTD_vs_CN | dev_z_spectral_slope | 52 | 0.5172413793103448 | 0.8384580770961452 | 1.0 |
| ds004504 | AUC_AD_vs_FTD | dev_z_spectral_slope | 59 | 0.4456521739130435 | 0.4923753812309384 | 1.0 |
| ds004504 | MMSE_regression_beta | dev_z_spectral_slope | 88 | 0.2429264910347232 | 0.4684765761711914 | 1.0 |
| ds004504 | AUC_AD_vs_CN | composite_deviation | 65 | 0.5229885057471264 | 0.7595120243987801 | 1.0 |
| ds004504 | AUC_FTD_vs_CN | composite_deviation | 52 | 0.5742128935532234 | 0.3705814709264536 | 0.9122005438189628 |
| ds004504 | AUC_AD_vs_FTD | composite_deviation | 59 | 0.4565217391304347 | 0.5790710464476776 | 1.0 |
| ds004504 | MMSE_regression_beta | composite_deviation | 88 | 0.4868415467945883 | 0.6217189140542972 | 1.0 |
| ds004584 | AUC_PD_vs_CN | dev_z_theta_alpha_ratio | 40 | 0.4649999999999999 | 0.7106144692765362 | 1.0 |
| ds004584 | RobustBeta_PD_vs_CN | dev_z_theta_alpha_ratio | 40 | 0.069910089738871 | 0.8470576471176441 | 1.0 |
| ds004584 | AUC_PD_vs_CN | dev_z_rel_alpha | 40 | 0.65 | 0.1075446227688615 | 0.4433778311084446 |
| ds004584 | RobustBeta_PD_vs_CN | dev_z_rel_alpha | 40 | 1.005691116462845 | 0.2329383530823459 | 0.6776388453304608 |
| ds004584 | AUC_PD_vs_CN | dev_z_spectral_slope | 40 | 0.48 | 0.83970801459927 | 1.0 |
| ds004584 | RobustBeta_PD_vs_CN | dev_z_spectral_slope | 40 | -0.2699198263997678 | 0.552222388880556 | 1.0 |
| ds004584 | AUC_PD_vs_CN | composite_deviation | 40 | 0.6225 | 0.1908904554772261 | 0.6108494575271236 |
| ds004584 | RobustBeta_PD_vs_CN | composite_deviation | 40 | 0.3593889512478447 | 0.1563421828908554 | 0.5558833169452639 |
| ds007020 | AUC_mortality | dev_z_theta_alpha_ratio | 94 | 0.6546717171717171 | 0.0294485275736213 | 0.1884705764711764 |
| ds007020 | RobustBeta_mortality | dev_z_theta_alpha_ratio | 0 | nan | nan | 1.0 |
| ds007020 | AUC_mortality | dev_z_rel_alpha | 94 | 0.3869949494949494 | 0.1108444577771111 | 0.4433778311084446 |
| ds007020 | RobustBeta_mortality | dev_z_rel_alpha | 0 | nan | nan | 1.0 |
| ds007020 | AUC_mortality | dev_z_spectral_slope | 94 | 0.4943181818181817 | 0.9311534423278836 | 1.0 |
| ds007020 | RobustBeta_mortality | dev_z_spectral_slope | 0 | nan | nan | 1.0 |
| ds007020 | AUC_mortality | composite_deviation | 94 | 0.6376262626262627 | 0.0528973551322433 | 0.2821192273719647 |
| ds007020 | RobustBeta_mortality | composite_deviation | 0 | nan | nan | 1.0 |

## Objective Guard
- `{"command": "objective_guard", "elapsed_sec": 0.006784200668334961, "ended_at": "2026-02-23T07:19:18.893864+00:00", "error": "", "issues": [], "log": "/project_runs/canonical_v2/AUDIT/objective_guard.log", "outputs": ["/project_runs/canonical_v2/AUDIT/objective_guard_summary.json"], "returncode": 0, "stage": "objective_guard", "started_at": "2026-02-23T07:19:18.887080+00:00", "status": "PASS", "strict_pass": true, "summary": "/project_runs/canonical_v2/AUDIT/objective_guard_summary.json"}`

## GPU utilization summary
- NVML logger (`gpu_util.csv`): `{"mem_used_mb_mean": 40509.30077066626, "mem_used_mb_median": 41931.0, "power_w_mean": 121.87525092535473, "power_w_median": 121.608, "rows": 6484.0, "util_gpu_mean": 0.009716224552745218, "util_gpu_median": 0.0, "util_mem_mean": 0.01850709438618137, "util_mem_median": 0.0}`
- nvidia-smi 1Hz (`AUDIT/nvidia_smi_1hz.csv`): `{"mem_used_mb_mean": 40034.39972023081, "mem_used_mb_median": 40828.0, "power_w_mean": 121.59399895086553, "power_w_median": 121.61, "rows": 11438, "util_gpu_mean": 0.009966777408637873, "util_gpu_median": 0.0, "util_mem_mean": 0.010491344640671446, "util_mem_median": 0.0}`

## Partial reasons
- bio_B_source_template skipped: source localization skipped: available H5 features do not include channel-wise evoked waveforms required for fsaverage inverse modeling.
- bio_D_cross_modality_ds004752 skipped: insufficient convergent spectral signatures across eeg/ieeg runs

## Figure paths
- `/project_runs/canonical_v2/PACK_CORE_LAWC/effect_sizes/FIG_slopes_uv_per_load.png`
- `/project_runs/canonical_v2/PACK_CORE_LAWC/effect_sizes/FIG_delta_uv_high_vs_low.png`
- `/project_runs/canonical_v2/PACK_CORE_LAWC/effect_sizes/FIG_waveforms_by_load.png`
- `/project_runs/canonical_v2/PACK_MECHANISM/FIG_load_vs_pupil.png`
- `/project_runs/canonical_v2/PACK_MECHANISM/FIG_pupil_vs_p3_partial.png`
- `/project_runs/canonical_v2/PACK_MECHANISM/FIG_mediation_ab.png`
- `/project_runs/canonical_v2/PACK_MECHANISM/FIG_mechanism_summary.png`
- `/project_runs/canonical_v2/PACK_NORMATIVE/FIG_lodo_nll_by_fold.png`
- `/project_runs/canonical_v2/PACK_CLINICAL_PDREST/FIG_pdrest_calibration.png`
- `/project_runs/canonical_v2/PACK_CLINICAL_PDREST/FIG_pdrest_primary_auc_roc.png`
- `/project_runs/canonical_v2/PACK_CLINICAL_MORTALITY/FIG_mortality_calibration.png`
- `/project_runs/canonical_v2/PACK_CLINICAL_MORTALITY/FIG_mortality_primary_auc_roc.png`
- `/project_runs/canonical_v2/PACK_BIO/BIO_A_topography/FIG_topography_similarity.png`
- `/project_runs/canonical_v2/PACK_BIO/BIO_C_arousal_regime/FIG_regime_effect.png`

## Provenance
- Repo fingerprint: `/project_runs/canonical_v2/AUDIT/repo_fingerprint.json`
- Dataset hashes: `/project_runs/canonical_v2/AUDIT/dataset_hashes.json`
- GPU monitor (nvidia-smi): `/project_runs/canonical_v2/AUDIT/nvidia_smi_1hz.csv`
- GPU monitor (NVML): `/project_runs/canonical_v2/gpu_util.csv`
- Config default: `configs/default.yaml`
- Mega config: `configs/nn_final_mega_v2_bio.yaml`
- Datasets config: `configs/datasets_nn_final_mega_v2_bio.yaml`
- Final bundle: `/project_runs/canonical_v2/OUTZIP/NN_FINAL_MEGA_V2_BIO_SUBMISSION_PACKET.zip`
