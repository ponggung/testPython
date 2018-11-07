import numpy as np
x = list(np.random.rand(100))


# TEST 1, merge_sort
def merge(l, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = l[p:p + n1]
    right = l[q + 1:q + 1 + n2]

    i = 0
    j = 0
    k = p
    while k < r + 1:
        if i == n1:
            l[k] = right[j]
            j += 1
        elif j == n2:
            l[k] = left[i]
            i += 1
        elif left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1


def _merge_sort(l, p, r):
    if p < r:
        q = int((p + r) / 2)
        _merge_sort(l, p, q)
        _merge_sort(l, q + 1, r)
        merge(l, p, q, r)


def merge_sort(l):
    _merge_sort(l, 0, len(l) - 1)


# TEST 2
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)


# TEST 3
def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


def test1():
    merge_sort(x)


def test2():
    quicksort(x)


def test3():
    qsort(x)


if __name__ == '__main__':
    import timeit
    print(
        'merge_sort:',
        timeit.timeit(
            "test1()", setup="from __main__ import test1, x;", number=10000))
    print(
        'quicksort:',
        timeit.timeit(
            "test2()", setup="from __main__ import test2, x;", number=10000))
    print(
        'qsort:',
        timeit.timeit(
            "test3()", setup="from __main__ import test3, x;", number=10000))
