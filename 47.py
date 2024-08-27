import sys

scores = {
    "fizik": 17,
    "riazi": 15,
    "arabi": 7,
    "farsi": 16,
    "shimi": 17,
}

for i, j in scores.items():
    # print(i[0],i[1])
    if j >= 10:
        print(i, ": passed")
    else:
        print(i, ": failed", file=sys.stderr)
# ---------------------------------------------------
grade = sum(scores.values()) / len(scores)
print(grade)
