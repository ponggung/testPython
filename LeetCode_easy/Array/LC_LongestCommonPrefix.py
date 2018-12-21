def longestCommonPrefix(strs):
    strs.sort(key=lambda s: len(s))
    output=""

    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        alpha = [x[i] for x in strs]
        if len(list(set(alpha))) == 1:
            print(alpha)
            output += alpha[0]
        else:
            break
    return output

# strs = ["flower", "flow", "flight"]
# strs = []
strs = ["aca", "cba"]

print(longestCommonPrefix(strs))
