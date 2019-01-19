from selenium.webdriver.support.ui import Select
from selenium import webdriver

#Don't use this to make actual accounts,
#all the pword function does is write the username backwards
uname = 'Roflmao133398'
pword = uname[::-1]
sex = 'Male'
bdaymonth = 'Aug'
bdayday = '07'
bdayyear = '2001'

url = 'https://www.roblox.com/account/signupredir'

driver = webdriver.Chrome('/Users/%USERNAME%/Desktop/Roblox Acc. Creator/Resources/chromedriver')
driver.get(url)

#GetFields&Send
unames = driver.find_element_by_id('signup-username')
pword1 = driver.find_element_by_id('signup-password')
gender = driver.find_element_by_id(sex+'Button')
signup = driver.find_element_by_id('signup-button')
####
month = driver.find_element_by_id('MonthDropdown')
day = driver.find_element_by_id('DayDropdown')
year = driver.find_element_by_id('YearDropdown')

#Selection
select = Select(month)
select.select_by_value(bdaymonth)
select = Select(day)
select.select_by_value(bdayday)
select = Select(year)
select.select_by_value(bdayyear)
####
unames.send_keys(uname)
pword1.send_keys(pword)
gender.click()
signup.click()


