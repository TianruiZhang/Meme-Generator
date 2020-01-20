from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")
        quotes = []
        with open(path, "r") as infile:
            for line in infile.readlines():
                parsed = line.split(" - ")
                try:
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)
                except IndexError:
                    break
        return quotes