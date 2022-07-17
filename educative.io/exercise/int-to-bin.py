from stack import Stack
def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        if dec_num == 0:
            break
        else:
            remainder = dec_num % 2
            dec_num = dec_num // 2 
            s.push(remainder)
    bin_num = ""
    while not s.isEmpty():
        bin_num += str(s.pop())
    return bin_num
    
    
print(convert_int_to_bin(25))
print(convert_int_to_bin(10))
print(convert_int_to_bin(0))
print(convert_int_to_bin(1))