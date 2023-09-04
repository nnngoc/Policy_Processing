import string
import numpy as np
import re
import os
import py_vncorenlp

from gensim.corpora import Dictionary
from gensim.models import TfidfModel, OkapiBM25Model, LuceneBM25Model, AtireBM25Model
from gensim.similarities import SparseMatrixSimilarity

import constant
from vncorenlp import VnCoreNLP

# best_document = corpus[np.argmax(similarities)]

# CURRENT_DIR = os.getcwd()
# CURRENT_FOLDER_NAME = CURRENT_DIR.split('/')[-1]
# VNCORENLP_PATH = constant.VNCORENLP_PATH
# VNCORENLP_MODEL_PATH = constant.VNCORENLP_MODEL_PATH

class BM25Gensim:
    def __init__(self, data=None):
        if data:
            self.corpus = [text.split() for text in data]
        self.load_annotator()

    def load_annotator(self):
        if not os.path.exists(constant.VNCORENLP_PATH):
            os.makedirs(constant.VNCORENLP_PATH)
            py_vncorenlp.download_model(save_dir=constant.VNCORENLP_PATH)
        self.annotator = VnCoreNLP(constant.VNCORENLP_MODEL_PATH, annotators='wseg')

    def create_model(self, output_path, k=1.5, b=0.75):
        dictionary = Dictionary(self.corpus)
        bm25_model = AtireBM25Model(dictionary=dictionary, k1=k, b=b)
        bm25_corpus = bm25_model[list(map(dictionary.doc2bow, self.corpus))]
        bm25_index = SparseMatrixSimilarity(
            bm25_corpus,
            num_docs=len(self.corpus),
            num_terms=len(dictionary),
            normalize_queries=False,
            normalize_documents=False
            )
        tfidf_model = TfidfModel(dictionary=dictionary, smartirs='bnn')

        dictionary.save(output_path + "/dict")
        tfidf_model.save(output_path + "/tfidf")
        bm25_index.save(output_path + "/bm25_index")

    def load_model(self, checkpoint_path):
        self.dictionary = Dictionary.load(checkpoint_path + "/dict")
        self.tfidf_model = TfidfModel.load(checkpoint_path + "/tfidf")
        self.bm25_index = SparseMatrixSimilarity.load(checkpoint_path + "/bm25_index")

    def preprocess(self, text):
        exclude = set(string.punctuation)
        text = ' '.join(text.split())
        text = ''.join(ch for ch in text if ch not in exclude)
        text = text.lower()
        text = text.replace('\n', ' ')
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        text = ' '.join([' '.join(text) for text in self.annotator.tokenize(text)])
        return text

    def get_top_result(self, query, topk=10):
        query = self.preprocess(query)
        tokenized_query = query.split()
        tfidf_query = self.tfidf_model[self.dictionary.doc2bow(tokenized_query)]
        scores = self.bm25_index[tfidf_query]
        top_n = np.argsort(scores)[::-1][:topk]
        return top_n.tolist(), scores[top_n]
