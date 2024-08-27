ages = {
    "adele": 36,
    "eminem": 51,
    "travis scott": 33,
    "lady gaga": 38,
    "lana del rey": 39,
}

maxage = max(ages.values())

for i in ages:
    if ages[i] == maxage:
        print(i, ":", maxage)
