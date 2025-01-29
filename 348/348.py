# company_simple1.py
import json


def number_of_employees(company):
    return sum([len(company[i]["members"]) for i in range(len(company))])


def total_salaries(company):
    return sum(
        [
            company[i]["members"][j]["salary"]
            for i in range(len(company))
            for j in range(len(company[i]["members"]))
        ]
    )


with open("company2.json") as f:
    data = json.load(f)

num = number_of_employees(data)
print("Total employees:", num)
assert num == 66
print("OK1")

salary = total_salaries(data)
print("Total salary:", salary)
assert salary == 1338800
print("OK2")

print("Done!")
