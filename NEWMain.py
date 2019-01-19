from tkinter import *
from tkinter import ttk
from selenium.webdriver.support.ui import Select
from selenium import webdriver

def account():
    url = 'https://www.roblox.com/account/signupredir'

    driver = webdriver.Chrome('/Users/LordA/Desktop/Python Projects/Resources/chromedriver')
    driver.get(url)

    #Don't use this to make actual accounts,
    #all the pword function does is write the username backwards
    uname = uname_text.get()
    pword = uname[::-1]
    sex = 'Male'
    bdaymonth = 'Aug'
    bdayday = '07'
    bdayyear = '2001'
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



window = Tk()
window.title("Roblox Account Maker")
window.geometry("700x700+0+0")
window.configure(background="light blue")

Label(window, text="Roblox Account Maker", font="calibri 16 italic", bg="light blue", fg="black").pack()

Label(window, text="User Name", bg="light blue").pack()
uname_text=StringVar()
ent1=Entry(window, textvariable=uname_text).pack()



btn1=ttk.Button(window, text="Click once User Name has been added (Password is Username backwards)")
btn1.pack()
btn1.config(command=account)
