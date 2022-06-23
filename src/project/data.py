from pickletools import float8
from base.data import Data, DataAggregator

from .conf import *


class Meeting(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    def getIndividualScore(self, person: str) -> float:
        personActivity = None

        # Find the person with exact name
        for p in self._practitioners:
            if p[0] == person:
                personActivity = self._practitioners[p]
                break

        # Assign position value by different position
        positionValue = 0
        if personActivity[0] == 'host':
            positionValue = 1 * personActivity[3]
        elif personActivity[0] == 'participant':
            positionValue = 0.8 * personActivity[3]

        # Count score base on weight in configuration file
        return meeting_personal_performance * personActivity[1] + \
               meeting_comment * personActivity[2] + \
               meeting_position * positionValue

class Expenditure(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners

    # Return corresponing score according to configuration file
    def getIndividualScore(self, person: str) -> float:
        personActivity = self._practitioners[0]
        if personActivity[1] != personActivity[2]:
            return common_score
        elif not personActivity[1] and not personActivity[2]:
            return failing_score
        else:
            return qualified_score 

class Task(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners
    def getIndividualScore(self, person: str) -> float:
        personActivity = None

        # Find the person with exact name
        for p in self._practitioners:
            if p[0] == person:
                personActivity = self._practitioners[p]
                break

        # Assign position value by different position
        positionValue = 0
        if personActivity[0] == 'leader':
            positionValue = 1 * personActivity[3]
        elif personActivity[0] == 'participant':
            positionValue = 0.8 * personActivity[3]

        # Count score base on weight in configuration file
        return task_personal_performance * personActivity[1] + \
               task_impression * personActivity[2] + \
               task_position * positionValue

class GitRecord(Data):
    def __init__(self, practitioners):
        self._practitioners = practitioners
    def getIndividualScore(self, person: str) -> float:
        # Find the person with exact name
        for p in self._practitioners:
            if p[0] == person:
                personActivity = self._practitioners[p]
                break
        if personActivity[0]
            return commit_pass_testing * personActivity[1]
        else:
            return commit_fail_testing * personActivity[1]
        
class ProjectDataAggregator(DataAggregator):
    pass
