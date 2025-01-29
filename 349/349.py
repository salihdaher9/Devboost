# company_tree1.py
import json
from dis import deoptmap


def number_of_employees(dept):

    if len(dept["departments"])==0:
        return len(dept["members"])
    else:
        sons=0
        for i in dept["departments"]:
            sons+=number_of_employees(i)
        return len(dept["members"]) +sons

def total_salaries(dept):
    if len(dept["departments"])==0:
        return sum(dept["members"][i]["salary"] for i in range(len(dept["members"])))
    else:
        sons=0
        for i in dept["departments"]:
            sons+=total_salaries(i)
        return sum(dept["members"][i]["salary"] for i in range(len(dept["members"]))) +sons


with open("company3.json") as f:
    data = json.load(f)

num = number_of_employees(data)
print("Total employees:", num)
assert num == 115
print("OK1")

salary = total_salaries(data)
print("Total salary:", salary)
assert salary == 2341200
print("OK2")

print("Done!")