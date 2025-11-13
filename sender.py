#from whatsapp_api_client_python import API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import smtplib
from email.message import EmailMessage
import getpass

import time

class sender:

    def __init__(self):
        #self.direcoty = directory

        options = Options()
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument("--start-maximized")

        # service = Service("/usr/bin/chromedriver")
        # driver = webdriver.Chrome(service=service, options=options)

    
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="141.0.7390.108").install()), options=options)
        
        # self.driver.get("https://web.whatsapp.com")

        # try:
        #     WebDriverWait(self.driver, 300).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='grid']")))
        #     print("✅ Sesión iniciada correctamente.")
        # except:
        #     print("⏰ Tiempo de espera agotado. No se detectó el inicio de sesión.")
        #     self.driver.quit()
        #     exit()

        #print(self.driver.title)

        #driver.quit()



    def send_Message():
        pass



class WA_sender(sender):

    def __init__(self):
        super().__init__()

        self.driver.get("https://web.whatsapp.com")

        try:
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='grid']")))
            print("✅ Sesión iniciada correctamente.")
        except:
            print("⏰ Tiempo de espera agotado. No se detectó el inicio de sesión.")
            self.driver.quit()
            exit()


    def send_Message(self, directory:dict):
        mensaje = "Hola!"
        
        for contacto in directory:

            #contacto = "Diego Núñez"
            
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']")))
            
            search_box.click()
            search_box.send_keys(directory[contacto])
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)

            # añade archivo
            msg_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")))
            
            msg_box.click()
            msg_box.send_keys(mensaje)
            msg_box.send_keys(Keys.ENTER)

            print(f"✅ Mensaje enviado a {contacto}.")
            time.sleep(3)

        
        # cierra sesión
        

        self.driver.quit()


class email_sender(sender):
    
    def __init__(self):
        super().__init__()


    def send_Message(self, directory:dict, subject, remitente):
        msg = EmailMessage()


        for contacto in directory:

            msg['Subject'] = subject
            msg['From'] = remitente
            msg['To'] = contacto


        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        



if __name__ == "__main__":

    test = WA_sender()
    test.send_Message()

    test = email_sender()
    test.send_Message()
    print("hola")
    