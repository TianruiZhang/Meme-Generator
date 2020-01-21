import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import ImageCaptioner
from glob import glob
from os import makedirs, remove
from random import choice, randint
from os.path import exists, join
from time import sleep

app = Flask(__name__)

def setup():
    """ Load all resources """

    quote_files = ["./_data/DogQuotes/DogQuotesTXT.txt",
                   "./_data/DogQuotes/DogQuotesDOCX.docx",
                   "./_data/DogQuotes/DogQuotesPDF.pdf",
                   "./_data/DogQuotes/DogQuotesCSV.csv"]

    quotes = [Ingestor.parse(file) for file in quote_files]

    images_path = "./_data/photos/dog/*"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = glob(images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """

    img = choice(imgs)
    quote = choice(quotes[0])
    captioner = ImageCaptioner.MemeGenerator(
        "static",
        "./fonts/Acme-Regular.ttf"
    )
    path = captioner.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]
    response = requests.get(image_url)
    rand = randint(0, 100)
    path = join("static", f"image_{rand}.jpg")
    if response.status_code == 200:
        with open(path, "wb") as infile:
            infile.write(response.content)
    captioner = ImageCaptioner.MemeGenerator(
        "static",
        "./fonts/Acme-Regular.ttf"
    )
    path = captioner.make_meme(path, body, author)
    to_delete = [
        file for file in glob("static/*.jpg") if file != path
    ]
    for file in to_delete:
        remove(file)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
