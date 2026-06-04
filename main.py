# main.py — Run the IAM System

from auth import login

print("=" * 40)
print("   TECHCORP IAM SECURITY SYSTEM")
print("   Built by: Prabhpreet Kaur")
print("=" * 40)

print("\n Available users:")
print("   Username: admin    Password: admin123")
print("   Username: prabhpreet  Password: user123")
print("   Username: guest    Password: guest123")

print("\n" + "=" * 40)

username = input("\n Enter username: ")
password = input(" Enter password: ")

session = login(username, password)

if session:
    print("\n" + "=" * 40)
    print(f" Welcome {session['username']}!")
    print(f" Your role: {session['role']}")
    print("\n You can access:")
    for permission in session['permissions']:
        print(f"   ✓ {permission}")
    print("=" * 40)
else:
    print("\n Access Denied! Please try again.")