from Conection.DataBase import *

_base = base
_db = db


class Modulos():
    """ This Class registers, lowers and modifies a module """

    def __init__(self):
        """Instantiate the session with the database to work"""

        Session = sessionmaker(db)
        self.session = Session()

    def insert(self, nameModules, descriptionModules):
        """ Register a new module"""

        module = Modules(module_name=nameModules, module_description=descriptionModules)
        self.session.add(module)
        self.session.commit()
        print("Inserted Module")

    def deleteID(self, idModule):
        """ Delete a module using Id"""

        m = self.session.query(Modules).get(idModule)
        self.session.delete(m)
        self.session.commit()
        print("Deleted Module")

    def deleteObject(self, module):
        """ Delete a module passing a object"""

        self.session.delete(module)
        self.session.commit()
        print("Deleted Module")

    def SearchModuleName(self, nameModule):
        """Search a module using the module name"""

        result = self.session.query(Modules).filter(Modules.module_name == nameModule).first()
        return result

    def SearchModuleId(self, idModule):
        """Search a module using the module id"""

        result = self.session.query(Modules).filter(Modules.id == idModule).first()
        return result