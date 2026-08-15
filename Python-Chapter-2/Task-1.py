"""
Task 1: Functions/Methods associated with Python Data Structures

Data structures covered:
1. List
2. Tuple
3. Set
4. Dictionary

"""

# ============================================================
# 1. LIST FUNCTIONS / METHODS
# ============================================================

numbers = [10, 20, 30, 20]

print("\nLIST")
print("Original:", numbers)

numbers.append(40)
print("append():", numbers)

numbers_copy = numbers.copy()
print("copy():", numbers_copy)

print("count():", numbers.count(20))
print("index():", numbers.index(30))

numbers.extend([50, 60])
print("extend():", numbers)

numbers.insert(1, 15)
print("insert():", numbers)

numbers.remove(20)
print("remove():", numbers)

removed_item = numbers.pop()
print("pop():", numbers, "| Removed:", removed_item)

numbers.reverse()
print("reverse():", numbers)

numbers.sort()
print("sort():", numbers)

numbers.clear()
print("clear():", numbers)


# ============================================================
# 2. TUPLE FUNCTIONS / METHODS
# ============================================================

employee = ("Mukesh", "Data Engineer", 5, "Chennai")

print("\nTUPLE")
print("Original:", employee)
print("count():", employee.count("Data Engineer"))
print("index():", employee.index("Chennai"))

# Common built-in functions used with tuples
print("len():", len(employee))
print("max():", max((10, 20, 30)))
print("min():", min((10, 20, 30)))
print("sum():", sum((10, 20, 30)))
print("sorted():", sorted((30, 10, 20)))


# ============================================================
# 3. SET FUNCTIONS / METHODS
# ============================================================

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("\nSET")
print("Set A:", set_a)
print("Set B:", set_b)

temp = set_a.copy()
temp.add(50)
print("add():", temp)

temp = set_a.copy()
temp.clear()
print("clear():", temp)

print("copy():", set_a.copy())
print("difference():", set_a.difference(set_b))
print("intersection():", set_a.intersection(set_b))
print("isdisjoint():", set_a.isdisjoint({70, 80}))
print("issubset():", {10, 20}.issubset(set_a))
print("issuperset():", set_a.issuperset({10, 20}))

temp = set_a.copy()
temp.pop()
print("pop():", temp)

temp = set_a.copy()
temp.discard(20)
print("discard():", temp)

temp = set_a.copy()
temp.remove(20)
print("remove():", temp)

temp = set_a.copy()
temp.update({50, 60})
print("update():", temp)

print("union():", set_a.union(set_b))
print("symmetric_difference():", set_a.symmetric_difference(set_b))

temp = set_a.copy()
temp.difference_update(set_b)
print("difference_update():", temp)

temp = set_a.copy()
temp.intersection_update(set_b)
print("intersection_update():", temp)

temp = set_a.copy()
temp.symmetric_difference_update(set_b)
print("symmetric_difference_update():", temp)


# ============================================================
# 4. DICTIONARY FUNCTIONS / METHODS
# ============================================================

employee = {
    "name": "Mukesh",
    "role": "Data Engineer",
    "experience": 5,
    "location": "Chennai"
}

print("\nDICTIONARY")
print("Original:", employee)
print("clear() demonstration:", {"a": 1}.clear())
print("copy():", employee.copy())
print("get():", employee.get("role"))
print("items():", employee.items())
print("keys():", employee.keys())
print("values():", employee.values())

employee.setdefault("salary", 100000)
print("setdefault():", employee)

employee.update({"experience": 6, "company": "Example Company"})
print("update():", employee)

removed_value = employee.pop("company")
print("pop():", employee, "| Removed:", removed_value)

last_item = employee.popitem()
print("popitem():", employee, "| Removed:", last_item)

print("fromkeys():", dict.fromkeys(["name", "role", "location"], "Not Available"))

employee.clear()
print("clear():", employee)
