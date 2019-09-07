# f = open('demo.txt', mode='r')
# # f.write('Add this content\n ')
# file_content = f.readlines()
# f.close()

# print(file_content)

# print every member of list except for newline (/n) character
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
with open('demo.txt', mode='w') as F:
    F.write('Testing if this closes ...')
user_input = input('Testing: ')
print('All Done!')

