from PIL import Image, ImageDraw, ImageFont
from random import randint
from os.path import exists
from os import makedirs


class MemeGenerator:

    def __init__(self, out_dir: str, font_path: str):
        self.out_dir = out_dir
        self.font_path = font_path
    
    def make_meme(self, img_path: str, text: str, author: str, width: int=500) -> str:
        assert width is not None, "Width cannot be empty!"
        assert width <= 500, "The maximum width is 500px!"
        assert img_path.split(".")[-1] in ["jpg", "png"], "The imported images should be JPG/PNG"
        img = Image.open(img_path)
        author = f"          -{author}"
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(img)
        text_font = ImageFont.truetype(
            self.font_path, 
            size=30
        )
        author_font = ImageFont.truetype(
            self.font_path, 
            size=20
        )
        x = randint(0, width)
        y = randint(0, height)
        if text is not None:
            draw.text(
                (x, y), 
                text, 
                font=text_font, 
                fill="yellow"
            )
        if author is not None:
            draw.text(
                (x, y+30), 
                author, 
                font=author_font, 
                fill="yellow"
            )
        if not exists(self.out_dir):
            makedirs(self.out_dir)

        output_path = f"{self.out_dir}/{img_path.split('/')[-1]}"
        img.save(output_path)
        return output_path