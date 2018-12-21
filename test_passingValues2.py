def spam_0(eggs):
    eggs.append(1)  # passing be reference
    eggs = [2,3]

ham = [0]
spam_0(ham)
print(ham)


def spam_1(eggs):
    eggs.append(1)  # passing be reference
    eggs += [2, 3]


ham = [0]
spam_1(ham)
print(ham)


def spam_2(eggs):
    # eggs.append(1)  # passing be reference
    eggs += 2

ham = 0
spam_2(ham)
print(ham)