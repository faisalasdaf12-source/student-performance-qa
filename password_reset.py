# Password Reset Algorithm

emails = ["student@mec.edu", "teacher@mec.edu"]

for request in range(1):
    email = "student@mec.edu"
    
    if email in emails:
        print("Email found")
        password = "NewPass123"
        
        if len(password) >= 8:
            print("Password reset successful")
        else:
            print("Password does not meet requirements")
    else:
        print("User not found")
