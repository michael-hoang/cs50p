file = input("File name: ").lower().strip()
extension = file.split(".")[-1]
if extension in ["gif", "jpg", "jpeg", "png"]:
    if extension == "jpg":
        extension = "jpeg"
    print(f"image/{extension}")
elif extension in ["pdf", "zip"]:
    print(f"application/{extension}")
elif extension == "txt":
    print("text/plain")
else:
    print("application/octet-stream")