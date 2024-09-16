courses = {
    "mabani computer": (17, 3),
    "barname sazi pishrafte": (15, 3),
    "tarbiat badani": (20, 1),
    "riazi omomi 1": (15, 3),
    "andishe eslami 1": (7, 2),
}


def pass_or_fail(courses):
    for k, v in courses.items():
        if v[0] >= 10:
            print(k, ": passed")
        else:
            print(k, ": failed")


def grade(courses):
    scores = []
    units = []

    for k, v in courses.items():
        scores.append(v[0] * v[1])
        units.append(v[1])

    print("Grade :", sum(scores) / sum(units))


# pass_or_fail(courses)
grade(courses)
