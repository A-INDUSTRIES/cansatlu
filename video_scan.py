from PIL import Image
import cv2

def get_sigmas(video="C:/Users/AINDUSTRIES/error.webm"):
    print("Working on video")
    vid = cv2.VideoCapture(video)
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    x_sigmas, y_sigmas = [], []
    i = 0
    while True:
        ret, frame = vid.read()
        if ret:
            print(f"Working on frame {i} out of {length} : {i/length:.2f}% done.", end="\t")
            sigs = get_sigma(frame)
            print(f"Frame sigs = {sigs}", end="\r")
            x_sigmas.append(sigs[0])
            y_sigmas.append(sigs[1])
            i += 1
        else:
            break
    return [x_sigmas, y_sigmas]


def get_sigma(frame):
    xs, ys = [], []
    img = Image.frombuffer(mode="RGB", size=(frame.shape[0], frame.shape[1]), data=frame)
    img.convert("RGB")
    for y in range(0, img.height):
        for x in range(0, img.width):
            pix = img.getpixel((x,y))
            if pix[1] > 100 and pix[0] < 100 and pix[2] < 100:
                xs.append(x)
                ys.append(y)

    num = img.width * img.height

    x_bar = sum(xs) / num
    y_bar = sum(ys) / num

    vxp = sum([pow(x * x_bar, 2) for x in xs]) / num
    vyp = sum([pow(y * y_bar, 2) for y in ys]) / num

    sig_x = pow(vxp, 1/2)
    sig_y = pow(vyp, 1/2)

    return [sig_x, sig_y]

if __name__ == "__main__":
    print(get_sigmas())