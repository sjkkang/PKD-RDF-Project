# API Usage and Examples

## Main Functions and Classes

### 1. Text Preprocessing

```python
from scripts.preprocess_text import TextPreprocessor

# Initialize preprocessor
preprocessor = TextPreprocessor()

# Process text
processed_text = preprocessor.process(raw_text)
entities = preprocessor.extract_entities(processed_text)
```

### 2. RDF Graph Construction

```python
from scripts.build_novel_rdf_fixed import RDFBuilder

# Initialize RDF builder
builder = RDFBuilder()

# Generate graph
graph = builder.build_graph(entities, relationships)
builder.save_graph(graph, "output.ttl")
```

### 3. SPARQL Queries

```python
from scripts.sparql_query import SPARQLAnalyzer

analyzer = SPARQLAnalyzer("graph.ttl")

# Query concepts by character
query = """
SELECT ?character ?concept WHERE {
    ?character novel:mentions ?concept .
}
"""
results = analyzer.execute_query(query)
```

## Usage Examples

### 1. Basic Analysis Pipeline

```python
# 1. Load data
data = load_processed_data("data/processed_novel.csv")

# 2. Build RDF graph
graph = build_rdf_graph(data)

# 3. Execute analysis
results = analyze_concepts(graph)

# 4. Save results
save_results(results, "results/analysis.csv")
```

### 2. Custom Analysis

```python
# Analyze concepts for specific character
character_concepts = analyze_character_concepts("Rick Deckard")

# Calculate concept similarity
similarity = calculate_concept_similarity("empathy", "authenticity")

# Network visualization
visualize_concept_network(graph, "network.png")
```

## Configuration Parameters

### Model Settings
```python
CONFIG = {
    "model_name": "sentence-transformers/all-MiniLM-L6-v2",
    "similarity_threshold": 0.7,
    "max_entities": 1000,
    "clustering_method": "hierarchical"
}
```

### RDF Namespaces
```python
NAMESPACES = {
    "novel": "http://example.org/novel#",
    "posthuman": "http://example.org/posthuman#",
    "character": "http://example.org/character#"
}
```
