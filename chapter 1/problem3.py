import os

# Select the directory whose content you want to list :
diretory_path = "/"

# Use the os module to list the directory content
contents = os.listdir(diretory_path)

#Print the content of the diretory    
print(contents)