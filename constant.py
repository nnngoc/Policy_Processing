PYPANDOC_FOLDER_PATH = 'resource/pypandoc'
PYPANDOC_PATH = 'resource/pypandoc/pandoc'

# POLICY_WORD_FOLDER = "data/policy/word"
POLICY_WORD_FOLDER = "policy-data"
POLICY_PROCESSED_WORD_FOLDER = "data/policy/removed_table_words"
POLICY_INDEX_FOLDER = "data/policy/index"
POLICY_TEXT_FOLDER = "data/policy/text"

TITLE_FLAG = "quyết định số"

CHUONG_PATTERN_MULTIPLE_LINES = r"^((CHƯƠNG|Chương)\s([1-9][0-9]*|(IX|IV|V?I{1,3})))$"
PHULUC_PATTERN_MULTIPLE_LINES = r"^(Phụ\slục|PHỤ\sLỤC)\s([1-9][0-9]*|(IX|IV|V?I{1,3}))$"

CHUONG_PATTERN = r"^((CHƯƠNG|Chương)\s([1-9][0-9]*|(IX|IV|V?I{1,3})))"
PHULUC_PATTERN = r"^(Phụ\slục|PHỤ\sLỤC)\s([1-9][0-9]*|(IX|IV|V?I{1,3}))"

DIEU_PATTERN = r"^(Điều\s[1-9][0-9]*\.\s)"

PHU_LUC_SUB_SECTION_PATTERN = r"^[1-9][0-9]*\.\s"

PASSAGE_FOLDER = 'data/passage'

PASSAGE_LENGTH_LIMIT = 400

SUBSUB_SECTION_PATERN = r"[1-9][0-9]*\."

ROLE_PATH = "role.json"
ROLE_LIST = ["phd", "master", "undergraduate"]

RETRIEVAL_INDEX_FOLDER = "data/retrieval_index"
VNCORENLP_PATH = 'resource/vncorenlp/'
VNCORENLP_MODEL_PATH = 'resource/vncorenlp/VnCoreNLP-1.2.jar'

RETRIEVER_K = 2
RETRIEVER_B = 0.85