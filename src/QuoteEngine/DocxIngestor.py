from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                parsed = paragraph.text.split(" - ")
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)
        return quotes
