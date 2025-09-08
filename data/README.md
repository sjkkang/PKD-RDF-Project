# Data Directory

This directory contains the research data structure and sample files. Due to copyright restrictions, original source materials are not included in this public repository.

## Directory Structure

```
data/
├── README.md                           # This file
├── sample_posthuman_glossary.txt       # Sample glossary format (152 terms)
├── sample_processed_novel.csv          # Sample processed text format  
├── sample_processed_entities.csv       # Sample entity extraction format
├── glossary_terms/                     # Individual term files (152 files)
│   └── README.md                       # Term structure documentation
├── glossary_terms_negative/            # Negative samples (151 files)
│   └── README.md                       # Negative sample documentation
└── processed/                          # Preprocessed data files
    └── README.md                       # Processing pipeline documentation
```

## Original Data (Not Included)

### Primary Sources
- `primary_text.txt` - Philip K. Dick's novel (copyright protected)
- `c-*.txt` - Academic paper excerpts (17 files, copyright protected)
- `posthuman_glossary.txt` - Complete terminology dictionary

### Processed Files  
- `processed_novel.csv` - Sentence-level novel analysis
- `processed_novel_entities.csv` - Extracted named entities

## Research Data Statistics

- **Posthumanist Terms**: 152 concepts from academic literature
- **Negative Samples**: 151 non-posthumanist text samples
- **Novel Sentences**: ~[X] processed sentences across 22 chapters
- **Character Entities**: ~[Y] unique character mentions
- **Concept Instances**: ~[Z] posthumanist concept occurrences

## Data Acquisition Guidelines

To reproduce this research legally:

1. **Novel Text**: Obtain legal copy of "Do Androids Dream of Electric Sheep?"
2. **Academic Literature**: Access through institutional subscriptions or fair use
3. **Glossary**: Compile from public domain or permissioned sources
4. **Processing**: Use provided scripts to generate analysis-ready data

## Technical Requirements

### File Formats
- Text files: UTF-8 encoding
- CSV files: Comma-separated, quoted strings
- JSON: Structured entity and concept data

### Processing Pipeline
1. Text cleaning and normalization
2. Sentence segmentation and tokenization  
3. Named entity recognition (spaCy)
4. Concept classification (fine-tuned BERT)
5. RDF graph construction

## Copyright Compliance

This research framework:
- ✅ Provides methodology and code
- ✅ Documents data structure and format
- ✅ Enables reproducible research
- ❌ Does not include copyrighted source materials
- ❌ Requires users to obtain texts legally

## Citation and Attribution

When using this framework, please cite:
- Original research methodology
- Academic sources for posthumanist theory
- Technical tools and libraries used
- Fair use compliance for text analysis

For questions about data acquisition or processing, refer to the documentation in each subdirectory.
