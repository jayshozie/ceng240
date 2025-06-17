print("The binary numbers you enter should be of equal length.")
bin1 = input("Please enter the first binary number : ")
bin2 = input("Please enter the second binary number : ")
is_same = False

ret_bin = ""

if len(bin1) == len(bin2):
    is_same = True

# Bitwise AND Operation
if is_same:
    for i in range(len(bin1)):
        if bin1[i] == '1' and bin2[i] == '1':
            ret_bin += '1'
        else:
            ret_bin += '0'
else:
    print("ERR : The binary numbers you enter should be of equal length.")

# Bitwise OR Operation
# for i in range(len(bin1)):
#     if bin1[i] == bin2[i]:
#         ret_bin += '1'
#     else:
#         ret_bin += '0'

print(ret_bin)
