import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import ImageCaptioner
from glob import glob
from os import makedirs, remove
from random import choice
from os.path import exists, join

app = Flask(__name__)
app.debug = True

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

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = choice(imgs)
    quote = choice(quotes[0])
    captioner = ImageCaptioner.MemeGenerator(
        "static", 
        "./fonts/Acme-Regular.ttf"
    )
    path = captioner.make_meme(img, quote.body, quote.author)
    # print(f"The path is {path}")
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]
    response = requests.get(image_url)
    path = join("static", "image.jpg")
    if response.status_code == 200:
        with open(path, "wb") as infile:
            infile.write(response.content)
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author from paramaters.
    captioner = ImageCaptioner.MemeGenerator(
        "static", 
        "./fonts/Acme-Regular.ttf"
    )
    path = captioner.make_meme(path, body, author)
    # 3. Remove the temporary saved image.
    remove(path)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
