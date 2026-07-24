import sys
from PIL import Image
import PIL

def main():
  input_img = sys.argv[1]
  output_img = sys.argv[2]

  index_of_period_inputimg = input_img.index(".")
  index_of_period_outputimg = output_img.index(".")

  if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif (not sys.argv[1].endswith(".png")) and (not sys.argv[1].endswith(".jpeg")) and (not sys.argv[1].endswith(".jpg")) and (not sys.argv[1].endswith(".PNG")) and (not sys.argv[1].endswith(".JPEG")) and (not sys.argv[1].endswith(".JPG")):
    sys.exit("Invalid input")
  elif (not sys.argv[2].endswith(".png")) and (not sys.argv[2].endswith(".jpeg")) and (not sys.argv[2].endswith(".jpg")) and (not sys.argv[2].endswith(".PNG")) and (not sys.argv[2].endswith(".JPEG")) and (not sys.argv[2].endswith(".JPG")):
    sys.exit("Invalid output")
  elif (input_img[index_of_period_inputimg: ] != output_img[index_of_period_outputimg: ]):
    sys.exit("Input and output have different extensions")

  try:
    with Image.open(input_img) as file:
      
      PIL.ImageOps.fit(file, (1200, 1600), method = 3, bleed = 0.0, centering = (0.5,0.5))
      Image.Image.paste(file, Image.open("shirt.png"), (300, 650))
      file.save(output_img)
  except FileNotFoundError:
    sys.exit("Input does not exist")

if __name__ == "__main__":
  main()