import sys
from soynlp.tokenizer import MaxScoreTokenizer

inputString = sys.argv[1]

scores = {'123': 0.9}
tokenizer = MaxScoreTokenizer(scores=scores)

print(tokenizer.tokenize(inputString, flatten=False))