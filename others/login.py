#%%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def Driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")  #impede erros em máquinas linux!
    options.add_argument("no-sandbox")  #para maiores privilégios de execução.
    driver = webdriver.Chrome(executable_path="D:\\Python\\chromedriver.exe", options=options)
    driver.get("")  #site pra login
    return driver
#%%
def main():
    email = "" #email for login
    password = ""  #password

    driver = Driver()
    login_bttn = driver.find_element(By. XPATH, "/html/body/header/div/div/div/a[2]").click()
    WebDriverWait(driver, 7)
    input_email = driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(email)
    continue_bttn = driver.find_element(By. XPATH, "//*[@id='identifierNext']/div/button/span").click()
    WebDriverWait(driver, 7)
    input_password = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(password)
    continue_bttn = driver.find_element(By. XPATH, "//*[@id='identifierNext']/div/button/span").click()
    WebDriverWait(driver, 7)

# XPATHS relacionados ao login no Gmail para exemplificação.
# %%
print(main())
# %%
