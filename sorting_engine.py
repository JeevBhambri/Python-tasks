def sort_employees(employees, key, reverse=False):
    try:
        sorted_list = sorted(employees, key=lambda x: x[key], reverse=reverse)
        return sorted_list
    except KeyError:
        print(f"Error: Key '{key}' not found in employee records.")
        return employees

def sort_by_age_then_salary(employees):
    sorted_list = sorted(employees, key=lambda x: (x["age"], x["salary"]))
    return sorted_list

if __name__ == "__main__":
    employees = [
        {"name": "Ajay", "age": 22, "salary": 25000},
        {"name": "Rahul", "age": 25, "salary": 40000},
        {"name": "Kiran", "age": 21, "salary": 30000},
        {"name": "Amit", "age": 22, "salary": 20000}
    ]

    print("Sorted by Salary (Descending):")
    print(sort_employees(employees, "salary", reverse=True))

    print("\nSorted by Age, then Salary:")
    print(sort_by_age_then_salary(employees))

    print("\nDynamic Sort by Name:")
    print(sort_employees(employees, "name"))
