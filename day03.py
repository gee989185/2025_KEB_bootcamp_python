subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]
#subjects = ["데이터베이스", "C++", 5, "Java", "Python", "Java", "9", "리눅스"] # not support between instance of int and str
#print(subjects[::-1])
#subjects[::-1]
#subjects = subjects[::-1]  # subjects.reverse()
print(subjects)

# delete
#subjects.remove("Java")
#del subjects[-2]
#del subjects[2]
#print(subjects.pop(2)) # delete () after return ()

# arrange
subjects.sort(reverse=True)  # desc / modified origin value
subjects.sort(reverse=False) # ascd
copy_subjects = sorted(subjects) # not modified origin value
print(subjects)
#print(copy_subjects)