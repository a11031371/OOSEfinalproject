from base.converter import Converter
from base.data import Data
from .data import Meeting, Expenditure, Task
from .conf import *

class ChurchConverter(Converter):
    def getIndividualScore(self, person: str) -> int:
        totalScore = 0
        events = self._aggregator.getEvents()

        # Sum up all IndividualScore in each event
        for e in events:
            totalScore += e.getIndividualScore(person)

        return totalScore

    
    def getGroupScore(self, person: str) -> dict:
        groupScore = {}
        events = self._aggregator.getEvents()
        for e in events:
            practitioners = e.getPractitioners()
            score = e.getIndividualScore(person)
            for practitioner in practitioners:
                if practitioner == person:
                    continue
                else:
                    # Add division score to other people
                    if practitioner not in groupScore:
                        groupScore[practitioner] = score / len(practitioners)
                    else:
                        groupScore[practitioner] += score / len(practitioners)
        return groupScore
