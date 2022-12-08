4import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos_df = pd.read_excel(r"....\Enviar.xlsx") #colocar caminho
print(contatos_df)

# navegador = webdriver.Chrome()
# navegador.get("https://web.whatsapp.com/")4

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\rafae\AppData\Local\Google\Chrome\User Data\Profile Selenium') #arrumar caminho
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")

while len(driver.find_elements(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    driver.get(link)
    try:
        while len(driver.find_elements(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')) < 1:
            time.sleep(1)
    except:
        pass

    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
