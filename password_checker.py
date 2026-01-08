def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    if criteria_met == 4:
        return "Strong"
    elif criteria_met >= 2:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    passwords = ["123", "password", "Pass123", "Strong!123", "Weak1"]
    for p in passwords:
        print(f"Password: {p} -> Strength: {check_password_strength(p)}")
