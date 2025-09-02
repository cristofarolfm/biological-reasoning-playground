# Biological Reasoning Playground

Small, clean demos of how I approach **computational biology** problems:

- RNA-seq QC & PCA
- scRNA-seq UMAP (Scanpy)
- **Variant interpretation** (ACMG principles + HGVS notation, mock examples)
- **Protein language model** demo (toy embedding + similarity)
- **De novo scoring pipeline** skeleton (interfaces for docking/LM/ADMET)

> All examples are illustrative/toy; not for clinical use. No PHI/PII.

## How to run
```bash
conda env create -f environment.yml
conda activate bio-reasoning
jupyter lab
