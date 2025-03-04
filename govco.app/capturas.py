from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tldextract
import time

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")

def obtener_captura(url):
    driver = webdriver.Chrome(options=chrome_options)
    extracted = tldextract.extract(url)
    driver.get(url)

    # Espera en segundos para que la pagina cargue completamente
    wait = WebDriverWait(driver, 3) 
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    #Se obtienen las dimensiones de la pagina web completa
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    print("Sitio:", url + ", " + str(total_width) + " x " + str(total_height))

    driver.set_window_size(1920, total_height)
    time.sleep(1)

    with open("capturas\\" + extracted.domain + ".png", "wb") as file:
        file.write(driver.get_screenshot_as_png())

    driver.quit()
