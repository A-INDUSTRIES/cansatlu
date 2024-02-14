from PIL import Image
from pathlib import Path

GREEN_RANGE_END = (200, 255, 175)  # Green redish to blueish
GREEN_RANGE_START = (0, 20, 0)  # Dark Green


def get_sigma(image_location: Path):
    xs, ys = [], []
    img = Image.open(image_location)
    img.convert("RGB")
    for y in range(0, img.height):
        for x in range(0, img.width):
            pix = img.getpixel((x, y))
            if all(
                [GREEN_RANGE_START[i] <= pix[i] <= GREEN_RANGE_END[i] for i in range(3)]
            ):
                xs.append(x)
                ys.append(y)
                img.putpixel((x, y), (255, 0, 0))

    num = img.width * img.height

    x_bar = sum(xs) / num
    y_bar = sum(ys) / num

    vxp = sum([pow(x * x_bar, 2) for x in xs]) / num
    vyp = sum([pow(y * y_bar, 2) for y in ys]) / num

    sig_x = pow(vxp, 1 / 2)
    sig_y = pow(vyp, 1 / 2)

    img.save("treated.png")

    return [sig_x, sig_y]


if __name__ == "__main__":
    print(get_sigma(Path(input("Provide the file path: "))))
