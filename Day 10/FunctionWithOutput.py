# Function with output

def format_name(fname, lname):
    fname = fname.title()
    lname = lname.title()
    #print(f"{fname} {lname}")
    return f"{fname} {lname}"

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

print(format_name(fname, lname))