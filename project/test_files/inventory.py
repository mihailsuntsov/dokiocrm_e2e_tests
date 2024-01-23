from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import test_files

class Inventory():

    def __init__(self):
        
        service = Service(executable_path=test_files.SysVars.web_driver_path)

        url="http://localhost:4200/"

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
            sleep(3)

            #################### Inventory ####################

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "goods"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inventory"))).click()

            # Click button "Create document"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-title/div[2]/a/button"))).click()
            sleep(3)
            
            # Open and save settings
            driver.find_element(By.ID, 'settings_btn').click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'save_user_settings_btn' ))).click()
                                                                                
            # Document status selection
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//mat-select[@formcontrolname="status_id"]' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span' ))).click() 

            # Product search and selection
            product_search=driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/mat-card-content/div[1]/div/div[2]/div/div/div/div[1]/mat-form-field[2]/div/div[1]/div[1]/input' )
            product_search.click()
            product_search.send_keys("товар")
            sleep(2)
            
            # Set amount, price and select this product
            product_amount=driver.find_element(By.XPATH, '            /html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/mat-card-content/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[2]/mat-form-field/div/div[1]/div[1]/input' )
            product_price=driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/mat-card-content/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[3]/mat-form-field/div/div[1]/div[1]/input')   
            product_amount.click()
            for i in range(4):
                product_amount.send_keys(Keys.BACKSPACE)
            product_amount.send_keys(1)
            product_price.click()
            for i in range(4):
                product_price.send_keys(Keys.BACKSPACE)
            product_price.send_keys(100)
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/div/div[2]/button[3]' ).click()            
            
            # Create document
            driver.find_element(By.ID, 'newdoc_btn').click()
            sleep(3) 

            # Delete product from products table
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/mat-card-content/div[2]/div/table/thead/tr/th[7]/mat-icon' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/deletedialog/div/div[2]/button[1]' ))).click()
            
            # Save document
            driver.find_element(By.ID, 'save_btn').click()
            sleep(3)
            
            # Product selection from pop-up window
                
                # Open product selection pop-up window
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/div/div[2]/button[1]').click()
            sleep(2)
            
                # category search
            category_search=driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/div/div/form/mat-form-field/div/div[1]/div[1]/input' )
            category_search.clear()
            category_search.send_keys("товары")
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/div/div/form/mat-form-field/div/div[1]/div[2]/button' ).click()
            sleep(2)
                
                # list of products in category
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/mat-tree/mat-tree-node/span' ))).click()
            sleep(2)
                
                # selected product
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer-content/div/mat-card/mat-card-content/div/div/div/table/tbody/tr/td[1]/mat-icon' ))).click()
                
                # close dialog after selection
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-card-title/button[1]').click()
            
            # Save document
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'save_btn' ))).click()


            # Delete product from products table
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/mat-card-content/div[2]/div/table/thead/tr/th[7]/mat-icon' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/deletedialog/div/div[2]/button[1]' ))).click()
            
            # Save document
            driver.find_element(By.ID, 'save_btn').click()
            sleep(3)



            # Category selection from pop-up window
                
                # Open product selection pop-up window
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/div/div[2]/div/app-inventory-products-table/div/div/div/form/mat-card/div/div[2]/button[2]').click()
            sleep(2)
            
                # category search
            category_search=driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/div/div/form/mat-form-field/div/div[1]/div[1]/input' )
            category_search.clear()
            category_search.send_keys("товары")
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/div/div/form/mat-form-field/div/div[1]/div[2]/button' ).click()
            sleep(2)
                
            
                
                # selected category
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-drawer-container/mat-drawer/div/mat-tree/mat-tree-node/button[2]/span[1]/mat-icon' ))).click()
                
                # close dialog after selection
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-product-categories-select/mat-card/mat-card-title/button[1]').click()
            
            # Save document
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'save_btn' ))).click()



            
           
            # Complete and uncomplete document
            driver.find_element(By.ID, 'complete_btn').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/deletedialog/div/div[2]/button[1]' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'completed_btn' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/deletedialog/div/div[2]/button[1]' ))).click()
            sleep(2)    

            # Files adding
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[2]').click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[3]').click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/div/mat-tab-body[3]/div/div/div/div/mat-card/mat-card-content/div[2]/div/button').click()
            sleep(5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-files/mat-drawer-container/mat-drawer-content/div/mat-card/mat-card-content/div/div/div/div[1]/div[6]/mat-card/mat-card-content/p/mat-checkbox' ))).click() 
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/app-files/mat-drawer-container/mat-drawer-content/div/mat-card/mat-card-title/div/button[4]' ))).click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[4]').click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory-doc/mat-card/form/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[1]').click()                                
            sleep(1)  
            
            # Exit to menu
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'cancel_btn'))).click() 
            sleep(2)
            
                #################### Menu of Customer's inventory ####################
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/button[2]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/ul/li/mat-checkbox"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div/button"))).click()
            sleep(3)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/button[2]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[1]/ul/li/mat-checkbox"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div/button"))).click()
            sleep(3)

            # Search
            
            search_field=driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/div/mat-form-field/div/div[1]/div[1]/input' )
            search_field.clear()
            search_field.send_keys("поста")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/div/mat-form-field/div/div[1]/div[2]/button"))).click()
            sleep(2)
            search_field=driver.find_element(By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/div/mat-form-field/div/div[1]/div[1]/input' )
            search_field.click()
            for i in range(5):
                search_field.send_keys(Keys.BACKSPACE)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/div/mat-form-field/div/div[1]/div[2]/button"))).click()
            sleep(2)
            

            # Rows in table

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/mat-form-field[1]/div/div[1]/div/mat-select' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/mat-option[3]' ))).click()                                                       
            sleep(2)

            # Departments

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/mat-form-field[3]/div/div[1]/div/mat-select' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/mat-option[1]' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/mat-form-field[3]/div/div[1]/div/mat-select' ))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/mat-option[2]' ))).click()
            sleep(2)

            # Refresh button

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/form/div[2]/button[1]' ))).click()
            sleep(2)

            # Settings

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-title/button' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'save_user_settings_btn' ))).click()
            sleep(2)

            # Columns

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[3]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[4]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[5]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[6]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[7]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[8]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[9]/span' ))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-ui/div/section/app-inventory/mat-card/mat-card-content/div/div/div/table/thead/tr/th[10]/span' ))).click()
            sleep(3)
            
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