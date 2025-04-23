# Задание 2
# from selenium.webdriver.common.by import By  #будем добавлять ожидание
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_address = driver.find_element_by_id("reg_email")
# email_address.send_keys("ram@mail.ru")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("G7t#kP9q$zW3@fJ2")
# register_button = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row")
# register_button.click()
# driver.quit()

# Задание 3

# from selenium.webdriver.common.by import By  #будем добавлять ожидание
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")# объявляем переменную login, задаём ей значение селектора поля логин
# login.send_keys("ram@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("G7t#kP9q$zW3@fJ2")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
#
# logout_element = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
# save_changes_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
# driver.quit()