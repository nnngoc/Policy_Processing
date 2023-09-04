import json
import os
import string
import re
import pandas as pd
import numpy as np
import py_vncorenlp
from pprint import pprint
from nltk import word_tokenize as lib_tokenizer
from vncorenlp import VnCoreNLP
from tqdm import tqdm

import constant
from code.bm25 import BM25Gensim
from code.loader import Document_Loader


# =================================================================================
# 1. READ ROLES
# =================================================================================

with open(constant.ROLE_PATH, "r") as f:
    json_file = json.load(f)

metadata = {role:[x for x in json_file.keys() if role in json_file[x]] for role in constant.ROLE_LIST}

INDEX_PATHS = {key: constant.RETRIEVAL_INDEX_FOLDER + '/' + key for key in metadata.keys()}
PASSAGE_PATHS = {key: [constant.PASSAGE_FOLDER + '/' + y for y in metadata[key]] for key in metadata.keys()}

for index_path in INDEX_PATHS.values():
    if not os.path.exists(index_path):
        os.makedirs(index_path)

# =================================================================================
# 2. LOAD WORDSEGMENTATOR
# =================================================================================

if not os.path.exists(constant.VNCORENLP_PATH):
    os.makedirs(constant.VNCORENLP_PATH)
    py_vncorenlp.download_model(save_dir=constant.VNCORENLP_PATH)
    
annotator = VnCoreNLP(constant.VNCORENLP_MODEL_PATH, annotators='wseg')

# =================================================================================
# 3. UTILITIES FUNCTION
# =================================================================================

def strip_context(text):        
    text = text.lower()
    text = text.replace('\n', ' ') 
    text = re.sub(r'\s+', ' ', text) 
    text = text.strip() 
    return text

def post_process(x):
    x = " ".join(word_tokenize(strip_context(x))).strip()
    x = x.replace("\n"," ")
    x = "".join([i for i in x if i not in string.punctuation])
    x = ' '.join([' '.join(text) for text in annotator.tokenize(x)])
    return x

dict_map = dict({})  
def word_tokenize(text): 
    global dict_map 
    words = text.split() 
    words_norm = [] 
    for w in words: 
        if dict_map.get(w, None) is None: 
            dict_map[w] = ' '.join(lib_tokenizer(w)).replace('``', '"').replace("''", '"') 
        words_norm.append(dict_map[w]) 
    return words_norm 

# =================================================================================
# 4. CREATE NEW INDEX
# =================================================================================

def create_index(index_name):
    index_path = INDEX_PATHS[index_name]
    passage_path = PASSAGE_PATHS[index_name]
    
    document_loader = Document_Loader(passage_path)
    data = document_loader.context
    data = list(map(post_process, data))
    
    retriever = BM25Gensim(data)
    retriever.create_model(index_path, k=constant.RETRIEVER_K, b=constant.RETRIEVER_B)
    
list(map(create_index, tqdm([index_name for index_name in metadata.keys()])))