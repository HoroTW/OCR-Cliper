# %% imports
import os
import easyocr
from linux_integration import *

# set DEBUG, if env var DEBUG is set to 1
DEBUG = os.environ.get("DEBUG") == "1"

# %% Get image/file path from clipboard
image = get_from_xclip()

# check if image is a valid path and an image file
if os.path.isfile(image) and image.endswith(
    (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
):
    if DEBUG:
        print("Image path from clipboard: " + image)
else:  # it is not a path to an image file
    if image != "":  # if clipboard is empty - e.g. image data in clipboard
        print("Clipboard is not a path to an image file or an image")
        exit(1)

    image = get_from_xclip(image=True)  # try to get an image from clipboard
    if type(image) != bytes:
        print("Clipboard is not a path to an image file or an image")
        exit(1)

# %% Execute OCR
# load the model to ram (with the languages you want to use)
reader = easyocr.Reader(["de", "en"])
# now we can read the text from the image
result = reader.readtext(image)

# and print it
resultString = ""

for r in result:
    # if env var DEBUG is set to 1, then print whole r
    if DEBUG:
        resultString += str(r) + "\n"
    else:
        resultString += r[1] + "\n"

print(resultString)

# copy the result to clipboard
copy_to_xclip(resultString)

# notify that it is done
notify(title="OCR", message="Text copied to clipboard")
