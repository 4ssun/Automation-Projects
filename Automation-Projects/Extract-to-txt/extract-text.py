#%% Importa bibliotecas necessárias e prepara o Driver a ser manipulado.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt
def Driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")  #impede erros em máquinas linux!
    options.add_argument("no-sandbox")  #para maiores privilégios de execução.
    driver = webdriver.Chrome(executable_path="D:\\Python\\chromedriver.exe", options=options)
    driver.get("https://www.browserstack.com/guide/web-scraping-using-selenium-python#:~:text=Web%20Scraping%20with%20Selenium%20allows%20you%20to%20gather,demonstrates%20how%20to%20do%20web%20scraping%20using%20Selenium.")
    return driver
#%%
def main():
    driver = Driver()
    item = driver.find_element(By. XPATH, "//*[@id='singlePageArticle']/div[1]/div/div/div[2]/section/div/div/div/div/div/div/p[2]/span")
    return item.text
def extrai_texto(texto):
    output =float(texto.split(":")[1])
    return output
def escreve_texto(texto):
    filename = f"{dt.now}.txt"
    with open(filename,'w') as file:
        file.write(texto)
# %%
print(main())
# %%
