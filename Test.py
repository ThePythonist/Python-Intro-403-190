people = {
    "reza": 14,
    "mamad": 16,
    "arian": 19,
}

# print("man", name, "hastam", "va", age, "sal daram")
# =================================================================
# print("man {} hastam va {} sal daram".format(name, age))
# =================================================================
# print("man {n} hastam va {a} sal daram".format(a=age, n=name))
# =================================================================
for k, v in people.items():
    print(f"man {k} hastam va {v} sal daram")
