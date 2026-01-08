from datetime import datetime

def analyze_attendance(logs):
    student_data = {}
    
    for name, date, status in logs:
        if name not in student_data:
            student_data[name] = {"dates": [], "statuses": []}
        student_data[name]["dates"].append(date)
        student_data[name]["statuses"].append(status)

    results = {}
    for name, data in student_data.items():
        total = len(data["statuses"])
        present_count = data["statuses"].count("Present")
        percentage = (present_count / total) * 100
        
        max_streak = 0
        current_streak = 0
        for status in data["statuses"]:
            if status == "Present":
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0
        
        results[name] = {
            "percentage": round(percentage, 2),
            "low_attendance": percentage < 75,
            "longest_streak": max_streak
        }
        
    return results

if __name__ == "__main__":
    attendance = [
        ("Ajay", "2026-01-01", "Present"),
        ("Ajay", "2026-01-02", "Absent"),
        ("Ajay", "2026-01-03", "Present"),
        ("Ajay", "2026-01-04", "Present"),
        ("Rahul", "2026-01-01", "Present"),
        ("Rahul", "2026-01-02", "Present"),
        ("Rahul", "2026-01-03", "Present")
    ]
    
    report = analyze_attendance(attendance)
    print("Attendance Report:")
    for student, stats in report.items():
        print(f"{student}: {stats}")
