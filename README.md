# POLICY INSERT FUNCTIONS IN BKHERT CHATBOT

### Goal: 
Insert a new Policy Fifles in MS Word format, the system then split the policy into smaller passages and create new BM25 index

### Pipeline:
1. Document Processing
    - Remove Tables in MS Word file
    - Convert MS Word file to text file
    - Create Header for Passages
    - Crete Passages
    - Export Passages
2. Index Creation
    - Read Passages
    - Create new index

### Inserting new policy steps:
    - Add new file into data/policy/word folder
    - add policy Name and Role into role.json
    - run document_processing.py
    - run create_index.py

### Tesing
Beside, there is a "test.ipynb" file to test:
    - Passage length
    - Retrieval Function
