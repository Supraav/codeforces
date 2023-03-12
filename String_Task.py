str_inp=input().lower()
# print(b)
vowels=['a','e','i','o','u','y']
l=[f'.{x}' for x in str_inp if x not in vowels]

# result=""
# for i in range(len(str_inp)):
#     if str_inp[i] not in vowels:
#         result = result + str_inp[i]
# print(result)

final=''.join(l)
print(final)
