from .IngestorInterface import IngestorInterface
from typing import List
from subprocess import Popen
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel
import re
from os import remove


class PDFIngestor(IngestorInterface):
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")
        process = Popen(
            f"pdftotext -layout {path}",
            shell=True
        )
        process.wait()
        path = re.sub(r"pdf$", "txt", path)
        quotes = TextIngestor.parse(path)
        remove(path)
        return quotes
