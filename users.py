# users.py — User Database with Roles

users = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "email": "admin@techcorp.com"
    },
    "prabhpreet": {
        "password": "user123",
        "role": "user",
        "email": "prabhpreet@techcorp.com"
    },
    "guest": {
        "password": "guest123",
        "role": "guest",
        "email": "guest@techcorp.com"
    }
}

# Role permissions — RBAC
permissions = {
    "admin": ["view_all_users", "add_user",
              "delete_user", "view_logs", "view_dashboard"],
    "user":  ["view_dashboard", "view_own_profile"],
    "guest": ["view_dashboard"]
}

def get_user(username):
    return users.get(username, None)

def get_permissions(role):
    return permissions.get(role, [])