def analyze_logs(logs):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_messages = {}

    for entry in logs:
        parts = entry.split(" ", 3)
        if len(parts) < 4:
            continue
        
        level = parts[2]
        message = parts[3]

        if level in counts:
            counts[level] += 1
        
        if level == "ERROR":
            error_messages[message] = error_messages.get(message, 0) + 1

    most_common_error = None
    max_count = -1
    for msg, count in error_messages.items():
        if count > max_count:
            max_count = count
            most_common_error = msg

    result = counts.copy()
    result["most_common_error"] = most_common_error
    return result

if __name__ == "__main__":
    sample_logs = [
        "2026-01-02 10:15:32 ERROR Database connection failed",
        "2026-01-02 10:16:01 INFO System started",
        "2026-01-02 10:17:15 ERROR Database connection failed",
        "2026-01-02 10:18:10 WARNING Low disk space",
        "2026-01-02 10:19:05 ERROR Timeout occurred",
        "2026-01-02 10:20:00 INFO User logged in"
    ]
    print(analyze_logs(sample_logs))
