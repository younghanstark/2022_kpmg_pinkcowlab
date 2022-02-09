import pickle
from soynlp.tokenizer import MaxScoreTokenizer

def get_core(string):
    try:
        with open('../core/scores_dict.pkl', 'rb') as f:
            scores = pickle.load(f)
            tokenizer = MaxScoreTokenizer(scores=scores)
            tokens = tokenizer.tokenize(string)
            for token in tokens:
                if token in scores:
                    return token
            return "Failed to get core"
    except Exception as e:
        return e
