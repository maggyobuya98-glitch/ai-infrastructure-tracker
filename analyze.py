"""
analyze.py - Summary statistics and governance gap analysis
AI Adoption Tracker: Critical Infrastructure (East Africa)
Author: Arldridge Margret Obuya
"""
import pandas as pd
from tabulate import tabulate

DATA_PATH = "data/deployments.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def summary_stats(df):
    print("\n=== Dataset Overview ===")
    print(f"Total deployments tracked: {len(df)}")
    print(f"Countries covered: {df['country'].nunique()} ({', '.join(sorted(df['country'].unique()))})")
    print(f"Total estimated affected population: {df['affected_population'].sum():,}")

def governance_gap_analysis(df):
    print("\n=== Governance Gap Analysis ===")
    gaps = {
        "No public governance documentation": len(df[df['governance_docs_public'] == False]),
        "No impact assessment conducted": len(df[df['impact_assessment_done'] == False]),
        "No local oversight body": len(df[df['local_oversight_body'].isna() | (df['local_oversight_body'] == '')]),
        "Not NIST AI RMF aligned": len(df[df['nist_rmf_aligned'] == False]),
    }
    for gap, count in gaps.items():
        pct = round(count / len(df) * 100)
        print(f"  {gap}: {count}/{len(df)} ({pct}%)")

def risk_breakdown(df):
    print("\n=== EU AI Act Risk Classification ===")
    for risk_class, count in df['eu_ai_act_risk_class'].value_counts().items():
        print(f"  {risk_class}: {count} deployment(s)")

def sector_table(df):
    print("\n=== By Sector ===")
    sector_summary = df.groupby('sector').agg(
        deployments=('id', 'count'),
        affected_population=('affected_population', 'sum'),
        governance_docs=('governance_docs_public', 'sum')
    ).reset_index()
    sector_summary['gov_pct'] = (sector_summary['governance_docs'] / sector_summary['deployments'] * 100).round(0).astype(int).astype(str) + '%'
    print(tabulate(sector_summary[['sector','deployments','affected_population','gov_pct']],
                   headers=['Sector','Deployments','Affected pop.','Has gov docs'], tablefmt='simple', showindex=False))

if __name__ == "__main__":
    df = load_data()
    summary_stats(df)
    governance_gap_analysis(df)
    risk_breakdown(df)
    sector_table(df)
