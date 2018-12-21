x = [72, 67, 92, 95, 59, 58, 95, 94, 84, 83,
     70, 79, 67, 73, 87, 86, 63, 92, 80, 76]
y = [76, 76, 95, 96, 79, 74, 97, 97, 90, 90,
     78, 91, 76, 90, 95, 95, 75, 10, 87, 90]



def pearson(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    sx = (sum([(i - mean_x)**2 for i in x]) / (n - 1))**0.5
    sy = (sum([(i - mean_y)**2 for i in y]) / (n - 1))**0.5

    xy = sum([x[i] * y[i] for i in range(n)])
    x_y = sum(x) * sum(y)

    x2 = sum([i**2 for i in x])
    y2 = sum([i**2 for i in y])
    rxy = (n * xy - x_y) / (
        (n * x2 - sum(x)**2)**0.5 * (n * y2 - sum(y)**2)**0.5)
    rxy = round(rxy, 2)
    return str(rxy)

    result = [pearson(math, phy), pearson(phy, chem), pearson(math, chem)]
    return result


ans = pearson(x, y)
print(ans)
