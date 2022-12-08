import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos_df = pd.read_excel(r"C:\Users\rafae\OneDrive\PhytonAulas\AulasHashtag - windows\Automacao Web(Web-Scraping)\enviar_mensagem_whatsapp\Enviar.xlsx")
print(contatos_df)

# navegador = webdriver.Chrome()
# navegador.get("https://web.whatsapp.com/")

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\rafae\AppData\Local\Google\Chrome\User Data\Profile Selenium')
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")

while len(driver.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    driver.get(link)
    while len(driver.find_element(By.ID,'side')) < 1:
        time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
