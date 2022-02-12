import read_data as rd
import string_processing as sp

data = rd.read_data('purchase_data_12Feb22')

num_data = len(data.values)
correct = 0

for pair in data.values:
    tokenized = sp.get_core(pair[0])
    print(tokenized)
    print("For string", pair[0], "Expected", pair[1], "And got", tokenized[0][0])
    if pair[1] == tokenized[0][0]:
        correct += 1

print("%f percent accuracy!" % (correct/num_data*100))
