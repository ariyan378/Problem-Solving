test_str_1 = 'CampusX best for DS students.'
repl_dict_1 = {"best" : "is the best channel", "DS" : "Data-Science"}

word_1 = test_str_1.split()

result = []

for word in word_1:
    if word in repl_dict_1:
        result.append(repl_dict_1[word])
    else:
        result.append(word)
    output = ' '.join(result)

print(f"Output is ---{output}")