'''
典型的參數傳遞方式有二種：

Pass-by-value: 複製參數的值傳入，所以原參數內容不會被影響。
Pass-by-reference: 傳入參數的參考，會影響原參數內容。

還有少數程式語言使用以下兩種傳遞方式：
Pass-by-name: 將傳入的參數視為變數名稱或是字串，概念類似 string evaluation。
Pass-by-value-result: 又稱 copy-in, copy-out，不直接傳入變數的參照，反而是將其複製一份傳入參照，最後再把結果指派回原先的變數。

-------------
Python 的參數傳遞方式兩種都不是
簡單來說，Python 的參數傳遞方式你必須注意：

Immutable Object 參數傳遞行為同 pass-by-value。
Mutable Object 參數傳遞行為同 pass-by-reference，但是不允許 re-assignment。

'''


# List - a mutable type

def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)


outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)


print("-----------------------")


def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)


outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)

print("-----------------------")

# String - an immutable type
def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)


outer_string = 'It was many and many a year ago'

print('before, outer_string =', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string =', outer_string)

print("-----------------------")