import re

HGVS_C = re.compile(r"^c\.\d+([ACGT]>([ACGT])|(?:del|dup|ins).*)$")
HGVS_P = re.compile(r"^p\.[A-Z]\d+(?:[A-Z]|fs\*\d+)$")

def valid_hgvs(c, p):
    c_ok = bool(HGVS_C.match(c))
    p_ok = bool(HGVS_P.match(p))
    return c_ok and p_ok
