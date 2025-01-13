import json
# TODO решите задачу
def task(file) -> float:
    y = 0
    for sum in file:
        y += sum["score"] * sum["weight"]
    return round(y, ndigits=3)


with open("input.json", 'r') as f:
    data = json.load(f)

print(task(data))


