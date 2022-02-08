import read_data as rd
from soynlp.tokenizer import MaxScoreTokenizer

data = rd.read_data('purchase_data_7Feb22')
scores = {}
for pair in data.values:
    scores[pair[1]] = 1.0
tokenizer = MaxScoreTokenizer(scores=scores)

def get_core(string):
    tokens = tokenizer.tokenize(string)
    for token in tokens:
        if token in scores:
            return token
    return "noun extractor"

