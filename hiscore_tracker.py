from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class hiscore:
    username
    Attack, Strength, Defence, Ranged, Prayer, Magic, Runecrafting
    Construction, Hitpoints, Agility, Herblore, Thieving, Crafting, Fletching
    Slayer, Hunter, Mining, Smithing, Fishing, Cooking, Firemaking
    Woodcutting, Farming

    def __init__(self, name):
        self.name = username


"""
options = Options()
options.add_argument('--headless')
"""
driver = webdriver.Firefox()
driver.get("https://secure.runescape.com/m=hiscore_oldschool/" +
           "overall.ws#_ga=2.28971004.1383053463." +
           "1537544578-302986252.1537544578")
elem = driver.find_element_by_name("user1")
username = input('Enter the user you want to look up:\n')
elem.send_keys(str(username))
elem.send_keys(Keys.ENTER)
hiscore_data = driver.find_element_by_id("contentHiscores")
hiscore = hiscore(username)
