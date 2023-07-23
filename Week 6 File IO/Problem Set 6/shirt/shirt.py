from PIL import Image, ImageOps
import sys

# Check if user specify exactly two command-line arguments
if len(sys.argv) != 3:
    print("Usage: shirt.py <in_file> <out_file>")
    sys.exit(1)

# Check if in_file and out_file have correct extensions (.jpg, .jpeg, or .png)
exts = ["jpg", "jpeg", "png"]
in_ext = sys.argv[1].split(".")[-1].lower()
out_ext = sys.argv[2].split(".")[-1].lower()
if in_ext not in exts or out_ext not in exts:
    print("Only extensions .jpg, .jpeg, or .png are permitted.")
    sys.exit(2)

# Check if both in_file and out_file have the same extensions
if in_ext != out_ext:
    print("<in_file> does not have the same extension as <out_file>.")
    sys.exit(3)

# Process and export image
try:
    with Image.open(sys.argv[1]) as img:
        model_img = ImageOps.fit(image=img, size=(600, 600))
        with Image.open("shirt.png") as shirt_img:
            model_img.paste(shirt_img, box=(0, 0), mask=shirt_img)
            model_img.save(sys.argv[2])
except FileNotFoundError:
    print("Specified in_file does not exist.")
    sys.exit(4)
