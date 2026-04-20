"""
validate.py - Schema and integrity checks for deployments.csv
Author: Arldridge Margret Obuya
"""
import pandas as pd, sys

DATA_PATH = "data/deployments.csv"
REQUIRED = ['id','country','sector','deployer_type','ai_system_type','deployment_year',
            'deployment_status','affected_population','governance_docs_public',
            'impact_assessment_done','eu_ai_act_risk_class','nist_rmf_aligned','source_url']
VALID_STATUS = {'pilot','active','discontinued','unknown'}
VALID_RISK = {'minimal_risk','limited_risk','high_risk','unacceptable_risk','unknown'}

def validate(df):
    errors = []
    for f in REQUIRED:
        if f not in df.columns: errors.append(f"Missing column: {f}")
    if df['id'].duplicated().any(): errors.append(f"Duplicate IDs: {df[df['id'].duplicated()]['id'].tolist()}")
    bad_status = df[~df['deployment_status'].isin(VALID_STATUS)]
    if not bad_status.empty: errors.append(f"Invalid status values: {bad_status['deployment_status'].tolist()}")
    bad_risk = df[~df['eu_ai_act_risk_class'].isin(VALID_RISK)]
    if not bad_risk.empty: errors.append(f"Invalid risk class values: {bad_risk['eu_ai_act_risk_class'].tolist()}")
    return errors

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    errors = validate(df)
    if errors:
        print("Validation FAILED:")
        for e in errors: print(f"  - {e}")
        sys.exit(1)
    print(f"Validation PASSED. {len(df)} entries valid.")
