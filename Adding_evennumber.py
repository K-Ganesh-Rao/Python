target = int(input())
even_sum = 0
for number in range(2 , target+1 , 2):
    even_sum += number
print(even_sum)

#alternate method

# target = int(input())
# even_sum = 0
# for number in range(2 , target+1):
#     if number % 2 == 0:
#         even_sum += number

# print(even_sum)
