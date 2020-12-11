from selenium import webdriver
import time
from Models.TestCaseRuns import *


class Login(object):

    def __init__(self):
        print("inicio Test")
        self.browser = webdriver.Chrome(
            executable_path=r'C:\Users\LENOVO\Documents\Unsa\Seminario\Selenium\chromedriver.exe')
        self.browser.get("http://localhost/Seminario/Code/index.php/login")

        time.sleep(3)
        self.username = self.browser.find_element_by_id("form-username")
        self.password = self.browser.find_element_by_id("form-password")
        self.submit = self.browser.find_element_by_name("submit")


    def reset(self):
        print("inicio Test")
        self.browser = webdriver.Chrome(
            executable_path=r'C:\Users\LENOVO\Documents\Unsa\Seminario\Selenium\chromedriver.exe')
        self.browser.get("http://localhost/Seminario/Code/index.php/login")

        time.sleep(3)
        self.username = self.browser.find_element_by_id("form-username")
        self.password = self.browser.find_element_by_id("form-password")
        self.submit = self.browser.find_element_by_name("submit")


    def loginAdmin(self, useLogin):
        inputs = "user:admin; password:1234"
        print("login admin")
        self.username.send_keys("admin")
        time.sleep(1)
        self.password.send_keys("1234")
        time.sleep(1)
        self.submit.click()
        wait = self.browser.implicitly_wait(5)  # seconds
        values_obteined = []
        values_obteined.append(self.browser.find_element_by_name('titulo-Paciente').text)
        config = self.browser.find_elements_by_id('menu-config')
        for x in config:
            values_obteined.append(x.text)
        usuarios = self.browser.find_elements_by_id('menu-usuarios')
        for x in usuarios:
            values_obteined.append(x.text)
        values_expected = ['Datos de Pacientes', u'Configuración', 'Usuarios']
        test = CasoPrubaRun()
        if self.equalsValues(values_obteined,values_expected):
            result = "Correcto"
        else:
            result = "Error"
        test.insert(inputs,
                    values_obteined,
                    values_expected,
                    result,
                    "Usuarios",
                    "Login Correcto Admin",
                    "Se loguea un usuario con perfil admin correctamente",
                    "Modulo de Gestion Usuarios")


        print("fin login admin")
        if useLogin:
            return self.browser
        else:
            self.browser.close()


    def loginSecretario(self, useLogin):
        inputs = "user:mcardozo; password:1234"
        print("login Secretario")
        self.username.send_keys("mcardozo")
        time.sleep(1)
        self.password.send_keys("1234")
        time.sleep(1)
        self.submit.click()
        wait = self.browser.implicitly_wait(5)  # seconds
        values_obteined = []
        values_obteined.append(self.browser.find_element_by_name('titulo-Paciente').text)
        config = self.browser.find_elements_by_id('menu-config')
        if len(config) == 0:
            values_obteined.append('')
        usuarios = self.browser.find_elements_by_id('menu-usuarios')
        if len(usuarios) == 0:
            values_obteined.append('')
        values_expected = ['Datos de Pacientes', '', '']
        test = CasoPrubaRun()
        if self.equalsValues(values_obteined, values_expected):
            result = "Correcto"
        else:
            result = "Error"
        test.insert(inputs,
                    values_expected,
                    values_obteined,
                    result,
                    "Usuarios",
                    "Login Correcto Secretario",
                    "Se loguea un usuario con perfil Secretario correctamente",
                    "Modulo de Gestion Usuarios")


        print("fin login secretario")
        if useLogin:
            return self.browser
        else:
            self.browser.close()


    def loginProfesional(self, useLogin):
        inputs = "user:palomoadriana; password:1234"
        print("login Profesional")
        self.username.send_keys("palomoadriana")
        time.sleep(1)
        self.password.send_keys("1234")
        time.sleep(1)
        self.submit.click()
        wait = self.browser.implicitly_wait(5)  # seconds
        values_obteined = []
        agenda = self.browser.find_elements_by_id('menu-agenda')
        for x in agenda:
            values_obteined.append(x.text)

        values_expected = ['Agenda']
        test = CasoPrubaRun()
        if self.equalsValues(values_obteined, values_expected):
            result = "Correcto"
        else:
            result = "Error"
        test.insert(inputs,
                    values_expected,
                    values_obteined,
                    result,
                    "Usuarios",
                    "Login Correcto Profesional",
                    "Se loguea un usuario con perfil Profesional correctamente",
                    "Modulo de Gestion Usuarios")


        print("fin login profesional")
        if useLogin:
            return self.browser
        else:
            self.browser.close()


    def equalsValues(self, values_obteined, values_expected):
        b = True
        i = 0
        while b and i < len(values_obteined):
            if values_obteined[i] != values_expected[i]:
                b = False
            else:
                i = i + 1

        return b


