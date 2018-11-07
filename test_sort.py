import random
import time
import sys
import timeit
import heapq


def runtime(func):
    '''測試執行時間'''
    def new_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost = round(end - start, 3)
        print("cost: {} sec".format(cost))

    return new_func


def create():
    ''' Create 1 million random numbers'''
    length = 1000000
    # length = 100
    nums = [random.randint(0, 99999999)
            for i in range(length)]  # 将序列nums中的元素顺序打乱

    with open("nums.txt", "w") as file:  # file size 8.5M
        stra = "\n".join([str(i) for i in nums])
        file.write(stra)
    return nums


@runtime
def use_heapq():
    '''最小堆排序算法'''
    import heapq
    with open('nums.txt', "r") as file:
        nums = map(int, file.readlines())
        print(heapq.nlargest(10, nums))  # 選出最大的十個
        # print (heapq.nsmallest(10, nums)) # 選出最小的十個


@runtime
def use_sort(nums):
    '''內建的sort 使用 timsort '''
    nums.sort()
    print(nums[-10:][::-1])  # 選出最大的十個
    return nums

if __name__ == "__main__":
    nums = create()
    use_sort(nums)
    use_heapq()
