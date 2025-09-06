import sys
sys.path.insert(1, '..')
from selenium import webdriver 
import random
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import urllib
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

opts = Options()
opts.add_argument("start-maximized")
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
prefs = {'profile.managed_default_content_settings.images': 2}
opts.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
opts.add_argument("--disable-search-engine-choice-screen")
install_path = # path for install the driver
cache_manager=DriverCacheManager(install_path)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
    options=opts
)

def rating(element):
    try:
        player = pd.DataFrame([driver.find_element('xpath', element).text])
    except:
        player = '0'
    return player


def xpath_element(link):
    done = False
    while not done:
        try:
            element = driver.find_element('xpath', link)
            done = True
        except:
            sleep(random.uniform(5.0, 10.0))
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH, link))
            )
    return element

url = 'https://es.whoscored.com/matches/1821163/live/inglaterra-premier-league-2024-2025-tottenham-bournemouth'

while True:
    try:
        driver.get(url)
        break
    except:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@id="live-match"]'))
        )
        driver.refresh()
        continue
    
sleep(random.uniform(5.0, 10.0))
try:
    button = driver.find_element('xpath', '//*[text()="ACEPTO"]')
    button.click()
except:
    pass


try:
    button = driver.find_element(
        'xpath', '//button[@class="webpush-swal2-close"]')
    button.click()
    sleep(random.uniform(5.0, 10.0))
except:
    pass
try:
    button = driver.find_element('xpath', '//*[@id="bar"]/div[2]')
    button.click()
    sleep(random.uniform(5.0, 10.0))
except:
    pass

try:
    stadium = driver.find_element('xpath', '//*[@id="stadium"]/div[1]/div[2]/div[2]')
except:
    stadium = None
    
if stadium:
    sleep(random.uniform(5.0, 10.0))
    match = pd.DataFrame()
    # Match Center
    match['Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-header"]/div[1]/div[2]/a').text])
    match['Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-header"]/div[3]/div[2]/a').text])
    match['Rating_Home'] = rating(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[1]/div[1]/span[1]')
    match['Rating_Away'] = rating(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[1]/div[1]/span[3]')
    
    # Rating Home
    match['Rating_player1_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span')
    match['Rating_player2_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span')
    match['Rating_player3_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/span')
    match['Rating_player4_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/span')
    match['Rating_player5_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/span')
    match['Rating_player6_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[6]/div[1]/span')
    match['Rating_player7_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/span')
    match['Rating_player8_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/span')
    match['Rating_player9_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[9]/div[1]/span')
    match['Rating_player10_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[10]/div[1]/span')
    match['Rating_player11_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[1]/div[11]/div[1]/span')
    match['Rating_player12_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[1]/div[3]/div[1]/div[1]/span')
    match['Rating_player13_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[1]/div[3]/div[2]/div[1]/span')
    match['Rating_player14_Home'] = rating(
        '//*[@id="stadium"]/div[1]/div[1]/div[3]/div[3]/div[1]/span')

    # Away Rating
    match['Rating_player1_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span')
    match['Rating_player2_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/span')
    match['Rating_player3_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span')
    match['Rating_player4_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/span')
    match['Rating_player5_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/span')
    match['Rating_player6_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[6]/div[1]/span')
    match['Rating_player7_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[7]/div[1]/span')
    match['Rating_player8_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[8]/div[1]/span')
    match['Rating_player9_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[9]/div[1]/span')
    match['Rating_player10_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[10]/div[1]/span')
    match['Rating_player11_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[2]/div[2]/div[2]/div[11]/div[1]/span')
    match['Rating_player12_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[3]/div[3]/div[1]/div[1]/span')
    match['Rating_player13_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[3]/div[3]/div[2]/div[1]/span')
    match['Rating_player14_Away'] = rating(
        '//*[@id="stadium"]/div[1]/div[3]/div[3]/div[3]/div[1]/span')

    # Possession
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[3]/div[2]/label')
    button.click()
    match['Possession%_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[3]/div[1]/ul/li[1]/div/span[1]').text])
    match['Possession%_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[3]/div[1]/ul/li[1]/div/span[3]').text])
    match['Touches_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[3]/div[1]/ul/li[2]/div/span[1]').text])
    match['Touches_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[3]/div[1]/ul/li[2]/div/span[3]').text])
    button.click()

    # Passes
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[4]/div[2]/label')
    button.click()
    match['Pass_success%_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[4]/div[1]/ul/li[1]/div/span[1]').text])
    match['Pass_success%_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[4]/div[1]/ul/li[1]/div/span[3]').text])
    match['Accurate_passes_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[4]/div[1]/ul/li[3]/div/span[1]').text])
    match['Accurate_passes_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[4]/div[1]/ul/li[3]/div/span[3]').text])
    button.click()

    try:
        button = driver.find_element('xpath', '//*[@id="dugout-clsbtn"]')
        button.click()
        sleep(random.uniform(5.0, 10.0))
    except:
        pass

    # Dribbles
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[5]/div[2]/label')
    button.click()
    match['Dribbles_won_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[1]/div/span[1]').text])
    match['Dribbles_won_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[1]/div/span[3]').text])
    match['Dribbles_attempted_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[2]/div/span[1]').text])
    match['Dribbles_attempted_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[2]/div/span[3]').text])
    match['Dribbles_past_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[3]/div/span[1]').text])
    match['Dribbles_past_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[3]/div/span[3]').text])
    match['Dribbles_success_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[4]/div/span[1]').text])
    match['Dribbles_success_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[5]/div[1]/ul/li[4]/div/span[3]').text])
    button.click()

    # Aerial
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[6]/div[2]/label')
    button.click()
    match['Aerials_won_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[1]/div/span[1]').text])
    match['Aerials_won_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[1]/div/span[3]').text])
    match['Aerials_won%_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[2]/div/span[1]').text])
    match['Aerials_won%_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[2]/div/span[3]').text])
    match['Offensive_aerials_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[3]/div/span[1]').text])
    match['Offensive_aerials_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[3]/div/span[3]').text])
    match['Defensive_aerials_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[4]/div/span[1]').text])
    match['Defensive_aerials_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[6]/div[1]/ul/li[4]/div/span[3]').text])
    button.click()

    # Tackles
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[7]/div[2]/label')
    button.click()
    match['Successful_tackles_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[1]/div/span[1]').text])
    match['Successful_tackles_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[1]/div/span[3]').text])
    match['Tackles_attempted_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[2]/div/span[1]').text])
    match['Tackles_attempted_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[2]/div/span[3]').text])
    match['Was_dribbled_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[3]/div/span[1]').text])
    match['Was_dribbled_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[3]/div/span[3]').text])
    match['Tackle_success%_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[4]/div/span[1]').text])
    match['Tackle_success%_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[4]/div/span[3]').text])
    match['Clearances_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[5]/div/span[1]').text])
    match['Clearances_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[5]/div/span[3]').text])
    match['Interception_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[6]/div/span[1]').text])
    match['Interception_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[7]/div[1]/ul/li[6]/div/span[3]').text])
    button.click()

    try:
        button = driver.find_element('xpath', '//*[@id="dugout-clsbtn"]')
        button.click()
        sleep(random.uniform(5.0, 10.0))
    except:  # noqa: E722
        pass

    # Corner
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[8]/div[2]/label')
    button.click()
    match['Corners_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[8]/div[1]/ul/li[1]/div/span[1]').text])
    match['Corners_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[8]/div[1]/ul/li[1]/div/span[3]').text])
    match['Corner_accuracy%_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[8]/div[1]/ul/li[2]/div/span[1]').text])
    match['Corner_accuracy%_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[8]/div[1]/ul/li[2]/div/span[3]').text])
    button.click()

    # Dispossessed
    sleep(random.uniform(10.0, 20.0))
    button = xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[1]/li[9]/div[2]/label')
    button.click()
    match['Dispossessed_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[1]/div/span[1]').text])
    match['Dispossessed_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[1]/div/span[3]').text])
    match['Errors_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[2]/div/span[1]').text])
    match['Errors_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[2]/div/span[3]').text])
    match['Fouls_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[3]/div/span[1]').text])
    match['Fouls_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[3]/div/span[3]').text])
    match['Offside_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[4]/div/span[1]').text])
    match['Offside_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="match-centre-stats"]/div[1]/ul[2]/li[9]/div[1]/ul/li[4]/div/span[3]').text])
    button.click()

    # Chalkboard

    button = xpath_element(
        '//*[@id="live-match-options"]/li[3]/a')
    button.click()
    # Shots
    match['Shots_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[1]/a/div/span[1]').text])
    match['Shots_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[1]/a/div/span[3]').text])
    # Results
    match['Shots_Results_on_target_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[3]/span[1]').text])
    match['Shots_Results_on_target_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[3]/span[2]').text])
    match['Shots_Results_off_target_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[4]/span[1]').text])
    match['Shots_Results_off_target_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[4]/span[2]').text])
    match['Shots_Results_woodworks_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[5]/span[1]').text])
    match['Shots_Results_woodworks_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[5]/span[2]').text])
    match['Shots_Results_blocked_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[6]/span[1]').text])
    match['Shots_Results_blocked_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[6]/span[2]').text])
    match['Shots_Results_own_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[7]/span[1]').text])
    match['Shots_Results_own_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[2]/div[7]/span[2]').text])
    # Zones
    match['Shots_Zones_6-yard_box_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[2]/span[1]').text])
    match['Shots_Zones_6-yard_box_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[2]/span[2]').text])
    match['Shots_Zones_6-yard_box_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[2]/span[1]').text])
    match['Shots_Zones_6-yard_box_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[2]/span[2]').text])
    match['Shots_Zones_penalty_area_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[3]/span[1]').text])
    match['Shots_Zones_penalty_area_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[3]/span[2]').text])
    match['Shots_Zones_outside_box_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[4]/span[1]').text])
    match['Shots_Zones_outside_box_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[3]/div[4]/span[2]').text])
    # Situation
    match['Shots_Situation_open_play_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[2]/span[1]').text])
    match['Shots_Situation_open_play_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[2]/span[2]').text])
    match['Shots_Situation_fastbreak_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[3]/span[1]').text])
    match['Shots_Situation_fastbreak_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[3]/span[2]').text])
    match['Shots_Situation_set_pieces_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[4]/span[1]').text])
    match['Shots_Situation_set_pieces_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[4]/span[2]').text])
    match['Shots_Situation_penalty_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[5]/span[1]').text])
    match['Shots_Situation_penalty_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[5]/span[2]').text])
    match['Shots_Situation_own_goal_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[6]/span[1]').text])
    match['Shots_Situation_own_goal_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[4]/div[6]/span[2]').text])
    # Body parts
    match['Shots_Body_parts_right_foot_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[2]/span[1]').text])
    match['Shots_Body_parts_right_foot_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[2]/span[2]').text])
    match['Shots_Body_parts_left_foot_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[3]/span[1]').text])
    match['Shots_Body_parts_left_foot_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[3]/span[2]').text])
    match['Shots_Body_parts_head_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[4]/span[1]').text])
    match['Shots_Body_parts_head_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[4]/span[2]').text])
    match['Shots_Body_parts_other_bp_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[5]/span[1]').text])
    match['Shots_Body_parts_other_bp_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[1]/div[5]/div[5]/span[2]').text])

    # Passes
    # Type
    button = xpath_element(
        '//*[@id="event-type-filters"]/li[2]')
    button.click()
    match['Pass_Type_cross_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[2]/span[1]').text])
    match['Pass_Type_cross_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[2]/span[2]').text])
    match['Pass_Type_freekick_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[3]/span[1]').text])
    match['Pass_Type_freekick_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[3]/span[2]').text])
    match['Pass_Type_corner_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[4]/span[1]').text])
    match['Pass_Type_corner_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[4]/span[2]').text])
    match['Pass_Type_through_ball_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[5]/span[1]').text])
    match['Pass_Type_through_ball_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[5]/span[2]').text])
    match['Pass_Type_throw_in_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[6]/span[1]').text])
    match['Pass_Type_throw_in_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[1]/div[6]/span[2]').text])

    # Length
    match['Pass_Length_long_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[2]/div[2]/span[1]').text])
    match['Pass_Length_long_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[2]/div[2]/span[2]').text])
    match['Pass_Length_short_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[2]/div[3]/span[1]').text])
    match['Pass_Length_short_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[2]/div[3]/span[2]').text])

    # Height
    match['Pass_Height_chipped_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[3]/div[2]/span[1]').text])
    match['Pass_Height_chipped_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[3]/div[2]/span[2]').text])
    match['Pass_Height_ground_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[3]/div[3]/span[1]').text])
    match['Pass_Height_ground_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[3]/div[3]/span[2]').text])

    # Body parts
    match['Pass_Body_parts_head_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[4]/div[2]/span[1]').text])
    match['Pass_Body_parts_head_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[4]/div[2]/span[2]').text])
    match['Pass_Body_parts_feet_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[4]/div[3]/span[1]').text])
    match['Pass_Body_parts_feet_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[4]/div[3]/span[2]').text])

    # Direction
    match['Pass_Direction_forward_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[2]/span[1]').text])
    match['Pass_Direction_forward_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[2]/span[2]').text])
    match['Pass_Direction_backward_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[3]/span[1]').text])
    match['Pass_Direction_backward_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[3]/span[2]').text])
    match['Pass_Direction_left_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[4]/span[1]').text])
    match['Pass_Direction_left_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[4]/span[2]').text])
    match['Pass_Direction_right_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[5]/span[1]').text])
    match['Pass_Direction_right_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[5]/div[5]/span[2]').text])

    # Target zone
    match['Pass_Target_zone_defensive_t_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[2]/span[1]').text])
    match['Pass_Target_zone_defensive_t_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[2]/span[2]').text])
    match['Pass_Target_zone_mid_t_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[3]/span[1]').text])
    match['Pass_Target_zone_mid_t_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[3]/span[2]').text])
    match['Pass_Target_zone_final_t_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[4]/span[1]').text])
    match['Pass_Target_zone_final_t_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[2]/div[6]/div[4]/span[2]').text])

    # Clearances
    button = xpath_element(
        '//*[@id="event-type-filters"]/li[6]')
    button.click()
    match['Clearance_off_the_line_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[1]/div[3]/span[1]').text])
    match['Clearance_off_the_line_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[1]/div[3]/span[2]').text])
    match['Clearance_head_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[2]/div[2]/span[1]').text])
    match['Clearance_head_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[2]/div[2]/span[2]').text])
    match['Clearance_feet_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[2]/div[3]/span[1]').text])
    match['Clearance_feet_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[6]/div[2]/div[3]/span[2]').text])

    # Blocks
    sleep(random.uniform(5.0, 10.0))
    button = xpath_element(
        '//*[@id="event-type-filters"]/li[7]')
    button.click()
    match['Blocks_blocked_shots_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[7]/div[1]/div[2]/span[1]').text])
    match['Blocks_blocked_shots_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[7]/div[1]/div[2]/span[2]').text])
    match['Blocks_crosses_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[7]/div[1]/div[3]/span[1]').text])
    match['Blocks_crosses_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[7]/div[1]/div[3]/span[2]').text])

    # Loss of possession
    button = xpath_element(
        '//*[@id="event-type-filters"]/li[12]')
    button.click()
    match['Loss_possession_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[12]/a/div/span[1]').text])
    match['Loss_possession_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[12]/a/div/span[3]').text])
    match['Loss_possession_turnover_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[12]/div[1]/div[3]/span[1]').text])
    match['Loss_possession_turnover_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[12]/div[1]/div[3]/span[2]').text])

    # Erros
    button = xpath_element(
        '//*[@id="event-type-filters"]/li[13]')
    button.click()
    match['Error_lead_to_shot_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[13]/div[1]/div[2]/span[1]').text])
    match['Error_lead_to_shot_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[13]/div[1]/div[2]/span[2]').text])
    match['Error_lead_to_goal_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[13]/div[1]/div[3]/span[1]').text])
    match['Error_lead_to_goal_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="chalkboard"]/div[2]/div[13]/div[1]/div[3]/span[2]').text])

    # Saves
    match['Saves_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[14]/a/div/span[1]').text])
    match['Saves_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[14]/a/div/span[3]').text])

    # Claims
    match['Claims_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[15]/a/div/span[1]').text])
    match['Claims_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[15]/a/div/span[3]').text])

    # Punches
    match['Punches_Home'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[16]/a/div/span[1]').text])
    match['Punches_Away'] = pd.DataFrame([xpath_element(
        '//*[@id="event-type-filters"]/li[16]/a/div/span[3]').text])
    
    # Link
    match['Link'] = pd.DataFrame([url])

driver.close()
print(match)