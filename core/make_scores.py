from soynlp import DoublespaceLineCorpus
import read_data as rd
import pickle
from soynlp.word import WordExtractor
import os

path = os.path.dirname(os.path.realpath(__file__))

if os.path.exists(path+'/test_data/raw.txt'):
    os.remove(path+'/test_data/raw.txt')

file_list = ['purchase_data_12Feb22_1', 'purchase_data_12Feb22_2', 'purchase_data_13Feb22_1']
f = open(path+'/test_data/raw.txt', 'a', encoding='utf8')
for file_name in file_list:
    data_frame = rd.read_data(file_name)
    for pair in data_frame.values:
        f.write(pair[1]+' ')
f.close()

corpus = DoublespaceLineCorpus(path+'/test_data/raw.txt')
word_extractor = WordExtractor(min_frequency=1, remove_subwords=True)
word_extractor.train(corpus)
word_score_table = word_extractor.extract()

scores = {word:score.cohesion_forward for word,score in word_score_table.items()}

with open(path+'/scores_dict.pkl', 'wb') as f:
    pickle.dump(scores, f)
