# Files


# # This method we have to close the file
# f = open("file", "r")
# f.close()


# This method automatically closes files
with open("basic/file.txt", "r") as file:

    # Read the file content
    # This reads all the content at once, this could load the memmory
    file_content = file.read()
    print(file_content)
    
    # Efficient way to do it
    # end = "" removes the default line break
    for line in file: 
        print(line, end="")
