def analyze_students(students):
    results = {}
    
    topper_name = None
    max_avg = -1

    for name, marks in students:
        if not marks:
            avg = 0
        else:
            avg = sum(marks) / len(marks)
        
        if avg >= 85:
            status = "Distinction"
        elif avg >= 50:
            status = "Pass"
        else:
            status = "Fail"
        
        results[name] = {"average": round(avg, 2), "status": status}

        if avg > max_avg:
            max_avg = avg
            topper_name = name

    return results, topper_name

if __name__ == "__main__":
    students_data = [
        ("Ajay", [78, 85, 90]),
        ("Kumar", [65, 70, 60]),
        ("Rahul", [88, 92, 95])
    ]
    
    results, topper = analyze_students(students_data)
    print("Results:", results)
    print("Topper:", topper)
