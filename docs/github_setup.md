# GitHub Repository Setup Guide

## Project Overview
This repository contains the code and analysis results for an AI-driven literary criticism study of Philip K. Dick's "Do Androids Dream of Electric Sheep?" using RDF technology and posthumanist theoretical frameworks.

## What's Included in This Repository

### ✅ Public Content
- **Analysis scripts** (`scripts/`) - All Python code for text processing, RDF construction, and analysis
- **Results data** (`results/`) - Generated CSV files, RDF graphs, and analysis outputs
- **Documentation** (`docs/`) - Detailed methodology and API documentation
- **Configuration files** - Requirements, gitignore, license
- **Processed data samples** - Anonymized and processed datasets

### ❌ Excluded Content (Copyright Protected)
- Original novel text (`primary_text.txt`)
- Academic paper excerpts (`c-*.txt` files)
- Research paper PDF
- Large trained model files

## Repository Structure
```
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md              # Main documentation
├── requirements.txt       # Python dependencies
├── docs/                  # Documentation
│   ├── methodology.md     # Research methodology
│   └── api_guide.md      # API usage guide
├── scripts/              # Analysis scripts
│   ├── preprocess_text.py
│   ├── build_novel_rdf_fixed.py
│   ├── analysis.py
│   └── ...
├── results/              # Analysis results
│   ├── *.ttl            # RDF graph files
│   ├── *.csv            # Analysis data
│   └── analysis_results/
└── data/                # Public data only
    ├── posthuman_glossary.txt
    ├── processed_novel.csv
    └── processed/
```

## Copyright Compliance

### What We Can Share
1. **Research code and methodology** - Original algorithms and analysis scripts
2. **Generated data** - RDF graphs, frequency counts, statistical results
3. **Derivative analysis** - Character networks, concept mappings, correlations
4. **Documentation** - Methodology explanations and usage guides

### What We Cannot Share
1. **Full text of copyrighted novel** - Protected by copyright law
2. **Academic paper excerpts** - Require permission from publishers
3. **Direct quotations** - Beyond fair use limits

## Academic Use and Citation

This repository is designed for:
- **Educational purposes** - Learning digital humanities methods
- **Research replication** - Applying methodology to other texts
- **Method development** - Building upon our analytical framework
- **Open science** - Transparent research practices

## Installation and Usage

1. **Clone the repository**
```bash
git clone [repository-url]
cd [repository-name]
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run analysis with your own data**
```bash
python scripts/analysis.py
```

## Reproducibility

While the original copyrighted texts are not included, researchers can:
1. Obtain legal copies of the source materials
2. Apply our preprocessing scripts to their texts
3. Use our RDF construction methodology
4. Reproduce the analytical framework

## Legal Notice

This repository complies with:
- **Fair use doctrine** for academic research
- **Copyright law** by excluding protected content
- **Open source principles** through MIT licensing
- **Academic integrity** standards

## Contact for Data Access

Researchers requiring access to the original processed datasets for legitimate academic purposes may contact the authors to discuss data sharing agreements that comply with copyright restrictions.

---

**Disclaimer**: This repository is for academic and educational use only. Commercial use requires separate licensing arrangements.
