import time
import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.kabum.com.br/promocao/HARDWAREKABUM")
time.sleep(10)

driver.maximize_window()
time.sleep(5)

id_do_produto = '520492', '338409'
try:
    
    elemento = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'id_do_produto'))
    )
    
    elemento.click()
except Exception as e:
    print(f"Erro ao clicar no elemento: {e}")
finally:

#produto_id = '520492'
#elemento = driver.find_element(By.ID, produto_id)
#elemento.click()
#time.sleep(10)


    driver.quit()


    df = pd.DataFrame()


    df.to_excel("hardware.xlsx", index=False)
    print(f"\nArquivo 'hardware.xlsx' salvo com sucesso. ({len(df)} produtos capturados)")