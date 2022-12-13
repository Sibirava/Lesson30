first = [1, 54, 48454, 4588, 1, 9214654, 44, 99, 344, 54, 69]
second = [1, 0, 6, 4, 8, 9, 0, 0, 1]


for i in range(len(first)):
    try:
        print(f"{first[i]}/ {second[i]} = {first[i]/second[i]}")
    except Exception as exc:
        print(repr(exc))

#механизм работы exception продолжить работу что бы не случилось