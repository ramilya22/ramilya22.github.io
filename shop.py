# Задание 4
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
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# HTML_5_Forms_book = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']")
# HTML_5_Forms_book.click()
# book_HTML5Forms_text = driver.find_element_by_css("product-181>div>h1")
# book_HTML5Forms_text  =  book_HTML5Forms.text
# assert book_HTML5Forms_text == "HTML5 Forms"
# driver.quit()
import time

# Задание 5
# from selenium.webdriver.common.by import By
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
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# html_btn = driver.find_element_by_css_selector(".product-categories>.cat-item-19")
# html_btn.click()
# book_HTML_5_Forms = driver.find_element_by_css("img[title='Mastering HTML5 Forms']")
# book_HTML_5_Forms_text = book_HTML_5_Forms.text
# book_HTML5_WebApp_Develpment = driver.find_element_by_css("img[title='HTML5 Web Application Development Beginner's guide']")
# book_HTML5_WebApp_Develpment_text = book_HTML5_WebApp_Develpment.text
# book_Thinking_in_HTML = driver.find_element_by_css_selector("img[title='Thinking in HTML']")
# book_Thinking_in_HTML_text = book_Thinking_in_HTML.text
# assert book_HTML_5_Forms == "Mastering HTML5 Forms"
# assert book_HTML5_WebApp_Develpment == "HTML5 Web Application Development Beginner's guide"
# assert book_Thinking_in_HTML == "Thinking in HTML"
# driver.quit()

# Задание 6
# from selenium.webdriver.common.by import By
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
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
# element = driver.find_element_by_class_name(".orderby") # "element" это просто название переменной, можно задать и другое
# select = Select(element) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
# select.select_by_value("0")
# select.select_by_value(5)
# time.sleep(5)
# element = driver.find_element_by_class_name(".orderby") # "element" это просто название переменной, можно задать и другое
# select = Select(element)
# default_sorting_value = select.first_selected_option.get_attribute("value")
# assert default_sorting_value == "5"
# from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
# element = driver.find_element_by_class_name("hight to low") # "element" это просто название переменной, можно задать и другое
# select = Select(element) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
# select.select_by_value("5")
# driver.quit()




# Задание 7
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
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# Android_Quick_Start_book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
# Android_Quick_Start_book.click()
# book_old_price=driver.find_element_by_css(".price>del>span")#проверим что содержание цены равно 600 и 450
# book_old_price_text  =  book_old_price.text
# book_new_price=driver.find_element_by_css(".price>ins>span")
# book_new_price_text = book_new_price.text
# #проверим значение цен
# assert book_old_price == 600.00 #проверяем цену, сравниваем
# assert book_new_price == 450.00
# #добавим явное ожидание
# book_cover = WebDriverWait(driver, 10) .until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10) .until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# driver.quit()


# Задание 8

# from selenium.webdriver.common.by import By  #будем добавлять ожидание
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# add_to_basket_btn = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
# add_to_basket_btn.click()
# basket_price = driver.find_element_by_id("wpmenucartli")
# basket_price_text = basket_price.text
# assert basket_price == "1 Item , ₹180.00"
# basket_btn = driver.find_element_by_id("wpmenucartli")
# basket_btn.click()
# subtotal_price = WebDriverWait(driver, 10) .until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal")))
# total_price = WebDriverWait(driver, 10) .until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total")))
# driver.quit()

# Задание 9

# from selenium.webdriver.common.by import By  #будем добавлять ожидание
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket_btn = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
# add_to_basket_btn.click()
# time.sleep(5)
# js_basket_btn = driver.find_element_by_css_selector(".post-180>a:nth-child(2)")
# js_basket_btn.click()
# basket_btn = driver.find_element_by_id("wpmenucartli")
# basket_btn.click()
# time.sleep(5)
# remove_btn = driver.find_element_by_css_selector(".cart_item>td>a")
# remove_btn.click()
# undo_btn = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo_btn.click()
# quantity_field_locator = (By.CSS_SELECTOR, ".input-text.qty.text")
# quantity_field = driver.find_element(quantity_field_locator)
# quantity_field.clear()
# quantity_field.send_keys('3')
# update_basket_btn = driver.find_element_by_xpath("//input[@value='Update Basket']")
# update_basket_btn.click()
# js_quantity = driver.find_element_by_xpath("//input[@value='3']")
# js_quantity_text = js_quantity.text
# assert js_quantity == 3
# time.sleep(5)
# apply_coupon = driver.find_element_by_xpath("///input[@value='Apply Coupon']")
# apply_coupon.click()
# error_message = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
# driver.quit()


# Задание 10
# from selenium.webdriver.common.by import By  #будем добавлять ожидание
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket_btn = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
# add_to_basket_btn.click()
# time.sleep(5)
# basket_btn = driver.find_element_by_id("wpmenucartli")
# basket_btn.click()
# proceed_to_checkout = WebDriverWait(driver, 10) .until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# proceed_to_checkout.click()
# first_name = WebDriverWait(driver, 10) .until(
#      EC.visibility_of_element_located((By.ID, "billing_first_name")))
# first_name.send_keys("Ram")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Lat")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89175640000")
# email_address = driver.find_element_by_id("billing_email")
# email_address.send_keys("ram@mail.ru")
# country_select = driver.find_element_by_id("s2id_billing_country")
# country_select.click()
# input_field = driver.find_element_by_id("s2id_autogen1_search")
# input_field.send_keys("Russia")
# russia = driver.find_element_by_xpath("//option[@value='RU']")
# russia.click()
# street_address = driver.find_element_by_xpath("//input[@placeholder='Street address']")
# street_address.send_keys("Spting")
# city = driver.find_element_by_xpath("//input[@name='billing_city']")
# city.send_keys("Bugulma")
# state_country = driver.find_element_by_xpath("//input[@id='billing_state']")
# state_country.send_keys("Tatarstan")
# postcode_zip = driver.find_element_by_xpath("//input[@id='billing_postcode']")
# postcode_zip.send_keys("423230")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# check_payments_checkbox = driver.find_element_by_css_selector(".wc_payment_methods>li:nth-child(2)")
# check_payments_checkbox.click()
# place_order = driver.find_element_by_id("place_order")
# place_order.click()
# window_text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce .woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# payment_method = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)"), "Check Payments"))
# driver.quit()
#
