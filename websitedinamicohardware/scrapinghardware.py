import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

# Caminho do chromedriver — corrigido com raw string
chrome_driver_path = r"C:\Program Files\chromedriver-win64\chromedriver.exe"


# Configuração do WebDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")


# Inicialização do WebDriver
driver = webdriver.Chrome(service=service, options=options)

# URL inicial
url_site = "https://www.kabum.com.br/promocao/HARDWAREKABUM"
driver.get(url_site)
time.sleep(5)

# Dicionário para armazenar os dados
dic_produtos = {"marca": [], "preco": []}

# Página inicial
pagina = 1

while True:
    print(f"\nColetando dados da página {pagina}...")

    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "productCard"))
        )
        print("Elementos encontrados com sucesso")
    except TimeoutException:
        print("Tempo de espera excedido ao buscar produtos")
        break

    # Coleta dos produtos
    produtos = driver.find_elements(By.CLASS_NAME, "productCard")

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, "nameCard").text.strip()
            preco = produto.find_element(By.CLASS_NAME, "priceCard").text.strip()

            print(f"{nome} - {preco}")

            dic_produtos["marca"].append(nome)
            dic_produtos["preco"].append(preco)
        except Exception as e:
            print("Erro ao coletar dados de um produto:", e)

    # Tentativa de clicar no botão "Próxima Página"
    try:
        botao_proximo = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "nextLink"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", botao_proximo)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", botao_proximo)
        print(f"Indo para a página {pagina + 1}...")
        pagina += 1
        time.sleep(5)
    except Exception as e:
        print("Não há mais páginas ou erro ao avançar:", e)
        break

# Fechar navegador
driver.quit()

# Salvar os dados em um DataFrame
df = pd.DataFrame(dic_produtos)

# Exportar para Excel
df.to_excel("hardware.xlsx", index=False)
print(f"\nArquivo 'hardware.xlsx' salvo com sucesso. ({len(df)} produtos capturados)")