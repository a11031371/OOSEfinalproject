from pickle import TRUE
from church.data import Expenditure, Task
from project.converter import ProjectConverter
from project.data import GitRecord, Meeting, ProjectDataAggregator
from project.reportgenerator import ProjectReportGenerator


def churchDemo():
    m1 = Meeting({
        'Potter': [
            'host', 1, 2, 5
        ],
        'Kevin': [
            'participant', 4, 5, 3
        ]
    })
    m2 = Meeting({
        'Kevin': [
            'host', 3, 3, 3
        ],
        'Kelvin': [
            'participant', 3, 2, 1
        ],
        'John': [
            'participant', 5, 5, 5
        ],
        'Peter': [
            'participant', 2, 4, 4
        ]
    })
    e1 = Expenditure({
        'Lily': [
            'spender', True, True
        ]
    })
    e2 = Expenditure({
        'Tim': [
            'spender', False, False 
        ]
    })
    t1 = Task({
        'Pastor': [
            'leader', 5, 5, 5
        ],
        'Chris': [
            'participant', 3, 5, 4
        ],
        'Allen': [
            'participant', 5, 5, 5
        ]
    })
    t2 = Task({
        'Christine': [
            'leader', 5, 5, 5
        ],
        'Stephen': [
            'participant', 5, 5, 5
        ]
    })
    dataAggregator = ProjectDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    dataAggregator.add(e1)
    dataAggregator.add(e2)
    dataAggregator.add(t1)
    dataAggregator.add(t2)
    convertor = ProjectConverter(dataAggregator)
    reportgenerator = ProjectReportGenerator(convertor)
    reportgenerator.generate('Tim', 'report.xls')

def EEDemo():
    pass


def projectDemo():
    m1 = Meeting({
        'Harry': [
            'host', 1, 2, 5
        ],
        'Jane': [
            'participant', 4, 5, 3
        ]
    })
    m2 = Meeting({
        'Jane': [
            'host', 3, 3, 2
        ],
        'Harry': [
            'participant', 1, 2, 3
        ],
        'Billy': [
            'participant', 5, 5, 5
        ],
    })
    e1 = Expenditure({
        'Hank': [
            'spender', True, False
        ]
    })
    e2 = Expenditure({
        'Billy': [
            'spender', False, True 
        ]
    })
    t1 = Task({
        'Sean': [
            'leader', 5, 5, 5
        ],
        'Daniel': [
            'participant', 3, 3, 2
        ],
        'Eric': [
            'participant', 4, 4, 5
        ]
    })
    t2 = Task({
        'Joe': [
            'leader', 4, 3, 2
        ],
        'Daniel': [
            'participant', 2, 3, 4
        ],
        'Hank': [
            'participant', 3, 3, 3
        ]
    })
    g1 = GitRecord({
        'Eric': [
            'committer', True, 5
        ],
        'Joe': [
            'committer', True, 4
        ]
    })
    dataAggregator = ProjectDataAggregator()
    dataAggregator.add(m1)
    dataAggregator.add(m2)
    dataAggregator.add(e1)
    dataAggregator.add(e2)
    dataAggregator.add(t1)
    dataAggregator.add(t2)
    convertor = ProjectConverter(dataAggregator)
    reportgenerator = ProjectReportGenerator(convertor)
    reportgenerator.generate('Harry', 'report.xls')


if __name__ == '__main__':
    churchDemo()
    projectDemo()
