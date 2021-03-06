# -*- coding: utf-8 -*-

from selenium import webdriver
import telegram

myTelegramBot_token = 'tokenKey'
autoLoginLogBot = telegram.Bot(token=myTelegramBot_token)
# updates = autoLoginLogBot.getUpdates()

chat_id = autoLoginLogBot.getUpdates()[-1].message.chat.id

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('D:\\00. jwhong\\99. DevelopTool\\chromedriver_win32\\chromedriver')
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS('/Users/beomi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(10)

# url에 접근한다.
driver.get('http://deafmov.org/bbs/login.php')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('mb_id').send_keys('xxx')
driver.find_element_by_name('mb_password').send_keys('xxx')

# 로그인 버튼을 눌러주자.
driver.find_element_by_css_selector('#thema_wrapper > div > div.container > div > div.col-md-9.at-col.at-main > div.row > div > div > div.form-body > form > div.row > div:nth-child(2) > button').click()
driver.implicitly_wait(10)

driver.find_element_by_css_selector('#thema_wrapper > div > aside > div > nav.at-lnb-menu > ul > li:nth-child(3) > a').click()
autoLoginLogBot.sendMessage(chat_id=chat_id, text='DeafMov Login Success..')
driver.close()
driver.quit()
