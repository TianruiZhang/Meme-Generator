from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if the file type is compatible with the ingestor class"""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """An abstract method for parsing the file content"""
        pass
