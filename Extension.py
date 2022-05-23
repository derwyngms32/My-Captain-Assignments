filename = input("Input the Filename:  ")
extension = filename.split(".")

if extension[1] == "py":
    print("The Extension of the file is: Python")
elif extension[1] == "c":
    print("The Extension of the file is: C ")
elif extension[1] == "cpp":
    print("The Extension of the file is: C++ ")
else:
    print("Invalid Input")
