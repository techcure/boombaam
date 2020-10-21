from selenium import webdriver
from time import sleep


# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='C:/Users/me/Downloads/driver/chromedriver.exe')
driver.get("https://www.alabamainteractive.org/dps_crash_report")

driver.find_element_by_id("mainMenu_mainMenuObject_confirmation").click()

driver.find_element_by_xpath("//input[@value='Purchase Crash Report']").click()


inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.firstName']")
inputElement.send_keys('hello')

inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.lastName']")
inputElement.send_keys('hello')

inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.phoneNumber']")
inputElement.send_keys('123-123-1234')

driver.find_element_by_xpath("//input[@value='Continue']").click()

inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
inputElement.send_keys('0699958')

driver.find_element_by_xpath("//input[@value='Search for Report']").click()

sleep(3)

driver.find_element_by_link_text("Add to Cart").click()

sleep(10)

inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
inputElement.send_keys('0699959')

driver.find_element_by_xpath("//input[@value='Search for Report']").click()

sleep(3)

driver.find_element_by_link_text("Add to Cart").click()

sleep(10)

# driver.find_element_by_link_text("Proceed to Cart").click()
driver.find_element_by_xpath("//input[@value='Proceed to Cart']").click()

driver.find_element_by_id("summary_summaryObject_confirmation").click()

sleep(3)

driver.find_element_by_xpath("//input[@value='Checkout']").click()

driver.find_element_by_xpath("//select[@name='creditCardObject.cctype']/option[text()='Visa']").click()

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccnumber']")
inputElement.send_keys('1234567891234567')

driver.find_element_by_xpath("//select[@name='creditCardObject.ccexprmonth']/option[text()='Jan (01)']").click()
driver.find_element_by_xpath("//select[@name='creditCardObject.ccexpryear']/option[text()='2020']").click()

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccname']")
inputElement.send_keys('hello hello')

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccaddress1']")
inputElement.send_keys('address 1')

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccaddress2']")
inputElement.send_keys('address 2')

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cccity']")
inputElement.send_keys('city')

driver.find_element_by_xpath("//select[@name='creditCardObject.ccstate']/option[text()='Alabama']").click()

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cczip']")
inputElement.send_keys('55555-4444')

driver.find_element_by_xpath("//input[@value='Submit Payment']").click()


















