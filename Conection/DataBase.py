from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_string = "postgresql://postgres:orellana@localhost:5432/salutia_testing"

db = create_engine(db_string)
base = declarative_base()


class Modules(base):
    """docstring for Modulos"""

    __tablename__ = 'modules'

    id = Column(Integer, Sequence('modulos_id_seq'), primary_key=True)
    module_name = Column(String)
    module_description = Column(String)
    casetest = relationship("CaseTest", order_by="CaseTest.id", back_populates="modules")

    def __repr__(self):
        return "{}".format(self.module_name)


class CaseTest(base):
    __tablename__ = 'casetest'

    id = Column(Integer, Sequence('casetest_id_seq'), primary_key=True)
    casetest_name = Column(String)
    casetest_description = Column(String)
    casetest_count_runs = Column(Integer)
    casetest_successful = Column(Integer)
    modules_id = Column(Integer, ForeignKey('modules.id'))

    modules = relationship("Modules", back_populates="casetest")
    casetestrun = relationship("CaseTestRun", order_by="CaseTestRun.casetestrun_date", back_populates="casetest")

    def __repr__(self):
        return "{} {} {}".format(self.casetest_name, self.casetest_count_runs, self.casetest_count_runs)


class CaseTestRun(base):
    __tablename__ = 'casetestrun'

    id = Column(Integer, Sequence('casetestrun_id_seq'), primary_key=True)
    casetestrun_date = Column(DateTime)
    casetestrun_values_input = Column(String)
    casetestrun_expected = Column(String)
    casetestrun_obteained = Column(String)
    casetestrun_result = Column(String)
    casetest_id = Column(Integer, ForeignKey('casetest.id'))

    casetest = relationship("CaseTest", back_populates="casetestrun")

    def __repr__(self):
        return "{} {} {}".format(self.casetest_id, self.casetestrun_date, self.casetestrun_result)


# Session = sessionmaker(db)
# session = Session()
# base.metadata.create_all(db)

