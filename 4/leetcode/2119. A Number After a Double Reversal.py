num = 526

num_list = list(str(num))
num_reverse_list = list(reversed(num_list))
reverse1_num = int(''.join(num_reverse_list))

reverse2_num = int(''.join(list(reversed(list(str(reverse1_num))))))

# print(reverse_num)
print(num == reverse2_num)