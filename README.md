# AI Adoption Tracker — Critical Infrastructure (East Africa)

A structured, open-source dataset and analysis tool for tracking AI system deployments in critical infrastructure sectors across East Africa, with governance gap analysis against major international frameworks.

**Built by:** [Arldridge Margret Obuya](https://www.linkedin.com/in/maggy-obuya-a9a281210/)  
**Focus regions:** Kenya, Tanzania, Uganda, Ethiopia, Rwanda  
**Sectors covered:** Fisheries, Agriculture, Logistics & Supply Chain, Energy, Water

---

## Why this project exists

AI systems are being deployed in East Africa's critical infrastructure sectors — often by international NGOs, development finance institutions, and private companies — with limited transparency, no systematic tracking, and no alignment to international governance standards.

This project provides:
1. A **structured dataset** of known AI deployments in East African critical infrastructure
2. A **risk scoring methodology** adapted for low-income country institutional contexts
3. A **governance gap analysis** comparing deployments against the EU AI Act, NIST AI RMF, and OECD AI Principles
4. An **open contribution model** so researchers and practitioners can add entries
   
[View live dashboard](https://maggyobuya98-glitch.github.io/ai-infrastructure-tracker/dashboard.html)

This is a living research tool, not a finished product. Contributions are welcome.

---

## Repository structure

```
ai-infrastructure-tracker/
├── data/
│   ├── deployments.csv          # Main dataset of AI deployments
│   ├── risk_scores.csv          # Computed risk scores per deployment
│   └── framework_mapping.csv   # Governance framework gap analysis
├── scripts/
│   ├── score.py                 # Risk scoring script
│   ├── analyze.py               # Analysis and summary statistics
│   └── validate.py              # Data validation and schema checks
├── docs/
│   ├── methodology.md           # Risk scoring methodology
│   ├── data_schema.md           # Field definitions and schema
│   └── contributing.md          # How to contribute entries
├── README.md
└── requirements.txt
```

---

## Dataset schema

Each deployment entry in `deployments.csv` includes:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique deployment ID (e.g. `KE-FISH-001`) |
| `country` | string | ISO 3166-1 alpha-2 country code |
| `sector` | string | Critical infrastructure sector |
| `subsector` | string | Specific subsector (e.g. "inland fisheries") |
| `deployer_type` | string | `government`, `ngo`, `private`, `development_finance` |
| `ai_system_type` | string | Type of AI system (e.g. "demand forecasting", "image classification") |
| `deployment_year` | int | Year of deployment or pilot |
| `deployment_status` | string | `pilot`, `active`, `discontinued`, `unknown` |
| `affected_population` | int | Estimated number of people affected |
| `governance_docs_public` | bool | Whether governance documentation is publicly available |
| `impact_assessment_done` | bool | Whether any impact assessment was conducted |
| `local_oversight_body` | string | Name of oversight body, if any |
| `eu_ai_act_risk_class` | string | Estimated EU AI Act risk classification |
| `nist_rmf_aligned` | bool | Whether deployment follows NIST AI RMF |
| `source_url` | string | Primary source URL |
| `notes` | string | Additional context |

---

## Risk scoring methodology

Deployments are scored on a 0–100 risk index across five dimensions:

1. **Deployment scope** — scale of affected population
2. **Sector criticality** — essentialness of the infrastructure sector
3. **Governance transparency** — availability of public documentation and oversight
4. **Institutional capacity** — strength of local oversight mechanisms
5. **Framework alignment** — compliance with EU AI Act / NIST AI RMF

See `docs/methodology.md` for full details.

---

## Quick start

```bash
git clone https://github.com/margret-obuya/ai-infrastructure-tracker.git
cd ai-infrastructure-tracker
pip install -r requirements.txt

python scripts/analyze.py          # Summary statistics
python scripts/score.py            # Compute risk scores
python scripts/validate.py         # Validate dataset integrity
```

---

## Contributing

We welcome entries from researchers, journalists, practitioners, and community members. See `docs/contributing.md` for the contribution guide and data standards.

Priority sectors for new entries: **fisheries, smallholder agriculture, rural energy, water systems**.

---

## License

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
Code: [MIT](https://opensource.org/licenses/MIT)

---

## Citation

```
Obuya, A.M. (2025). AI Adoption Tracker — Critical Infrastructure (East Africa).
GitHub. https://github.com/margret-obuya/ai-infrastructure-tracker
```
