# Conceptual Mapping and AI-Driven Literary Criticism: An RDF-Based Study

## Project Overview

This project presents an AI-driven literary criticism study of Philip K. Dick's novel "Do Androids Dream of Electric Sheep?" using RDF (Resource Description Framework). The study analyzes the work from a posthumanist perspective and visualizes semantic relationships within the text.

## Research Objectives

- Map relationships between posthumanist concepts and elements within the novel
- Provide structural analysis of literary works through RDF graphs
- Develop automated literary criticism tools using AI models
- Present digital humanities research methodologies

## Key Features

### 1. Text Preprocessing and Entity Recognition
- Text analysis using NLP technologies
- Extraction of characters, concepts, and themes
- Construction of posthumanist terminology dictionary

### 2. RDF Graph Construction
- Semantic relationship modeling of novels and critical literature
- Relationship analysis through SPARQL queries
- Generation of RDF data in Turtle format

### 3. AI-Based Analysis
- Concept analysis using Transformer models
- Similarity measurement through sentence embeddings
- Automated theme extraction

### 4. Visualization and Analysis
- Network graph visualization
- Statistical analysis results generation
- Character-concept correlation analysis

## Installation and Execution

### System Requirements
```bash
pip install -r requirements.txt
```

### Key Libraries
- **NLP**: spaCy, Transformers, NLTK
- **Data Analysis**: pandas, numpy, scipy
- **RDF Processing**: rdflib
- **Visualization**: matplotlib, networkx, seaborn
- **Machine Learning**: scikit-learn, torch

### Usage

1. **Text Preprocessing**
```bash
python scripts/preprocess_text.py
```

2. **RDF Graph Construction** (Final Versions)
```bash
# Build novel RDF graph
python scripts/build_novel_rdf_fixed.py

# Build criticism RDF graph  
python scripts/build_criticism_rdf_fixed.py
```

3. **Main Analysis Pipeline**
```bash
# Primary analysis script used in research
python scripts/analysis.py
```

4. **Character-Concept Analysis**
```bash
python scripts/character_concept.py
```

5. **Generate Specific Tables**
```bash
python scripts/generate_table2.py
python scripts/generate_table5.py
python scripts/analyze_table4.py
```

6. **SPARQL Queries**
```bash
python scripts/query_novel.py
```

7. **Visualization** (Optional)
```bash
python scripts/visualize_rdf.py
```

## Project Structure

```
├── scripts/                    # Analysis scripts
│   ├── preprocess_text.py     # Text preprocessing
│   ├── build_novel_rdf_fixed.py  # Novel RDF construction (FINAL)
│   ├── build_criticism_rdf_fixed.py  # Criticism RDF construction (FINAL)
│   ├── analysis.py            # Main analysis pipeline (PRIMARY)
│   ├── character_concept.py   # Character-concept analysis
│   ├── generate_table2.py     # Table 2 generation
│   ├── generate_table5.py     # Table 5 generation
│   ├── analyze_table4.py      # Table 4 analysis
│   ├── query_novel.py         # SPARQL query engine
│   ├── rdf_analysis.py        # RDF utilities
│   └── visualize_rdf.py       # Visualization tools
├── results/                   # Analysis results
│   ├── *_fixed.ttl           # Final RDF graph files
│   ├── *.csv                 # Analysis data tables
│   └── analysis_results/     # Detailed analysis results
├── data/                     # Data files (excluding original texts)
│   ├── posthuman_glossary.txt  # Posthumanist terminology dictionary
│   ├── processed_novel.csv    # Processed novel data
│   └── processed/            # Preprocessed data
├── docs/                     # Documentation
│   ├── methodology.md        # Research methodology
│   ├── api_guide.md         # API usage guide
│   └── scripts_analysis.md  # Script version analysis
└── requirements.txt          # Dependencies list
```

**Note**: Scripts with `_fixed` suffix represent the final, production versions used in the actual research. Other numbered versions (e.g., `_1.py`, `_2.py`) were development iterations and are excluded from the repository.

## Key Results

### 1. Concept Analysis
- Frequency analysis of posthumanist concepts
- Character-concept association mapping
- Theme-based clustering

### 2. Relationship Analysis
- Character interaction networks
- Semantic connections between concepts
- Co-occurrence analysis within text

### 3. RDF Graph
- Total of [X] triples generated
- [Y] unique concepts identified
- [Z] relationship types defined

## Research Methodology

### 1. Data Collection and Preprocessing
- Structural segmentation of novel text
- Collection of posthumanist academic literature
- Construction and validation of terminology dictionary

### 2. Entity Recognition and Relationship Extraction
- Named Entity Recognition (NER)
- Relationship extraction through dependency parsing
- Context-based concept classification

### 3. RDF Modeling
- Ontology design
- Triple generation rule definition
- Data consistency validation

### 4. Analysis and Evaluation
- Pattern discovery through SPARQL queries
- Statistical significance testing
- Comparative analysis with literary criticism theory

## Data Usage Guidelines

### Copyright Considerations
- Original novel text is not published due to copyright protection
- Academic papers and critical literature texts are not included
- Only research result data and analysis code are published

### Reproducibility
- Same methodology can be applied to other texts
- Code is designed to be generalizable
- Detailed parameter settings are documented

## Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

