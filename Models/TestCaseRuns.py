
from .TestCase import CasoPruba
from Conection.DataBase import *
from datetime import datetime




_base = base
_db = db


class CasoPrubaRun():
    """docstring for CasoPrubaRun"""

    def __init__(self):
        """Instantiate the session with the database to work"""
        Session = sessionmaker(db)
        self.session = Session()
        self.CaseTest = CasoPruba()

    def insert(self, TestRun_Inputs, Expected, Obtained, Result, ModuleName, CaseTestName, CaseTestDes=" ",
               ModuleDes=" "):
        test = self.CaseTest.SearchCaseTestName(CaseTestName)
        module = self.CaseTest.module.SearchModuleName(ModuleName)
        if module == None:
            self.CaseTest.module.insert(ModuleName, ModuleDes)
        if test == None:
            m = self.CaseTest.module.SearchModuleName(ModuleName)
            self.CaseTest.insert(CaseTestName, CaseTestDes, m.id)

        CT = self.CaseTest.SearchCaseTestName(CaseTestName)
        caseTestR = CaseTestRun(casetestrun_date=datetime.now(),
                                casetestrun_values_input=TestRun_Inputs,
                                casetestrun_expected=Expected,
                                casetestrun_obteained=Obtained,
                                casetestrun_result=Result,
                                casetest_id=CT.id)

        self.session.add(caseTestR)
        self.session.commit()
        self.CaseTest.UpdateCount(CT.id)
        if Result == 'Correcto':
            self.CaseTest.UpdateSuccessful(CT.id)
        print("Case Test Run Inserted")




