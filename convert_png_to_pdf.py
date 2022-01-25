import argparse
from PIL import Image


def png2pdf(in_file, out_file, resolution=120):
    image1 = Image.open(in_file)
    im1 = image1.convert('RGB')
    im1.save(out_file, resolution=resolution)


def main():
    parser = argparse.ArgumentParser("converting png into pdf")
    parser.add_argument("in_file", type=str)
    parser.add_argument("out_file", type=str)
    parser.add_argument("--resolution", type=int, default=120)

    args = parser.parse_args()

    png2pdf(args.in_file, args.out_file, args.resolution)


if __name__ == "__main__":
    main()
