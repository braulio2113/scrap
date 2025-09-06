"""
! RECOMENDACIÓN: Usar IP dedicada porque el sitío suele bloquear después de cierto número de requerimentos    
"""

import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

#* Todos los ajustes para el driver de selenium
opts = Options()
opts.add_argument("start-maximized")
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
prefs = {'profile.managed_default_content_settings.images': 2}
opts.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
opts.add_argument("--disable-search-engine-choice-screen")
install_path = # path for install the driver
cache_manager = DriverCacheManager(install_path)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
    options=opts
)

url = 'https://www.inmuebles24.com/inmuebles-en-renta-en-ciudad-de-mexico.htmll'
driver.get(url)

soup = bs(driver.page_source, 'lxml')
driver.close()

inmuebles = soup.find_all(attrs={"data-qa": "posting PROPERTY"})

df = []
x = 0
for inmueble in inmuebles:
    precio = inmueble.find(attrs={"data-qa": "POSTING_CARD_PRICE"}).text
    precio = precio.replace('MN', '').strip()
    
    mantenimiento = inmueble.find(attrs={"data-qa": "expensas"}).text
    mantenimiento = mantenimiento.replace('MN', '').replace('Mantenimiento', '').strip()
    if len(mantenimiento) == 0: #* Esto es por si no aparece el costo de mantenimiento
        mantenimiento = 'Costo mantenimiento N/D'
    
    calle = inmueble.select('[class*="location-address"]')[0].text
    
    #* Colonia y municipio estan en una misma línea de texto
    col_mun = inmueble.find(attrs={"data-qa": "POSTING_CARD_LOCATION"}).text
    col_mun = col_mun.split(', ')
    colonia = col_mun[0]
    municipio = col_mun[1]
    
    #* No siempre estan disponibles las caracteristicas entonces por default se pone que ninguna esta disponible
    caracteristicas = inmueble.find('h3', attrs={"data-qa": "POSTING_CARD_FEATURES"}).find_all('span')
    superficie = 'Superficie N/D'
    recamaras = 'Recamaras N/D'
    baños = 'Baños N/D'
    estacionamiento = 'Estacionamiento N/D'
    for carac in caracteristicas:
        if 'm² tot' in carac.text:
            superficie = carac.text.replace('m² tot.', '').strip()
        elif 'rec' in carac.text:
            recamaras = carac.text.replace('rec.', '').strip()
        elif 'baño' in carac.text:
            baños = carac.text.replace('baños', '').replace('baño', '').strip()
        elif 'estac' in carac.text:
            estacionamiento = carac.text.replace('estac.', '').strip()
    
    link = inmueble.find('h3', attrs={"data-qa": "POSTING_CARD_DESCRIPTION"}).find('a').get('href')
    link = f'https://www.inmuebles24.com{link}'
    
    # descripcion = inmueble.find('h3', attrs={"data-qa": "POSTING_CARD_DESCRIPTION"}).find('a').text
    
    #* Se guarda en un DataFrame
    df_inmueble = pd.DataFrame()
    df_inmueble['Precio'] = pd.DataFrame([precio])
    df_inmueble['Mantenimiento'] = pd.DataFrame([mantenimiento])
    df_inmueble['Calle'] = pd.DataFrame([calle])
    df_inmueble['Colonia'] = pd.DataFrame([colonia])
    df_inmueble['Municipio o Alcaldía'] = pd.DataFrame([municipio])
    df_inmueble['Superficie'] = pd.DataFrame([superficie])
    df_inmueble['Recamara'] = pd.DataFrame([recamaras])
    df_inmueble['Baños'] = pd.DataFrame([baños])
    df_inmueble['Lugares de estac.'] = pd.DataFrame([estacionamiento])
    df_inmueble['Link'] = pd.DataFrame([link])
    # df_inmueble['Descripción'] = pd.DataFrame([descripcion])
    
    df.append(df_inmueble)
    
    x += 1
    print(f'{x}/{len(inmuebles)}')
    print(precio)
    print(mantenimiento)
    print(calle)
    print(colonia)
    print(municipio)
    print(superficie)
    print(recamaras)
    print(baños)
    print(estacionamiento)
    print(link)
    # print(descripcion)

df = pd.concat(df)
df.to_csv(f'Inmuebles24.csv', header=True, index=False)

