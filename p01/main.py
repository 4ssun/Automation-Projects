from selenium import webdriver

def webscraping():
    driver = webdriver.Chrome(executable_path="D:\\Python\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.arguments("disable-infobars")
    options.arguments("start-maximized")
    options.arguments("disable-dev-shm-usage")  #impede erros em máquinas linux!
    options.arguments("no-sandbox")  #para maiores privilégios de execução.