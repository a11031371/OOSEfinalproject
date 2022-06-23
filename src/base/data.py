import abc


class Data(abc.ABC):
    def __init__(self):
        self._practitioners = [[]]

    @abc.abstractmethod
    def getIndividualScore(self, person: str) -> int:
        return NotImplemented

    def getPractitioners(self) -> list[list[str]]:
        return self._practitioners


class DataAggregator(abc.ABC):
    def __init__(self):
        self._events = []

    def getEvents(self) -> list[Data]:
        return self._events

    def add(self, event: Data) -> bool:
        self._events.append(event)
        return True
