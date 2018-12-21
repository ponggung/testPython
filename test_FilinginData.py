import numpy as np
import pandas as pd

with open("text","r") as file:
    lines = file.readlines()

n = int(lines[0])

values = []
for line in lines:
    line.strip("\n")
    line = line.strip("\n").split(" ")
    if len(line)==1:
        n = int(line[0])
    else:
        value = line[1].split("\t")[1]
        values.append(value)

def trans(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return None

index = [i for i, v in enumerate(values) if "Missing" in v]
values = pd.Series([trans(i) for i in values])
values = values.fillna(method='ffill')

output = list(values[index])
output = [str(i) for i in output]
output = "\n".join(output)
print(output)
