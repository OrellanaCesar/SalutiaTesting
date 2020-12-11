from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from Models.TestCaseRuns import *
from .Login_correcto import Login

class Logout():
    def __init__(self):
        self.l = Login()


    def logout_admin(self):
        inputs = ['user:admin, pass:1234']
        browser = self.l.loginAdmin(True)
        values_obteined = []
        logout = browser.find_element_by_id('logout')
        logout.click()
        time.sleep(2)
        values_obteined.append(browser.find_element_by_id('salutia-login').text)
        values_obteined.append(browser.find_element_by_id('form-login').text)
        values_expected = ['SALUTIA', 'Ingrese al Sitio']

        if self.l.equalsValues(values_obteined,values_expected):
            result = 'Correcto'
        else:
            result = 'Error'

        test = CasoPrubaRun()
        test.insert(inputs,
                    values_expected,
                    values_obteined,
                    result,
                    "Usuarios",
                    "Logout Administrador",
                    "El usuairo administrador sale del Sistema",
                    "Modulo de Gestion Usuarios")

        browser.close()


    def logout_Secretario(self):
        inputs = "user:mcardozo; password:1234"
        self.l.reset()
        browser = self.l.loginSecretario(True)
        values_obteined = []
        logout = browser.find_element_by_id('logout')
        logout.click()
        time.sleep(2)
        values_obteined.append(browser.find_element_by_id('salutia-login').text)
        values_obteined.append(browser.find_element_by_id('form-login').text)
        values_expected = ['SALUTIA', 'Ingrese al Sitio']

        if self.l.equalsValues(values_obteined, values_expected):
            result = 'Correcto'
        else:
            result = 'Error'

        test = CasoPrubaRun()
        test.insert(inputs,
                    values_expected,
                    values_obteined,
                    result,
                    "Usuarios",
                    "Logout Secretario",
                    "El usuairo Secretario sale del Sistema",
                    "Modulo de Gestion Usuarios")

        browser.close()


    def logout_Profesional(self):
        inputs =  "user:palomoadriana; password:1234"
        self.l.reset()
        browser = self.l.loginProfesional(True)
        values_obteined = []
        logout = browser.find_element_by_id('logout')
        logout.click()
        time.sleep(2)
        values_obteined.append(browser.find_element_by_id('salutia-login').text)
        values_obteined.append(browser.find_element_by_id('form-login').text)
        values_expected = ['SALUTIA', 'Ingrese al Sitio']

        if self.l.equalsValues(values_obteined, values_expected):
            result = 'Correcto'
        else:
            result = 'Error'

        test = CasoPrubaRun()
        test.insert(inputs,
                    values_expected,
                    values_obteined,
                    result,
                    "Usuarios",
                    "Logout Profesional",
                    "El usuairo Profesional sale del Sistema",
                    "Modulo de Gestion Usuarios")

        browser.close()


