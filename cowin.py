from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/home")
elem = driver.find_element_by_id("mat-input-0")
elem.clear()
elem.send_keys("248198")
driver.find_element_by_xpath("//input[@value='18']").click()

elem.send_keys(Keys.RETURN)

text="No Vaccination center is available for booking."

print(driver.find_element_by_class_name("available-para").get_attribute("Value"))

# if text in driver.find_element_by_class_name("available-para").get_attribute("Value")
#     print ("vaccine not available")


# assert "No Vaccination center is available for booking." not in driver.page_source
# driver.close()
