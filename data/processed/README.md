# Processed Data Directory

This directory contains preprocessed versions of the source materials after text cleaning and initial processing.

## Contents Structure

```
processed/
├── primary_text_cleaned.txt      # Cleaned novel text (not included)
├── criticism_excerpts/           # Processed academic texts (not included)
├── character_mentions.csv        # Character occurrence data
├── concept_extractions.csv       # Posthumanist concept instances
└── chapter_summaries.txt         # Chapter-wise analysis notes
```

## Processing Pipeline

1. **Text Cleaning**: Remove formatting, normalize encoding
2. **Sentence Segmentation**: Split into analyzable units
3. **Entity Recognition**: Extract characters, organizations, concepts
4. **Concept Mapping**: Identify posthumanist theoretical elements
5. **Data Validation**: Verify extraction accuracy

## File Descriptions

### character_mentions.csv
- Character appearance tracking
- Co-occurrence analysis data
- Dialogue attribution information

### concept_extractions.csv
- Posthumanist concept instances
- Context windows for each mention
- Confidence scores from classification model

### chapter_summaries.txt
- Thematic analysis by chapter
- Key concept distributions
- Character development notes

## Usage Instructions

1. Place legally obtained source texts in parent directory
2. Run `scripts/preprocess_text.py` to generate cleaned versions
3. Execute entity extraction pipeline
4. Verify results before analysis

## Data Privacy

All content must comply with copyright law and academic fair use policies.
