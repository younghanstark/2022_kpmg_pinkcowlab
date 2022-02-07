import read_data as rd
import string_processing as sp

data = rd.read_data('purchase_data_7Feb22')

num_data = len(data.values)
correct = 0
for pair in data.values:
    if sp.get_core(pair[0]) == pair[1]:
        correct += 1
print(correct/num_data*100, "% Accuracy!")