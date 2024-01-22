from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_files

class Login():
    def __init__(self):
        
        
        service = Service(executable_path=test_files.SysVars.web_driver_path)

        url="http://localhost:4200/"

        #from selenium.webdriver.chrome.options import Options

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get(url=url)
            driver.maximize_window()

        #################### LOGIN ####################

            login_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-input-0")))
            login_input.clear
            login_input.send_keys(test_files.Credentials.username)
            login_password = driver.find_element("id","mat-input-1")
            login_password.clear
            login_password.send_keys(test_files.Credentials.password)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-login/mat-card/mat-card-content/form/button"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/div/div[2]/div[3]/a/mat-icon"))).click()
        except Exception as ex:
            print(ex)
            print("-----")
            print(str(ex))
            print("-----")
            print(ex.args)
            print("=====")
        finally:
            driver.close()
            driver.quit()


