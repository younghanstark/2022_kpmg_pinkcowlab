import pickle
from soynlp.tokenizer import MaxScoreTokenizer
import os

path = os.path.dirname(os.path.realpath(__file__))

def get_core(string):
    try:
        with open(path + '/scores_dict.pkl', 'rb') as f:
            scores = pickle.load(f)
            tokenizer = MaxScoreTokenizer(scores=scores)
            tokens = tokenizer.tokenize(string, flatten=False)
            flat_tokens = [item for sublist in tokens for item in sublist]
            return sorted(flat_tokens, key=lambda x: x[3], reverse=True)
    except Exception as e:
        return e
