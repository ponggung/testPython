e = "SKA-1946 St. Petersburg U21"
c = "斯圖皮諾隊長 U21"

def is_chinese(s):
    if s >= u'\u4e00' and s<=u'\u9fa5':
        return True
    else:
        return False


print(is_chinese(e))
print(is_chinese(c))

foo = "新澤西惡魔"
print(foo.replace("新澤西惡魔", "新澤西魔鬼"))