from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from Models.TestCaseRuns import *


class Login_inc():
    def __init__(self):
        print("inicio Test")
        self.browser = webdriver.Chrome(
            executable_path=r'C:\Users\LENOVO\Documents\Unsa\Seminario\Selenium\chromedriver.exe')
        self.browser.get("http://localhost/Seminario/Code/index.php/login")

        time.sleep(3)
        self.username = self.browser.find_element_by_id("form-username")
        self.password = self.browser.find_element_by_id("form-password")
        self.submit = self.browser.find_element_by_name("submit")


    def login(self):
        inputs = "user:test; password:test"
        print("login incorrecto")
        self.username.send_keys("test")
        time.sleep(1)
        self.password.send_keys("test")
        time.sleep(1)
        self.submit.click()
        wait = self.browser.implicitly_wait(3)  # seconds
        values_obteined = []
        values_obteined.append(self.browser.find_element_by_id('msj').text)
        values_expected = [u'El usuario/contraseña son incorrectos']
        if self.equalvalues(values_obteined, values_expected):
            result = 'Correcto'
        else:
            result = 'Error'

        test = CasoPrubaRun()

        test.insert(inputs,
                    values_obteined,
                    values_expected,
                    result,
                    "Usuarios",
                    "Login incorrecto ",
                    "Se intenta loguear un usuario con datos incorrectos y deberia mostrar un mensaje de error",
                    "Modulo de Gestion Usuarios")

        self.browser.close()




    def equalvalues(self,values_obteined,values):
        b = True
        i = 0
        while b and i < len(values_obteined):
            if values_obteined[i] != values[i]:
                b = False
            else:
                i = i + 1

        return b


