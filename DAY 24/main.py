# #reading a file
# with open("D:\STUDY\CODE\PYTHON 100DAYS CODE\DAY 24\my_file.txt") as file:
#     content = file.read()
#     print(content)

#writing a file
# with open("D:\STUDY\CODE\PYTHON 100DAYS CODE\DAY 24\my_file.txt", mode="w") as file:
#     file.write("New content")
    
with open("new_file.txt", mode="a") as file:
    file.write("\nNew content")

# modes
# r = read
# w = write
# a = append