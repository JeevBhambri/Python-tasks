def detect_fraud(transactions):
    suspicious = []
    user_locations = {}

    for tx in transactions:
        is_suspicious = False
        
        if tx["amount"] > 50000:
            is_suspicious = True
        
        user = tx.get("user", "default_user")
        location = tx["location"]
        
        if user in user_locations:
            if location not in user_locations[user]:
                is_suspicious = True
                user_locations[user].append(location)
        else:
            user_locations[user] = [location]

        if is_suspicious:
            suspicious.append(tx)
            
    return suspicious

if __name__ == "__main__":
    transactions = [
        {"id": 1, "user": "A", "amount": 500, "location": "Chennai"},
        {"id": 2, "user": "B", "amount": 45000, "location": "Delhi"},
        {"id": 3, "user": "A", "amount": 52000, "location": "Chennai"},
        {"id": 4, "user": "A", "amount": 200, "location": "Coimbatore"}
    ]
    
    suspicious_txs = detect_fraud(transactions)
    print("Suspicious Transactions:")
    for tx in suspicious_txs:
        print(tx)
