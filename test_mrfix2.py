import time
import pytest
from selenium import webdriver
from mrfix.mrfix import MrFixUI as Mr

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Внимание! time.sleep(1.5) установлены только для того, чтобы можно было визуально оценить, что методы модуля mrfix работают корректно

def test_mrfix_for_example(driver):

    # селекторы:
    xpath_login_page_link = '//a[text()="Form Authentication"]'
    xpath_login_input = '//input[@id="username"]'
    xpath_password_input = '//input[@id="password"]'
    xpath_submit_button = '//button[@type="submit"]'
    xpath_logout = '//i[text()=" Logout"]'
    xpath_dropdown_page_link = '//a[text()="Dropdown"]'
    xpath_dropdown = '//select[@id="dropdown"]'
    xpath_checkbox = '//input[@type="checkbox"]'
    xpath_dynamic_controls_page_link = '//a[text()="Dynamic Controls"]'
    xpath_enable_button = '//button[text()="Enable"]'
    xpath_waiting = '//div[@id="loading"]'
    xpath_content = '//*[@id="content"]/div[1]/p'
    xpath_input = '//input[@type="text"]'
    xpath_disable_button = '//button[text()="Disable"]'
    xpath_its_disabled_text = '//p[@id="message"]'

    # данные
    userlogin = 'tomsmith'
    userpassword = 'SuperSecretPassword!'
    start_url = 'http://the-internet.herokuapp.com/'
    dropdown_text1 = 'Option 1'
    dropdown_text2 = 'Option 2'
    its_disabled_text = "It's disabled!"

    # установили максимальный размер окна браузера
    driver.maximize_window()

    # заходим на стартовую страницу
    driver.get(start_url)
    time.sleep(1.5)

    # переходим на страницу с логином и паролем
    Mr.click_element(driver, xpath_login_page_link)
    time.sleep(1.5)

    # вводим логин
    Mr.send_input_text(driver, xpath_login_input, userlogin)
    time.sleep(1.5)

    # вводим пароль
    Mr.send_input_text(driver, xpath_password_input, userpassword)
    time.sleep(1.5)

    # нажимаем кнопку Submit
    Mr.click_element(driver, xpath_submit_button)
    time.sleep(1.5)

    # нажимаем кнопку Logout
    Mr.click_element(driver, xpath_logout)
    time.sleep(1.5)

    # перезаходим на стартовую страницу
    driver.get(start_url)
    time.sleep(1.5)

    # переходим на страницу с dropdown
    Mr.click_element(driver, xpath_dropdown_page_link)
    time.sleep(1.5)

    # выбираем первый элемент выпадающего списка
    Mr.select_drop_down_text(driver, xpath_dropdown, dropdown_text1)
    time.sleep(1.5)

    # выбираем второй элемент выпадающего списка
    Mr.select_drop_down_text(driver, xpath_dropdown, dropdown_text2)
    time.sleep(1.5)

    # перезаходим на стартовую страницу
    driver.get(start_url)
    time.sleep(1.5)

    # переходим на страницу Dynamic Controls
    Mr.click_element(driver, xpath_dynamic_controls_page_link)
    time.sleep(1.5)

    # выделяем checkbox A
    Mr.click_element(driver, xpath_checkbox)
    time.sleep(1.5)

    # убираем выделение checkbox
    Mr.click_element(driver, xpath_checkbox)
    time.sleep(1.5)

    # нажимаем кнопку "Enable"
    Mr.click_element(driver, xpath_enable_button)

    # ждем, пока станет доступно поле ввода
    Mr.waiting_process_complete(driver, xpath_waiting, 10)

    # считываем текст подзаголовка
    content = Mr.get_elements_text(driver, xpath_content)

    # вставляем полученный текст в поле ввода
    Mr.send_input_text(driver, xpath_input, content)
    time.sleep(1.5)

    # очищаем поле ввода
    Mr.clear_input_element(driver, xpath_input)
    time.sleep(1.5)

    # закрываем доступ к полю ввода
    Mr.click_element(driver, xpath_disable_button)

    # ждем, пока завершится процесс закрытия доступа
    Mr.waiting_process_complete(driver, xpath_waiting, 10)

    # если появилась надпись "It's disabled!", то переходим на стартовую страницу
    if Mr.get_elements_text(driver, xpath_its_disabled_text) == its_disabled_text:
        driver.get(start_url)
        time.sleep(1.5)


















