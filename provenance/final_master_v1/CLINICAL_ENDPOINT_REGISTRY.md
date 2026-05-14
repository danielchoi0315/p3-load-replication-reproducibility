# Clinical Endpoint Registry

- ds004584 primary: `composite_deviation` AUC PD vs CN
- ds007020 primary: LEAPD balanced LOOCV AUC (with out-of-sample summary)
- ds004504 primary: theta/alpha ratio AUCs (canonical V2_BIO)

## Correction scopes
- Within-dataset BH-FDR: ds004584 endpoints
- Within-dataset BH-FDR: ds007020 baseline endpoints
- Global BH-FDR (transparency): ds004504 + ds004584 + ds007020
