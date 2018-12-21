s="12413525"

ls = list(s.strip())

ret, i = 0, 0
while i < len(ls) and ls[i].isdigit() :
    ret = ret*10 + ord(ls[i]) - ord('0')
    print(ret)
    i += 1

print(ret)