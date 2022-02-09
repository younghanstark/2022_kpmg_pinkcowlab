import read_data as rd
import pickle

file_list = ['purchase_data_7Feb22']
scores = {}

for file_name in file_list:
    data_frame = rd.read_data(file_name)
    for pair in data_frame.values:
        scores[pair[1]] = 1.0

with open('./core/scores_dict.pkl', 'wb') as f:
    pickle.dump(scores, f)
