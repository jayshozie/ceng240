# import time
decimal = int(input("Please enter the integer you want to convert to binary : "))
bits_str = ""

next_iter = decimal
i = 0
while True:
    if next_iter == 0:
        break

    remainder = next_iter % 2
    next_iter = next_iter // 2
    bits_str += str(remainder)

    # print("----------------------------------------------------")
    # print(f"DEBUG | decimal = {decimal} | bits_str = {bits_str}")
    # print("----------------------------------------------------")
    # print(f"DEBUG | next_iter = {next_iter} | remainder = {remainder}")
    # time.sleep(2)

bits_str = bits_str[::-1]  # Reversing the string
print(bits_str)
