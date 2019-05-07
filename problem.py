from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types/deluxe-room")
js = "window.scrollTo(0,1500)"
driver.execute_script(js)
time.sleep(2)
# room_element = driver.find_element_by_xpath("/html/body/div[8]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/a/h3/font/font")
# room_element.click()
startdata_element = driver.find_element_by_xpath("//input[@aria-describedby='DateInput__screen-reader-message-startDate_bookingbar']")
startdata_element.click()
startdata_element.send_keys("01/05/2019")
time.sleep(2)
enddata_element = driver.find_element_by_xpath("//input[@aria-describedby='DateInput__screen-reader-message-endDate_bookingbar']")
enddata_element.click()
enddata_element.send_keys("02/05/2019")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div/div/button").click()





