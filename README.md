# LLMeshMine: LLM-Based Data Mesh Framework for Inter-process Behavioral Analytics

## Project Background
LLMeshMine is a framework designed to enable inter-process behavioral analytics by leveraging Large Language Models (LLMs) and Data Mesh architectures. The project demonstrates how domain-based process analytics can be achieved through effective process-to-domain mapping, improving insights, resource allocation, and accuracy in complex environments such as healthcare systems.

---

## Use Cases
1. **Smart Healthcare**: Analyze and optimize workflows in organizations (e.g., hospitals).
2. **Behavioral Analytics**: Predict and improve user behaviors across interconnected systems.
3. **Data Governance**: Provide domain-specific insights using decentralized data management.
4. **Process Mining**: Facilitate inter-process analytics using data lakes transformed into data meshes.

---

# LLMeshMine Directory Structure

## Data
### knowledge/
- Domain-specific knowledge resources
- Contains merged.xml

### process/ 
- Sample process-related raw data
- Contains case_1.txt

### workflow/
- Workflow-related resources  
- Contains merged.docx

## Results
### datamesh/
- Output files related to data mesh generation
- Contains domains.csv

### entity_relationship/
- Extracted entity-relationship data
- Contains CSV and TXT files

### erd/
- Entity-Relationship Diagram outputs
- Contains erd.png

## Scripts
### domain.py
- Script for data domain identification

### entity_relationships.py
- Script to process entity relationships

### erd.py
- Script for generating entity-relationship diagrams

### graph_domain.py
- Script for domain graph construction

### process_mapping.py
- Script for process-to-domain mapping
