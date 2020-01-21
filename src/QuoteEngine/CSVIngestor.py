from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")
        quotes = []
        df = pandas.read_csv(path)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row["body"], row["author"])
            quotes.append(new_quote)
        return quotes
