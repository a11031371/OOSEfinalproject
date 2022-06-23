import xlwt
from base.reportgenerator import ReportGenerator


class ProjectReportGenerator(ReportGenerator):

    def generate(self, person: str, filePath: str) -> bool:
        book = xlwt.Workbook(encoding="utf-8")
        individualScore = self._convertor.getIndividualScore(person)
        groupScore = self._convertor.getGroupScore(person)

        personalSheet = book.add_sheet('Personal score', cell_overwrite_ok=True)
        # Write personal sheet column name
        personalSheet.write(0, 0, 'Name')
        personalSheet.write(0, 1, 'Score')

        # Write personal sheet content
        personalSheet.write(1, 0, person)
        personalSheet.write(1, 1, str(individualScore))

        groupSheet = book.add_sheet('Group score', cell_overwrite_ok=True)
        # Write group sheet column name
        groupSheet.write(0, 0, 'Name')
        groupSheet.write(0, 1, 'Score')

        # Write group sheet content

        for i, p in enumerate(groupScore):
            groupSheet.write(i + 1, 0, p)
            groupSheet.write(i + 1, 1, groupScore[p])
            i += 1

        book.save(filePath)
