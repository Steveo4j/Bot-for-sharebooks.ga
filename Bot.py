import os
from selenium import webdriver


os.environ['PATH'] += r"C:/Chrome driver/chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://sharebooksserver.herokuapp.com")
for i in range(1, 5):
    driver.implicitly_wait(5)
    upload_button=driver.find_element_by_id('ember5')
    upload_button.click()

    driver.implicitly_wait(10)
    book_title = driver.find_element_by_id('ember16')
    book_author = driver.find_element_by_id('ember17')
    book_year = driver.find_element_by_id('ember18')
    book_code = driver.find_element_by_id('ember19')
    owner = driver.find_element_by_id('ember20')
    admin_number = driver.find_element_by_id('ember21')
    phone_number= driver.find_element_by_id('ember22')
    email= driver.find_element_by_id('ember23')

    book_title.send_keys(f"Amith has never managed to beat Stephen at chess")
    book_author.send_keys(f"Bot")
    book_year.send_keys(2020+i)
    book_code.send_keys(101+i)
    owner.send_keys(f"Bot {i}")
    admin_number.send_keys(1221+i)
    phone_number.send_keys(9972800777+i)
    email.send_keys("stephen911vishagan@gmail.com")

    submit_button = driver.find_element_by_class_name('is-primary')
    submit_button.click()
    driver.implicitly_wait(10)

    security_code = driver.find_element_by_id('alert-id').text
    print(security_code)
    driver.implicitly_wait(10)
    final_submit = driver.find_element_by_class_name('is-success')
    final_submit.click()

