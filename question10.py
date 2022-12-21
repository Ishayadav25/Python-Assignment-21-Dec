sample_list = [87,45,41,65,94,41,99,94]
sample_list = list(set(sample_list))
print("unique items", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Min: ", min(t))
print("Max: ", max(t))