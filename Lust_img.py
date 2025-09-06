import requests
from PIL import Image, ImageFile
import io
from time import sleep
import random
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

#* Todos los ajustes para el driver de selenium
opts = Options()
opts.add_argument("start-maximized")
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    )
# prefs = {'profile.managed_default_content_settings.images': 2}
opts.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
opts.add_argument("--disable-search-engine-choice-screen")
install_path = # path for install the driver
cache_manager=DriverCacheManager(install_path)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
    options=opts
    )

url = 'https://lustmexico.com/collections/new-arrivals'
driver.get(url)

#* Hay una ventana que a veces aparece
sleep(random.uniform(5.0, 10.0))
try:
    button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/div/div/div[1]/button')
    button.click()
except:
    pass

anuncios = driver.find_elements('xpath', '//div[@class="card-wrapper"]')
i = 0
for anuncio in anuncios:
    i += 1
    modelo = anuncio.find_element('xpath', './/a[@class="card-information__text h4"]').text
    precio = anuncio.find_element('xpath', './/price-money/bdi').get_attribute("innerHTML").splitlines()[0]
    precio = re.split(r"[><]", precio)[4] #* 
    print(modelo)
    print(precio)
    
    #* Si una imagén no se puede descargar se marca el error y continua
    try:
        url_imagen = anuncio.find_element('xpath', './/img')
        url_imagen = url_imagen.get_attribute('src')
        image_content = requests.get(url_imagen, headers=headers).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = './imagenes/'+ str(i) + '.jpg'  # nombre a guardar de la imagen
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
    except Exception as e:
        print(e)
        print ("Error")

driver.close()