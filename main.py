from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

target_url = "https://chromedino.com/"
driver.get(target_url)

game = driver.find_element_by_xpath('/html')
print(game.text)
sleep(2)
game.send_keys(Keys.SPACE)
sleep(5)
game.send_keys(Keys.SPACE)
sleep(1)
game.send_keys(Keys.SPACE)
sleep(1)
game.send_keys(Keys.SPACE)

#game.click()
#game.click()
sleep(2)

driver.quit()   # Close Session
