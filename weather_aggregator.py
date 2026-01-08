def aggregate_weather(weather_data):
    if not weather_data:
        return {}

    total_temp = 0
    rainy_days_count = 0
    hottest_temp = -float('inf')
    hottest_day = None

    for entry in weather_data:
        day = entry["day"]
        temp = entry["temp"]
        rain = entry["rain"]

        total_temp += temp
        
        if rain:
            rainy_days_count += 1
        
        if temp > hottest_temp:
            hottest_temp = temp
            hottest_day = day

    avg_temp = total_temp / len(weather_data)

    summary = {
        "hottest_day": hottest_day,
        "average_temperature": round(avg_temp, 2),
        "rainy_days": rainy_days_count
    }
    
    return summary

if __name__ == "__main__":
    weather = [
        {"day": "Mon", "temp": 32, "rain": False},
        {"day": "Tue", "temp": 35, "rain": True},
        {"day": "Wed", "temp": 30, "rain": False}
    ]
    print(aggregate_weather(weather))
