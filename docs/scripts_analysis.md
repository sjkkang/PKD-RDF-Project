# 🎯 Actual Scripts Used in Research

## Core Analysis Pipeline Scripts (Final Versions)

### 📊 **Primary Analysis Scripts** (최종 실험 코드)

#### 1. **RDF Graph Construction** 
- `build_novel_rdf_fixed.py` ✅ (Feb 24, 2025)
  - **Final version** for novel RDF construction
  - Uses AI models for concept extraction
  - Generates `novel_posthumanism_rdf_fixed.ttl`

- `build_criticism_rdf_fixed.py` ✅ (Feb 24, 2025)
  - **Final version** for criticism literature RDF
  - Processes academic literature
  - Generates `criticism_rdf_fixed.ttl`

#### 2. **Main Analysis Engine**
- `analysis.py` ✅ (Feb 24, 2025)
  - **Primary analysis script** used in research
  - Loads both RDF graphs
  - Generates concept counts and statistics
  - Produces final results for tables

#### 3. **Character-Concept Analysis**
- `character_concept.py` ✅ (Feb 25, 2025)
  - **Latest version** for character analysis
  - Generates character-concept relationship tables

#### 4. **Specific Table Generation**
- `generate_table2.py` ✅ (Feb 24, 2025)
  - Generates Table 2 results
  
- `generate_table5.py` ✅ (Feb 24, 2025)
  - Generates Table 5 results

- `analyze_table4.py` ✅ (Feb 24, 2025)
  - Specific analysis for Table 4

#### 5. **Query and Analysis**
- `query_novel.py` ✅ (Feb 25, 2025)
  - **Latest version** for SPARQL queries
  - Novel-specific analysis

---

## 🗂️ Development/Experimental Scripts (개발 과정)

### **Iterative Development Files** (실험 중 폐기된 버전들)
- `build_novel_rdf.py` ❌ (Feb 3, 2025) - **Early version**
- `build_novel_rdf_1.py` ❌ (Feb 24, 2025) - **Intermediate version** 
- `build_criticism_rdf.py` ❌ (Feb 2, 2025) - **Early version**
- `rebuild_critic.py` ❌ (Feb 2, 2025) - **Development version**

### **Utility Scripts** (보조 도구들)
- `preprocess_text.py` ✅ (Sep 8, 2025) - Text preprocessing
- `rdf_analysis.py` ✅ (Feb 24, 2025) - Additional RDF utilities
- `update_rdf_ttl.py` ✅ (Feb 24, 2025) - RDF updating utilities
- `visualize_rdf.py` ⚠️ (Feb 2, 2025) - Visualization (earlier version)

### **Model Training Scripts**
- `train_posthuman_glossary.py` ⚠️ (Feb 2, 2025) - Model training
- `test_trained_model.py` ⚠️ (Feb 2, 2025) - Model testing
- `generate_negative_samples.py` ⚠️ (Feb 2, 2025) - Training data prep

---

## 📈 Final Results Files

### **Generated Output Files** (실제 연구 결과)
- `novel_posthumanism_rdf_fixed.ttl` ✅ - Final novel RDF
- `criticism_rdf_fixed.ttl` ✅ - Final criticism RDF
- `character_theme_mapping.csv` ✅ - Character analysis results
- `concept_counts.csv` ✅ - Concept frequency analysis
- `table5_like_output.csv` ✅ - Table 5 formatted results

---

## 🎯 Recommended Scripts for GitHub

### **Essential Scripts** (반드시 포함)
1. `build_novel_rdf_fixed.py` - Core RDF construction
2. `build_criticism_rdf_fixed.py` - Criticism RDF construction  
3. `analysis.py` - Main analysis pipeline
4. `character_concept.py` - Character analysis
5. `preprocess_text.py` - Text preprocessing

### **Analysis Scripts** (분석 관련)
6. `generate_table2.py` - Table generation
7. `generate_table5.py` - Table generation
8. `analyze_table4.py` - Specific analysis
9. `query_novel.py` - SPARQL queries
10. `rdf_analysis.py` - RDF utilities

### **Support Scripts** (보조 도구)
11. `update_rdf_ttl.py` - RDF management
12. `visualize_rdf.py` - Visualization (if updated)

---

## 🚫 Exclude from GitHub

### **Deprecated/Development Versions**
- `build_novel_rdf.py` (old version)
- `build_novel_rdf_1.py` (intermediate)
- `build_criticism_rdf.py` (old version)
- `rebuild_critic.py` (development)
- `python analysis.py` (duplicate/test file)

### **Model Training Scripts** (if models not included)
- `train_posthuman_glossary.py`
- `test_trained_model.py` 
- `generate_negative_samples.py`

---

## 📋 File Naming Convention Analysis

**Pattern Identified:**
- `*_fixed.py` = **Final, working versions**
- `*_1.py`, `*_2.py` = **Iterative development versions**
- Plain names without numbers = **Either early versions or utilities**
- Latest modification dates (Feb 24-25) = **Most recent, final versions**

**Recommendation:** Use `_fixed` versions and latest-dated files for the GitHub repository.
