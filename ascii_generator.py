import PIL.Image

# characters in order of decreasing intensity
chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
chars.reverse()

# resize the image


def change(img, new_width, new_height=100):
    return img.resize((new_width, new_height)).convert("L")

# convert the pixels to characters


def pix_to_char(img):
    pixels = img.getdata()
    new_chars = "".join([chars[pixel//22] for pixel in pixels])
    return new_chars


def main(new_height=100):
    path = input("Enter the path of the image: ")
    try:
        img = PIL.Image.open(path)
    except:
        print("Invalid path")
        return

    width, height = img.size
    ratio = width/height
    new_width = int(new_height * ratio*2.4)
    new_img = pix_to_char(change(img, new_width, new_height))
    image = "\n".join(new_img[i:(i+new_width)]
                      for i in range(0, len(new_img), new_width))
    print(image)
    with (open("ascii_image.txt", "w")) as f:
        f.write(image)

main(200)
