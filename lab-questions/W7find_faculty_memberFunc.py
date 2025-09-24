"""
Question asks the developer to implement a function formatted like this:
    find_faculty_member(member_name, file_name)
        Takes a member name and a file name, returns the faculty
        member's office.
        
        Arguments
        ---------
        member_name : string, case-insensitive
        file_name   : string

        Returns
        -------
        office_number : string, if the member_name is available
        None, the member_name is not available

File is not malformed, and it doesn't have a header. Format of the file:
<member name> <office>
<member name> <office>
E.g.:
Ahmet Mehmet Yilmaz A130
Ayse Yildirim A131

Names can be 2 or 3 words separated by ' ' character, name and office is
also separated by ' ' character.

Hint:
You can use <var>.rsplit() to split the variable.

Usage:
>>> print(find_faculty_member("ahmet mehmet Yilmaz", members.csv)
A130
>>> print(find_faculty_member("Ayse Yil", members.csv)
None
"""

# My Solution (100/100)

def find_faculty_member(memName, fName):
    memName_lower = memName.lower()  # Case-insensitive

    with open(fName, 'r') as faculty:
        for line in faculty:
            if not line:
                # Handles empty lines, even if it doesn't exist
                continue
            line = line.strip()  # Handles '\n' characters

            parts = line.rsplit(' ', 1)
            # rsplit since ' ' is in the names too
            
            member_raw = parts[0]
            office_raw = parts[1]

            member = member_raw.strip()
            member_lower = member.lower()  # Case-insensitive

            office = office_raw.strip()  # Handles not-shown characters

            if memName_lower == member_lower:
                return office
            # else:
            #     return None
            # I almost got 50/100 because of the above block.
            # It returns 'None' if the first line doesn't include the
            # member name. Thus it's faulty.


# Test Cases

print(find_faculty_member("ceren yilmaz", "members.csv"))
print(find_faculty_member("Ahmet Mehmet Yilmaz", "members.csv"))
print(find_faculty_member("Ayse Yildirim", "members.csv"))
print(find_faculty_member("ahmet yilmaz", "members.csv"))
print(find_faculty_member("MUSTAFA EFE", "members.csv"))
print(find_faculty_member("Umut Ali", "members.csv"))
print(find_faculty_member("ayse yildirim", "members.csv"))
print(find_faculty_member("John Doe", "members.csv"))
print(find_faculty_member("Zeynep Can", "members.csv"))
print(find_faculty_member("cem YILMAZ", "members.csv"))
print(find_faculty_member("Deniz Soylu", "members.csv"))
