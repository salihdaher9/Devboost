# company_tree2.py

import json

def simple_org_chart(dept, indent=0):
    s = "  " * indent + "- " + dept["title"] + "\n"

    for sub_dept in dept["departments"]:
        s += simple_org_chart(sub_dept, indent + 1)

    return s



with open("company3.json") as f:
    data = json.load(f)

s = simple_org_chart(data)
print(s)
expected = """- ACME International
  - Management
  - Operations
    - Human Resources
    - IT
      - Helpdesk
    - Customer Support
  - Marketing
    - Sales
  - Research and Development
    - Software Engineering
      - Web Development
      - Mobile Development
      - Backend Development
        - Algorithms
        - Computer Vision
        - Graphics
    - Quality Assurance
      - Test Engineering
      - Automation
    - Data Engineering
      - Cloud
"""
assert s == expected

print("OK")