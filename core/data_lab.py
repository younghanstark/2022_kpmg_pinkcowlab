import read_data as rd
import string_processing as sp

data = rd.read_data('purchase_data_7Feb22')

num_data = len(data.values)
correct = 0
for pair in data.values:
    # print("From %s we got %s, intended %s" % (pair[0], sp.get_core(pair[0]), pair[1]))
    if sp.get_core(pair[0]) == pair[1]:
        # print("Correct")
        correct += 1
    else:
        print("From %s we got %s, intended %s" % (pair[0], sp.get_core(pair[0]), pair[1]))
        print("Not correct")
print("%f percent accuracy!" % (correct/num_data*100))
