from dataclasses import dataclass

@dataclass
class Evidence:
    code: str
    strength: str
    note: str

BENIGN_FREQ_THRESHOLD = 0.01  # toy threshold for demo only

def frequency_evidence(allele_freq: float):
    if allele_freq >= BENIGN_FREQ_THRESHOLD:
        return Evidence("BA1", "stand-alone", f"AF={allele_freq} ≥ {BENIGN_FREQ_THRESHOLD}")
    return None

def impact_evidence(impact: str):
    if impact.lower() in {"frameshift","stop_gained","splice_acceptor","splice_donor"}:
        return Evidence("PVS1","very-strong","Predicted LoF variant")
    return None

def literature_evidence(pmids: str):
    if pmids and len(pmids.split(";")) >= 2:
        return Evidence("PS4","strong","Multiple studies reporting association")
    return None

def classify(acmg_evidence):
    codes = {e.code for e in acmg_evidence if e}
    if "BA1" in codes:
        return "Benign/Likely Benign"
    if "PVS1" in codes or "PS4" in codes:
        return "Pathogenic/Likely Pathogenic"
    return "VUS"
