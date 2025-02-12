import copy
#subjects = ["a", "b", "c"]         # immutable
subjects = ["a", ["b", "c"], "d"]   # include mutable(subjects[1,2])
a = subjects                        # reference
b = subjects.copy()                 # shallow copy
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)                # deep copy
print(subjects, a, b, c, d, e)
subjects[1][1] = "x"
print(subjects, a, b, c, d, e)