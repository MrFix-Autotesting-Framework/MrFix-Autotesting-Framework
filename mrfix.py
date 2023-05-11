import sys
import time
import requests
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui



class MrFixUI :

    def assertElementsIsPresentByXpatch(self, xpath_elements):
        try:
            elements = self.find_elements(By.XPATH, xpath_elements)
            return [True, len(elements)]
        except NoSuchElementException:
            return [False, 0]

    def assertElementIsPresentByXPath_Click(self, xpath, msg=None):
        try:
            element = self.find_element(By.XPATH, xpath).click()
            return True
        except NoSuchElementException:
            return False

    def assertElementIsPresentByXPath_Send(self, xpath_input, send_message):
        try:
            element = self.find_element(By.XPATH, xpath_input)
            element.clear()
            length = len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            time.sleep(0.5)
            element.send_keys(send_message)
            return True
        except NoSuchElementException:
            return (False)

    def check_exists_xpath(self, xpath_element):
        try:
            self.set_page_load_timeout(1)
            self.implicitly_wait(1)
            self.find_element(By.XPATH, xpath_element)
            self.implicitly_wait(10)
            self.set_page_load_timeout(10)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, xpath_element):
        if MrFixUI.check_exists_xpath(self, xpath_element) == True:
            self.find_element(By.XPATH, xpath_element).click()
        else:
            print(f'Element {xpath_element} not exists')
            sys.exit()


    def click_drop_down_text(self, xpath_element, element_text):
        if MrFixUI.check_exists_xpath(self, xpath_element) == False:
            print(f'Element {xpath_element} not exists')
            sys.exit()
        element = self.find_element(By.XPATH, xpath_element)
        element.click()
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("text") == element_text:
                option.click()
                break

    def send_input_text(self, xpath_input, input_text):
        if MrFixUI.check_exists_xpath(self, xpath_input) == False:
            print(f'Element {xpath_input} not exists')
            sys.exit()
        MrFixUI.assertElementIsPresentByXPath_Send(self, xpath_input, input_text)


    def return_elements_array(self, xpath_elements):
        if MrFixUI.check_exists_xpath(self, xpath_elements) == False:
            print(f'Element {xpath_elements} not exists')
            sys.exit()
        elements_array = MrFixUI.assertElementsIsPresentByXpatch(self, xpath_elements)
        return elements_array


    def return_elements_array2(self, xpath_elements):
        if MrFixUI.check_exists_xpath(self, xpath_elements) == False:
            print(f'Element {xpath_elements} not exists')
            sys.exit()
        elements_array = self.find_elements(By.XPATH, xpath_elements)
        return elements_array


    def scroll_down_click_element(self, xpath_down_link):
        scroll_pause_time = 0.5
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height or MrFixUI.check_exists_xpath(self, xpath_down_link):
                break
            last_height = new_height
        assert MrFixUI.assertElementIsPresentByXPath_Click(self, xpath_down_link), f'Element {xpath_down_link} not exists'


    def click_element_key_enter(self, xpath_element):
        if MrFixUI.check_exists_xpath(self, xpath_element) == False:
            print(f'Element {xpath_element} not exists')
            sys.exit()
        self.find_element(By.XPATH, xpath_element).send_keys(Keys.RETURN)


    def autorization_user(self, url, login, password):
        session = requests.Session()
        session.post(url, {
            'username': login,
            'password': password,
            'remember': 1,
        })


    def uploading_file(self, xpath_input_file, file_path):
        if MrFixUI.check_exists_xpath(self, xpath_input_file) == False:
            print(f'Element {xpath_input_file} not exists')
            sys.exit()
        self.find_element(By.XPATH, xpath_input_file).send_keys(file_path)


    def switch_to_current_window(self):
        self.switch_to.active_element
        handles = self.window_handles
        for handle in handles:
            if self.current_window_handle != handle:
                # Close first window
                self.close()
                # set second window active (handle)
                self.switch_to.window(handle)


    def get_elements_attribute(self, xpath_element, attribute):
        if MrFixUI.check_exists_xpath(self, xpath_element) == False:
            print(f'Element {xpath_element} not exists')
            sys.exit()
        element = self.find_element(By.XPATH, xpath_element)
        return element.get_attribute(attribute)


    def get_elements_text(self, xpath_element):
        if MrFixUI.check_exists_xpath(self, xpath_element) == False:
            print(f'Element {xpath_element} not exists')
            sys.exit()
        element = self.find_element(By.XPATH, xpath_element)
        return element.text


    def select_drop_down_value(self, xpath_drop_down, drop_down_value):
        if MrFixUI.check_exists_xpath(self, xpath_drop_down) == False:
            print(f'Element {xpath_drop_down} not exists')
            sys.exit()
        select = Select(self.find_element(By.XPATH, xpath_drop_down))
        # select by value
        select.select_by_value(drop_down_value)


    def select_drop_down_text(self, xpath_drop_down, drop_down_text):
        if MrFixUI.check_exists_xpath(self, xpath_drop_down) == False:
            print(f'Element {xpath_drop_down} not exists')
            sys.exit()
        select = Select(self.find_element(By.XPATH, xpath_drop_down))
        # select by visible text
        select.select_by_visible_text(drop_down_text)


    def clear_input_element(self, xpath_input_element):
        if MrFixUI.check_exists_xpath(self, xpath_input_element) == False:
            print(f'Element {xpath_input_element} not exists')
            sys.exit()
        element = self.find_element(By.XPATH, xpath_input_element)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.clear()


    def pressing_down_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(.1)
        action.perform()


    def pressing_up_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_UP)
            time.sleep(.1)
        action.perform()


    def pressing_left_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_LEFT)
            time.sleep(.1)
        action.perform()


    def pressing_right_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_RIGHT)
            time.sleep(.1)
        action.perform()


    def pressing_enter_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.RETURN)
            time.sleep(.1)
        action.perform()


    def pressing_tab_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.TAB)
            time.sleep(.1)
        action.perform()


    def pressing_backspace_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.BACKSPACE)
            time.sleep(.1)
        action.perform()


    def pressing_delete_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.DELETE)
            time.sleep(.1)
        action.perform()


    def pressing_char_key(self, char, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(char)
            time.sleep(.1)
        action.perform()


    def check_url(url):
        try:
            response = requests.get(url)
        except ValueError:
            return False
        return True


    def open_url_in_new_tab(self, url):
        # open in new tab
        self.execute_script("window.open('%s', '_blank')" % url)
        # Switch to new tab
        self.switch_to.window(self.window_handles[-1])


    def check_clickable_element(self, xpath_element):
        try:
            if MrFixUI.check_exists_xpath(self, xpath_element) == False:
                print(f'Element {xpath_element} not exists')
                sys.exit()
            element = self.find_element(By.XPATH, xpath_element)
            element.click()
            return True
        except WebDriverException:
            print("Element is not clickable")
            return False


    def check_visible_element(self, xpath_element):
        try:
            element = self.find_element_by_xpath(xpath_element)
            return element.is_visible()
        except NoSuchElementException:
            return False

    def check_displayed_element(self, xpath_element):
        try:
            element = self.find_element_by_xpath(xpath_element)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def get_clipboard_text(self):
        return str(pyperclip.paste())


    def convert_string_to_float(string_value):
        val = string_value.replace(',', '.')
        if val != '':
            val = val.replace(' ', '', 100)
            val = float(val)
            return val
        else:
            return 0


    def find_text_on_page(self, text):
        try:
            self.find_element_by_partial_link_text(text).click()
            return True
        except NoSuchElementException:
            return False


    def make_element_displayed_and_click(self, xpath_element):
        while not MrFixUI.check_displayed_element(self, xpath_element):
            MrFixUI.pressing_down_arrow_key(self, 1)
        MrFixUI.click_element(self, xpath_element)


    def make_element_displayed_and_send(self, xpath_element, send_text):
        while not MrFixUI.check_displayed_element(self, xpath_element):
            MrFixUI.pressing_down_arrow_key(self, 1)
        MrFixUI.send_input_text(self, xpath_element, send_text)


    def find_href_on_page(self, link):
        link_availability = False
        if MrFixUI.check_exists_xpath(self, "//a[@href]") == True:
            elems = self.find_element(By.XPATH, "//a[@href]")
        for elem in elems:
            s = elem.get_attribute("href")
            if link in s:
                link_availability = True
        return link_availability


    def waiting_process_complete(self, xpath_proccess, time_in_second):
        for i in range(time_in_second * 2):
            if MrFixUI.check_displayed_element(self, xpath_proccess):
                time.sleep(0.5)
            else:
                time.sleep(0.5)
                break


    def waiting_appearance_element (self, xpath_element, time_in_second):
        for i in range(time_in_second * 2):
            if not MrFixUI.check_displayed_element(self, xpath_element):
                time.sleep(0.5)
            else:
                time.sleep(0.5)
                break


    def check_class_in_element(self, xpath_element, text_in_class):
        element = self.find_element(By.XPATH, xpath_element)
        if text_in_class in str(element.get_attribute("class")):
            return True
        else:
            return False







