userfilename = input("Enter File Name: ")

# remove whitespace and turn to lowercase
userfilename = userfilename.strip().lower()

# classify the files to their file types
if ".gif" in userfilename:
    print("image/gif")
elif ".jpg" in userfilename or ".jpeg" in userfilename:
    print("image/jpeg")
elif ".png" in userfilename:
    print("image/png")
elif ".pdf" in userfilename:
    print("application/pdf")
elif ".txt" in userfilename:
    print("text/plain")
elif ".zip" in userfilename:
    print("application/zip")
else:
    print("application/octet-stream")