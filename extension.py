#Extension
extension = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
type = ["Image", "Image", "Image", "Image", "Document", "Text", "Compressed"]
def attach(suffix):
    found = False
    for i in range(len(extension)):
        if suffix == extension[i][1:]:
            print(f"{type[i]}/{extension[i]}")
            found = True
        elif not found and i == len(extension)-1:
            print("application/octet-stream")

file_name = ""
while "." not in file_name:
    file_name = input("File name: ")
for i in range(len(file_name)):
    if file_name[i] == ".":
        suffix = file_name[i+1:]
        attach(suffix)
