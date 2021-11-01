import random
import time
from selenium import webdriver
a=random.randint(5,12)
driver = webdriver.Chrome(executable_path='/home/user/Downloads/chromedriver')
driver.get('https://www.google.com.vn/search?q=haitt300&source=hp&ei=UrB7YfyzNc34-gS25oz4DQ&iflsig=ALs-wAMAAAAAYXu-YkZS9kHad0nf2UpU8hv4rwfYZjKn&oq=haitt300&gs_lcp=Cgdnd3Mtd2l6EAM6BAgAEA06BAguEA06BggAEA0QHjoICAAQCBANEB46CggAEAgQDRAKEB5QlQZYtgZgyOwNaANwAHgBgAGYAYgBjQSSAQMwLjSYAQCgAQE&sclient=gws-wiz&ved=0ahUKEwj8pPK5me_zAhVNvJ4KHTYzA98Q4dUDCAc&uact=5')
time.sleep(a)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()
time.sleep(a)
driver.execute_script("window.scrollTo(0,750)")
driver.find_element_by_xpath("//div[@id='main']/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div/a/div/div/div[2]/div/div[2]/div[2]").click()
time.sleep(a)
driver.execute_script('window.scrollTo(0,950)')
time.sleep(a)
driver.quit()

