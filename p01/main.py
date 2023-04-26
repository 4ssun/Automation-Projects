from selenium import webdriver

def Driver():
    driver = webdriver.Chrome(executable_path="D:\\Python\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.arguments("disable-infobars")
    options.arguments("start-maximized")
    options.arguments("disable-dev-shm-usage")  #impede erros em máquinas linux!
    options.arguments("no-sandbox")  #para maiores privilégios de execução.

def main():
    driver = Driver()
    element = driver.find_element(By. XPATH, "//*[@id="singlePageArticle"]/div[1]/div/div/div[2]/section/div/div/div/div/div/div/p[2]/span")