from QuoteEngine import Ingestor
from MemeEngine import ImageCaptioner
from argparse import ArgumentParser
from glob import glob
from os.path import abspath
from random import choice

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Generate a Memed Image!"
    )
    parser.add_argument("--body", type=str)
    parser.add_argument("--author", type=str)
    parser.add_argument("--img_path", type=str)
    args = parser.parse_args()
    body = args.body
    author = args.author
    img_path = args.img_path
    captioner = ImageCaptioner.MemeGenerator(
        "_data/MemedImages",
        "./fonts/Acme-Regular.ttf"
    )
    if all([body, author, img_path]):
        captioner.make_meme(img_path, body, author)
    else:
        img_path = choice(glob("./_data/photos/dog/*"))
        text_path = choice(glob("./_data/DogQuotes/*"))
        body, author = choice(Ingestor.parse(text_path))
        captioner.make_meme(img_path, body, author)
