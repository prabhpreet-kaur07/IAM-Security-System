# auth.py — Login + MFA Verification

import random
from users import get_user, get_permissions

def check_password(username, password):
    user = get_user(username)
    if user is None:
        return False, "User not found!"
    if user["password"] == password:
        return True, "Password correct!"
    return False, "Wrong password!"

def generate_otp():
    otp = random.randint(1000, 9999)
    print(f"\n Your OTP is: {otp}")
    return str(otp)

def verify_otp(real_otp, entered_otp):
    if real_otp == entered_otp:
        return True
    return False

def login(username, password):
    print(f"\n Trying to login as: {username}")
    
    # Step 1 - Check password
    success, message = check_password(username, password)
    if not success:
        print(f" Login failed: {message}")
        return None
    
    print(" Password verified!")
    
    # Step 2 - MFA (OTP)
    print(" MFA required - sending OTP...")
    otp = generate_otp()
    entered = input(" Enter OTP: ")
    
    if not verify_otp(otp, entered):
        print(" Wrong OTP! Access denied!")
        return None
    
    # Step 3 - Give permissions
    role = get_user(username)["role"]
    permissions = get_permissions(role)
    
    print(f"\n Login successful!")
    print(f" Role: {role}")
    print(f" Permissions: {permissions}")
    
    return {"username": username, 
            "role": role, 
            "permissions": permissions}