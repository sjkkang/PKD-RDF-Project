# 🔄 Research Workflow and Script Execution Order

## Complete Analysis Pipeline

### Phase 1: Data Preparation
```bash
# 1. Preprocess raw text data
python scripts/preprocess_text.py
```

### Phase 2: RDF Graph Construction
```bash
# 2. Build novel-based RDF graph (FINAL VERSION)
python scripts/build_novel_rdf_fixed.py

# 3. Build criticism literature RDF graph (FINAL VERSION)  
python scripts/build_criticism_rdf_fixed.py
```

### Phase 3: Primary Analysis
```bash
# 4. Execute main analysis pipeline (CORE SCRIPT)
python scripts/analysis.py
```

### Phase 4: Detailed Character Analysis
```bash
# 5. Character-concept relationship analysis
python scripts/character_concept.py

# 6. SPARQL queries for novel analysis
python scripts/query_novel.py
```

### Phase 5: Table Generation
```bash
# 7. Generate Table 2 results
python scripts/generate_table2.py

# 8. Generate Table 5 results
python scripts/generate_table5.py

# 9. Analyze Table 4 data
python scripts/analyze_table4.py
```

### Phase 6: Additional Analysis (Optional)
```bash
# 10. Additional RDF analysis utilities
python scripts/rdf_analysis.py

# 11. Visualization (if needed)
python scripts/visualize_rdf.py
```

---

## 📁 Generated Output Files

### After Phase 2 (RDF Construction):
- `results/novel_posthumanism_rdf_fixed.ttl` - Novel RDF graph
- `results/criticism_rdf_fixed.ttl` - Criticism RDF graph

### After Phase 3 (Primary Analysis):
- `results/concept_counts.csv` - Concept frequency analysis
- `results/concept_mentions_analysis.csv` - Mention analysis

### After Phase 4 (Character Analysis):  
- `results/character_theme_mapping.csv` - Character-theme relationships
- `results/character_analysis.csv` - Character analysis results
- `results/character_concept_analysis.csv` - Character-concept mapping

### After Phase 5 (Table Generation):
- `results/table2_results.csv` - Table 2 data
- `results/table5_results.csv` - Table 5 data  
- `results/analysis_table4.csv` - Table 4 analysis

---

## 🎯 Script Classifications

### **Core Production Scripts** (실제 연구에 사용)
✅ **Essential for replication:**
- `build_novel_rdf_fixed.py` - Final novel RDF builder
- `build_criticism_rdf_fixed.py` - Final criticism RDF builder
- `analysis.py` - Primary analysis engine
- `character_concept.py` - Character analysis
- `preprocess_text.py` - Text preprocessing

✅ **Table generation scripts:**
- `generate_table2.py`
- `generate_table5.py` 
- `analyze_table4.py`

✅ **Query and utilities:**
- `query_novel.py`
- `rdf_analysis.py`

### **Development Scripts** (개발 과정, 제외됨)
❌ **Excluded from GitHub:**
- `build_novel_rdf.py` (early version)
- `build_novel_rdf_1.py` (intermediate)
- `build_criticism_rdf.py` (early version)
- `rebuild_critic.py` (development test)

---

## 📊 Research Results Overview

| Analysis Phase | Primary Script | Output Files | Research Tables |
|----------------|---------------|--------------|-----------------|
| RDF Construction | `build_*_fixed.py` | `*_fixed.ttl` | Foundation |
| Concept Analysis | `analysis.py` | `concept_*.csv` | Tables 3, 4 |
| Character Study | `character_concept.py` | `character_*.csv` | Character analysis |
| Table Generation | `generate_table*.py` | `table*_results.csv` | Tables 2, 5 |
| Query Analysis | `query_novel.py` | SPARQL results | Supplementary |

---

## 🔍 Version Control Strategy

**Naming Convention Used:**
- `*_fixed.py` = Final, production-ready versions
- `*_1.py`, `*_2.py` = Development iterations (excluded)
- Base names = Either early versions or utilities

**File Selection Criteria:**
1. Latest modification dates (Feb 24-25, 2025)
2. `_fixed` suffix indicating final versions  
3. Referenced in `analysis.py` as dependencies
4. Generate outputs used in research paper

This ensures only the actual research scripts are included in the public repository, maintaining code quality and reproducibility.
