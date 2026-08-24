import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_extensions = (".jpg", ".jpeg", ".png")
    input_file = sys.argv[1].lower()
    output_file = sys.argv[2].lower()

    if not input_file.endswith(valid_extensions):
        sys.exit("Invalid input")
    if not output_file.endswith(valid_extensions):
        sys.exit("Invalid output")
    if input_file.split(".")[-1] != output_file.split(".")[-1]:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as photo:
            fitted_photo = ImageOps.fit(photo, shirt.size)
            
            
            fitted_photo.paste(shirt, (0, 0), shirt)
            fitted_photo.save(sys.argv[2])
            
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()