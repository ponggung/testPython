def isVaild(string):
    tf1 = string.count("(") == string.count(")")
    tf2 = string[0] == ("(") and string[-1] == (")")
    tf = tf1 and tf2
    if tf:
        return "valid"
    else:
        return "invalid"


str1 = "()()()()()"  #valid
str2 = "(()()())"  #valid
str3 = "))))(((( "  #invalid
str4 = "(((())))) "  #invalid

print(isVaild(str1))
print(isVaild(str2))
print(isVaild(str3))
print(isVaild(str4))