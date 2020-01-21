# Motivational Puppy Meme Generator

The goal of this project is to build a "meme generator" — a multimedia application to dynamically generate memes, including an image with an overlaid quote.

![demo gif](./demo.gif)

## Configuration
### Dependencies
1. Python 3.7
2. Packages are listed in `requirements.txt` (See Installation).
### Installation
1. Clone the repository: `git clone https://github.com/TianruiZhang/Meme-Generator.git`
2. Switch directory: `cd Meme-Generator`
2. Create a virtual environment: `python3 -m venv venv`
3. Switch to `src` directory: `cd src`
3. Activate the vitural environment: `source venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
## Instruction
1. `main.py`: a command line interface tool

    The program takes three OPTIONAL arguments:
    * A string quote body (`--body`)
    * A string quote author (`--author`)
    * An image path (`--img_path`)

    The program returns a path to a generated image. If any of the three arguments is not defined, a random selection is used.

2. `app.py`: a web interface

    In the virtual environment, run `python app.py` and type `http://127.0.0.1:5000/` in your browser.

## Modules
### QuoteEngine Module

The QuoteEngine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). Example quotes are provided in a variety of files, take a moment to review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`. 

### MemeEngine Module

The MemeEngine Module is responsible for manipulating and drawing text onto images. 

#### The MemeGenerator class
The class is responsible for:
1. loading an image using Pillow (PIL)
2. resizing the image so the width is at most 500px and the height is scaled proportionally
3. add a quote body and a quote author to the image
4. saving the manipulated image
