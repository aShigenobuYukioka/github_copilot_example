def check_user(user):
    if user:
        if user["age"] >= 18:
            if user["account_active"]:
                if "email" in user:
                    return "Access granted"
                else:
                    return "Email required"
            else:
                return "Account inactive"
        else:
            return "User under 18"
    else:
        return "No user data"


print(check_user({"age": 20, "account_active": True, "email": "user@example.com"}))
