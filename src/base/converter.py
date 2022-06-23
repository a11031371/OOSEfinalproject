import abc

from .data import DataAggregator


class Converter(abc.ABC):
    def __init__(self, aggregator: DataAggregator):
        self._aggregator = aggregator

    @abc.abstractmethod
    def getIndividualScore(self, person: str) -> int:
        return NotImplemented

    @abc.abstractmethod
    def getGroupScore(self, person: str) -> dict:
        return NotImplemented
