from Conection.DataBase import *
from .Modules import Modulos

_base = base
_db = db


class CasoPruba(object):
    """docstring for CasoPruba"""

    def __init__(self):
        """Instantiate the session with the database to work"""

        Session = sessionmaker(db)
        self.session = Session()
        self.module = Modulos()

    def insert(self, CaseName, CaseDescription, ModulesId):
        """ Register a new case test"""

        caseTest = CaseTest(casetest_name=CaseName,
                            casetest_description=CaseDescription,
                            modules_id=ModulesId,
                            casetest_count_runs=0,
                            casetest_successful=0)

        self.session.add(caseTest)
        self.session.commit()
        print("Case Test Inserted")

    def deleteId(self, idCase):
        """ Delete a case test using Id"""

        c = self.session.query(CaseTest).get(idCase)
        self.session.delete(c)
        self.session.commit()
        print("Deleted Case Test")

    def deleteObject(self, ObjectCaseTest):
        """ Delete a case test passing a object """

        self.session.delete(ObjectCaseTest)
        self.session.commit()
        print("Deleted Case Test")

    def SearchCaseTestName(self, CaseName):
        """Search Case Test by name"""

        c = self.session.query(CaseTest).filter(CaseTest.casetest_name == CaseName).first()
        return c

    def SearchCaseTestId(self, CaseId):
        """Search Case Test by ID"""

        c = self.session.query(CaseTest).filter(CaseTest.id == CaseId).first()
        return c

    def UpdateCount(self, idCaseTest):
        """ Increase number of runs """

        c = self.SearchCaseTestId(idCaseTest)
        c.casetest_count_runs += 1
        self.session.commit()

    def UpdateSuccessful(self, idCaseTest):
        """ Increase number of runs """

        c = self.SearchCaseTestId(idCaseTest)
        c.casetest_successful += 1
        self.session.commit()
