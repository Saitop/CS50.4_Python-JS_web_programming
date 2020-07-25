houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

houses["Hermino"] = "Gryffindor"


for key in houses:
    print(f"key: {key}, value: {houses[key]}")

print("=========")
print(houses)
print("=========")
print(houses["Harry"])
