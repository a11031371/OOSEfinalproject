import abc

from .converter import Converter


class ReportGenerator(abc.ABC):
    def __init__(self, convertor: Converter):
        self._convertor = convertor

    @abc.abstractmethod
    def generate(self, person: str, filePath: str) -> bool:
        return NotImplemented
