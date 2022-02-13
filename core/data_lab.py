from lib2to3.pgen2 import token
import read_data as rd
import string_processing as sp

file_list = ['purchase_data_12Feb22_1', 'purchase_data_12Feb22_2', 'purchase_data_13Feb22_1']
num_data = 0
correct = 0
for file_name in file_list:
    data = rd.read_data(file_name)
    num_data += len(data.values)

    for pair in data.values:
        tokenized = sp.get_core(pair[0])
        # print(tokenized)
        if pair[1] != tokenized[0][0]:
            print(tokenized)
            print("For string", pair[0], "Expected", pair[1], "And got", tokenized[0][0])
        if pair[1] == tokenized[0][0]:
            correct += 1

print("%f percent accuracy!" % (correct/num_data*100))
