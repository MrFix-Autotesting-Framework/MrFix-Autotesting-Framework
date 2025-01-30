import re
from urllib.parse import urlparse
from pathlib import Path
import sys
import shutil
from collections import defaultdict
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from loguru import logger
import datetime
import pyperclip
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from bs4 import BeautifulSoup
import subprocess
import psycopg2    # pip install psycopg2-binary
import os
if os.name != 'nt':
    import sh
import csv
import socket
from cryptography.fernet import Fernet
import os
import requests
import concurrent.futures
import asyncio
import httpx
import pytest
import pathlib



class MrFixUI:

    @staticmethod
    def check_exists_xpath(driver, check_xpath, timeout=0.5):
        # - checks the existence of an element with xpath = check_xpath and returns True or False
        try:
            rezult = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, check_xpath)))
            return rezult

        except Exception:
            # If the element is not found or any other exception occurs, return False
            return False

    @staticmethod
    def click_element_by_xpath(driver, element_xpath):
        # Find and click on the element
        try:
            # Find the element by XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Select the option by its text
            element.click()
            return True  # Click successfully

        except NoSuchElementException as e:
            error_message = f"Element not found: {str(e)}"
            return error_message

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

    @staticmethod
    def click_element_by_xpath2(driver, element_xpath, timeout=10):
        try:
            # Wait for the element to be clickable before attempting the click
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, element_xpath))
            )

            # Click the element
            element.click()

            return True  # Click successful

        except Exception:
            # If the element is not found or any other exception occurs, return False
            return False

    @staticmethod
    def select_from_dropdown_text(driver, dropdown_xpath, dropdown_text):
        # - selects a line with text = dropdown_text from the drop-down list with xpath = dropdown_xpath and returns True of success or text of error
        try:
            # Find the dropdown element by XPath
            dropdown = Select(driver.find_element(By.XPATH, dropdown_xpath))

            # Select the option by its text
            dropdown.select_by_visible_text(dropdown_text)
            return True  # Option selected successfully

        except NoSuchElementException as e:
            error_message = f"Element not found: {str(e)}"
            return error_message

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

    @staticmethod
    def send_text_to_input(driver, input_xpath, send_text):
        # - sends to the input element with xpath = input_xpath text = send_text and returns True of success or text of error
        try:
            # Find the input element using XPath
            input_element = driver.find_element(By.XPATH, input_xpath)

            # Clear the input field
            input_element.clear()

            # Send text to the input element
            input_element.send_keys(send_text)
            # input_element.send_keys(Keys.ENTER)

            # Return True to indicate successful text entry
            return True

        except NoSuchElementException:
            # If the input element is not found, return the error message
            return f"Input element not found for XPath: {input_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def return_list_elements_by_xpath(driver, elements_xpath):
        # - returns a list of elements with xpath = elements_xpath or returns text of error
        try:
            # Find the elements using XPath
            elements = driver.find_elements(By.XPATH, elements_xpath)

            # Return the list of elements
            return elements

        except NoSuchElementException:
            # If no elements are found, return the error message
            return f"No elements found for XPath: {elements_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def press_enter_on_element(driver, element_xpath):
        # - click Enter on element with xpath = elements_xpath and returns True of success or text of error
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Simulate pressing the Enter key on the element
            element.send_keys(Keys.ENTER)

            # Return True to indicate successful key press
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def press_space_on_element(driver, element_xpath):
        # - click Space on element with xpath = elements_xpathand and returns True of success or text of error
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Simulate pressing the Enter key on the element
            element.send_keys(Keys.SPACE)

            # Return True to indicate successful key press
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def upload_file(driver, input_xpath, file_path):
        # - upload file with path + file name = "file_path" in element of type "input" with xpath = "input_xpath" and returns True of success or text of error
        try:
            # Find the file input element using XPath
            file_input = driver.find_element(By.XPATH, input_xpath)

            # Clear the file input field (optional)
            file_input.clear()

            # Send the file path to the file input element
            file_input.send_keys(file_path)

            # Return True to indicate successful file upload
            return True

        except NoSuchElementException:
            # If the file input element is not found, return the error message
            return f"File input element not found for XPath: {input_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)


    @staticmethod
    def upload_file_by_script(driver, input_xpath, file_path):
    # - upload file with help of script and with path + file name = "file_path" in element of type "input" with xpath = "input_xpath" and returns True of success or text of error
        try:
            # Find the file input element using its XPath
            file_input = driver.find_element(By.XPATH, input_xpath)

            # Make the element interactable if it's hidden or disabled
            driver.execute_script("arguments[0].style.display = 'block';", file_input)
            driver.execute_script("arguments[0].removeAttribute('disabled');", file_input)

            # Set the value of the file input element to the file path
            driver.execute_script(f"arguments[0].value = '{file_path}';", file_input)

            # Submit the form or perform any other actions necessary
            # (You may need to adjust this part based on your specific web page)

            # Return True to indicate success
            return True
        except Exception as e:
            # Print any exceptions that occur for debugging
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def switch_to_current_window(driver):
        # - swith to current window in browser and returns True or error text
        try:
            # Get the window handle of the current window
            current_window = driver.current_window_handle

            # Close all other windows except the current window
            for window_handle in driver.window_handles:
                if window_handle != current_window:
                    driver.switch_to.window(window_handle)
                    driver.close()

            # Switch back to the current window
            driver.switch_to.window(current_window)

            # Return True to indicate successful window switch
            return True

        except NoSuchWindowException:
            # If the window handle is not found, return the error message
            return "Window handle not found"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def get_element_attribute(driver, element_xpath, element_attribute):
        # - get attribute = element_attribute of element with xpath = element_xpath and returns the attribute value or text of error
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Get the attribute value of the element
            attribute_value = element.get_attribute(element_attribute)

            # Return the attribute value
            return attribute_value

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def get_element_text(driver, element_xpath):
        # - get text of element with xpath = element_xpath and returns the text of success or text of error
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Get the text of the element
            element_text = element.text

            # Return the element text
            return element_text

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def select_dropdown_value(driver, dropdown_xpath, dropdown_value):
        # - select the item with xpath = dropdown_xpath from the drop-down list. value = dropdown_value and return True of success or text of error
        try:
            # Find the drop-down list element using XPath
            dropdown = Select(driver.find_element(By.XPATH, dropdown_xpath))

            # Select the value from the drop-down list
            dropdown.select_by_value(dropdown_value)

            # Return True to indicate successful selection
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {dropdown_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def clear_input_element(driver, element_xpath):
        # - clear element with xpath = element_xpath and return True of success or text of error

        try:
            # Find the input element using XPath
            input_element = driver.find_element(By.XPATH, element_xpath)

            # Clear the input element

            # method 1
            input_element.send_keys(Keys.DELETE)

            # method 2
            input_element.clear()

            # Return True to indicate successful clearing
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

    @staticmethod
    def press_escape_key(driver, n):
        # - presses the ESCAPE key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ESCAPE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_down_arrow_key(driver, n):
        # - presses the ARROW DOWN key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_up_arrow_key(driver, n):
        # - presses the ARROW UP key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_UP)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_left_arrow_key(driver, n):
        # - presses the ARROW LEFT key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_LEFT)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_right_arrow_key(driver, n):
        # - presses the ARROW RIGHT key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_RIGHT)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_enter_key(driver, n):
        # - presses the ENTER key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.RETURN)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_tab_key(driver, n):
        # - presses the TAB key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.TAB)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_backspace_key(driver, n):
        # - presses the BACKSPACE key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.BACKSPACE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_delete_key(driver, n):
        # - presses the DELETE key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.DELETE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_char_key(driver, char_key, n):
        # - presses the key = char_key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(char_key)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_space_key(driver, n):
        # - presses the SPACE key n-times
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.SPACE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def check_url_exists(driver, check_url):
        # - checks if url = check_url exists and return True of success or False
        try:
            # Set a timeout to wait for the page to load
            original_timeout = driver.get_timeout()
            driver.set_page_load_timeout(original_timeout)

            # Open the URL
            driver.get(check_url)

            # If no exception is raised, the URL exists
            return True

        except WebDriverException:
            # URL does not exist or failed to load
            return False

    @staticmethod
    def open_url_in_new_tab(driver, open_url):
        # - opens url = open_url in a new browser tab and return True of success or text of error
        try:
            # Open a new tab
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])

            # Open the URL in the new tab
            driver.get(open_url)

            # Return True if the URL was opened successfully
            return True

        except WebDriverException as e:
            # Handle any exceptions that occur and return the error message
            return str(e)

    @staticmethod
    def check_element_is_displayed(driver, element_xpath):
        # - checks the display of an element with xpath = element_xpath on the page and return True of success or False
        try:
            # Find the element on the page using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Check if the element is displayed
            if element.is_displayed():
                return True
            else:
                return False

        except NoSuchElementException as e:
            # Element not found on the page
            return False

        except Exception as e:
            # Other exceptions
            return False

    @staticmethod
    def get_clipboard_text():
        # - gets the text from the clipboard
        return str(pyperclip.paste())

    @staticmethod
    def convert_string_to_float(string_for_convert):
        # - converts a string value to a floating point value and return float value or text of error
        try:
            float_value = string_for_convert.replace(',', '.')
            if float_value != '':
                float_value = float_value.replace(' ', '', 100)
                float_value = float(float_value)
                return float_value
        except ValueError as e:
            return str(e)

    @staticmethod
    def check_text_is_present_on_page(driver, check_text):
        # - checks to present text = check_text on page and return True of success or False or text of error
        try:
            # Check if the text is present in the page source
            page_source = driver.page_source
            if check_text in page_source:
                return True
            else:
                return False

        except Exception as e:
            # Handle any exceptions that occur
            return f"An error occurred: {e}"

    @staticmethod
    def make_displayed_with_arrow_down(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing the key ARROW DOWN and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    return True
            except:
                pass

            # Press the "ARROW UP" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_up(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing the key ARROW UP and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    return True
            except:
                pass

            # Press the "ARROW UP" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_down_and_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.click()
                    return True
            except:
                pass

            # Press the "ARROW DOWN" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_up_and_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.click()
                    return True
            except:
                pass

            # Press the "ARROW UP" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_down_and_enter_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks ENTER key on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.send_keys(Keys.ENTER)
                    return True
            except:
                pass

            # Press the "ARROW DOWN" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_up_and_enter_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks ENTER key on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.send_keys(Keys.ENTER)
                    return True
            except:
                pass

            # Press the "ARROW UP" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_down_and_space_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks SPACE key on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.send_keys(Keys.SPACE)
                    return True
            except:
                pass

            # Press the "ARROW DOWN" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_up_and_space_click(driver, element_xpath, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks SPACE key on the element and return True of success or False
        end_time = time.time() + waiting_time
        element = None

        while time.time() < end_time:
            try:
                element = WebDriverWait(driver, 0.2).until(
                    EC.visibility_of_element_located((By.XPATH, element_xpath))
                )
                if element.is_displayed():
                    element.send_keys(Keys.SPACE)
                    return True
            except:
                pass

            # Press the "ARROW UP" key
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        return False

    @staticmethod
    def make_displayed_with_arrow_down_and_send(driver, element_xpath, send_text, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and send text = send_text in elemet of type "input" with element's xpath = element_xpath and return True or text of error
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Send on the element send_text
                        element.send_keys(send_text)
                        break
                    stop_time = datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            # Return True if the element is displayed and send successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

    @staticmethod
    def make_displayed_with_arrow_up_and_send(driver, element_xpath, send_text, waiting_time):
        # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and send text = send_text in elemet of type "input" with element's xpath = element_xpath and return True or text of error
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Send on the element send_text
                        element.send_keys(send_text)
                        break
                    stop_time = datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            # Return True if the element is displayed and send successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

    @staticmethod
    def find_href_on_page(driver, find_href):
        # - finds href = find_href on page and return True or text of error
        try:
            # Find all anchor elements on the page
            anchor_elements = driver.find_elements_by_tag_name("a")

            # Check if the href is present in any anchor element
            for anchor in anchor_elements:
                try:
                    if anchor.get_attribute("href") == find_href:
                        return True
                except NoSuchElementException:
                    pass

            # Return False if the href is not found
            return False

        except Exception as e:
            return str(e)

    @staticmethod
    def wait_for_element_to_disappear(driver, element_xpath, waiting_time):
        # - during the waiting time, time = waiting_time waits for the element with xpath = element_xpath to disappear and return True or text of error
        try:
            # Wait for the element to disappear
            wait = WebDriverWait(driver, waiting_time)  # Maximum wait time in seconds
            wait.until(EC.invisibility_of_element_located((By.XPATH, element_xpath)))
            # Return True once the element has disappeared
            return True

        except Exception as e:
            return str(e)

    @staticmethod
    def wait_for_element_to_appear(driver, element_xpath, waiting_time):
        # - during the waiting time, time = waiting_time waits for the element with xpath = element_xpath to appear and return True or text of error
        try:
            # Wait for the element to appear
            wait = WebDriverWait(driver, waiting_time)  # Maximum wait time in seconds
            wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
            # Return True once the element has appeared
            return True

        except Exception as e:
            return str(e)

    @staticmethod
    def check_text_in_class(driver, element_xpath, class_text):
        # - checks to exist text = class_text in class of element with xpath = element_xpath and return True of success or False
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            class_attribute = element.get_attribute('class')
            if class_text in class_attribute:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    @staticmethod
    def double_click_element(driver, element_xpath):
        # - makes double click on element with xpath = element_xpath and return True or text of error
        try:
            # Find the element by XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Perform a double click on the element
            actions = ActionChains(driver)
            actions.double_click(element).perform()

            # Return True once the double click is performed
            return True

        except Exception as e:
            return str(e)

    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def click_ok_in_alert(driver, waiting_time):
        # - during the waiting time, time = waiting_time waits and clicks on the "Ok" of alert window and return True or text of error
        try:
            # Wait for the alert to appear
            wait = WebDriverWait(driver, waiting_time)  # Adjust the timeout value as needed
            alert = wait.until(EC.alert_is_present())

            # Switch to the alert and accept it (click "OK")
            # alert = browser.switch_to.alert
            # alert.accept()
            Alert(driver).accept()
            return True  # Clicked the "OK" button successfully

        except NoAlertPresentException:
            return "No alert window present"

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

    @staticmethod
    def click_ok_button_modal_footer(driver):
        # - clicks on the "Ok" of modal footer and return True or text of error
        try:
            original_timeout = driver.get_timeout()
            # Wait for the modal to appear
            wait = WebDriverWait(driver, original_timeout)
            modal_footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-footer")))

            # Find the "OK" button within the modal footer
            ok_button = modal_footer.find_element(By.XPATH, ".//button[text()='OK']")

            # Click the "OK" button
            ok_button.click()

            # Do something else after clicking the button...

            return True  # Return True if the button is clicked successfully

        except NoSuchElementException as e:
            return str(e)  # Return the error's text if the button is not found

        except Exception as e:
            return str(e)  # Return the error's text if any other exception occurs

    @staticmethod
    def get_chrome_default_download_folder():
        # - gets path to the downloads folder in Google Chrome and return path or text of error
        try:
            output = subprocess.check_output(['xdg-user-dir', 'DOWNLOAD'], universal_newlines=True)
            download_folder = output.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "Error: Could not get the path to the downloads folder in Google Chrome"

        # Проверить, существует ли папка загрузок
        if not os.path.isdir(download_folder):
            return "Error: The downloads folder in Google Chrome was not found"

        # folder_name = os.path.basename(download_folder)

        return download_folder  # , folder_name

    @staticmethod
    def get_last_modified_file(folder):
        # - gets last modifierd file in folder and return file name or text of error
        try:
            # Get the list of files in the specified folder
            files = os.listdir(folder)

            # Filter out directories from the list
            files = [f for f in files if os.path.isfile(os.path.join(folder, f))]

            # Sort the files based on modification time
            files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)

            if files:
                # Retrieve the name of the last modified file
                last_modified_file = files[0]
                return last_modified_file  # Return the last modified file name and no error message
            else:
                return None  # "No files found in the folder"
        except Exception as e:
            return str(e)  # Return the error message

    @staticmethod
    def get_path_separator():
        # - returns the character used by the operating system to separate path elements. For Windows – ‘\\’
        return os.sep

    @staticmethod
    def check_page_errors(driver):
        # - checks for errors on the browser page on the Console and Network tab in the Developer Panel (F12 key)
        try:
            current_url = driver.current_url
            driver.get(current_url)

            console_logs = driver.get_log("browser")
            network_entries = driver.execute_script("return window.performance.getEntries()")

            console_errors = []
            network_errors = []

            for log in console_logs:
                if log["level"] == "SEVERE":
                    console_errors.append(log["message"])

            for entry in network_entries:
                if entry["response"]["status"] >= 400:
                    network_errors.append(entry["name"])

            if console_errors or network_errors:
                return console_errors + network_errors
            else:
                return "OK"

        except Exception as e:
            # Handle any exceptions that may occur
            print(f"An error occurred: {str(e)}")

    @staticmethod
    def return_all_errors_on_page(url):
        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, "html.parser")

                # Find all the exception elements on the page (modify as per your HTML structure)
                exception_elements = soup.find_all(class_="exception")

                # Loop through the exception elements and print their text
                for exception in exception_elements:
                    return exception.text
            else:
                return "Request was not successful. Status code:", response.status_code

        except requests.exceptions.RequestException as e:
            return "An error occurred: " + str(e)

    @staticmethod
    def is_element_clickable(driver, xpath):
        # - checks the clickability of this element
        try:
            element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            return True
        except:
            return False

    @staticmethod
    def is_element_present(driver, xpath):
        # - checks for element presence
        try:
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            if element.is_displayed():
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def set_implicit_waiting_time(driver, time_in_second):
        # - sets an implicit timeout
        driver.implicitly_wait(time_in_second)

    @staticmethod
    def get_input_value(driver, input_xpath):
    # - gets the element's input value with element's xpath = input_xpath

        try:
            # Find element by XPath
            input_element = driver.find_element(By.XPATH, input_xpath)

            # Get field value
            input_value = input_element.get_attribute('value')

            return input_value

        except Exception as e:
            # If there is an error, return False
            print(f"Error: {e}")
            return False

    @staticmethod
    def get_separator():
    # get system's separator in files path (It is for example for Windows "\", for Linux "/")
        return os.altsep

    @staticmethod
    def change_element_text(driver, span_xpath, new_text):
        # Modify the innerHTML of an element identified by XPath.
        # Parameters:
        # - driver: Selenium WebDriver instance.
        # - element_xpath: XPath expression to locate the element.
        # - new_text: The new text to set as innerHTML.
        # Example usage:
        # modify_element_text(browser, "//div[@class='example']", "New Text")

        try:
            element = driver.find_element(By.XPATH, span_xpath)
            driver.execute_script('arguments[0].innerHTML = arguments[1];', element, new_text)
            print(f"Element at XPath '{span_xpath}' modified successfully.")
            return True
        except Exception as e:
            message = f"An error occurred: {e}"
            print(message)
            return message

    @staticmethod
    def delete_disable_attribute(driver, element_xpath):
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            driver.execute_script("arguments[0].removeAttribute('disabled');", element)
            print(f"Element with XPath '{element_xpath}' enabled now.")
            return  True
        except Exception as e:
            message = f"An error occurred: {e}"
            print(message)
            return message
            

    @staticmethod
    def get_text_list_in_select(driver, select_xpath):
        try:
            #Find the select element by its xpath
            select_element = driver.find_element(By.XPATH, select_xpath)

            # Get all option elements inside the select
            options = select_element.find_elements(By.TAG_NAME, "option")

            # Create an empty list to store the text values
            text_values_list = []

            # Extract text from each option element and add it to the list
            for option in options:
                text_values_list.append(option.text)

            # Return this list
            return text_values_list

        except NoSuchElementException:
            # If the element is not found, return an error code
            return f"Element with xpath {select_xpath} not found"
        except Exception as e:
            # If other errors occur, return an error message
            return f"An error occurred: {e}"

    @staticmethod
    def get_all_cookies(driver):
        # - this method receives all cookies
        try:
            # Get all cookies
            cookies = driver.get_cookies()
            return cookies
        except Exception as e:
            # If other errors occur, return an error message
            return f"Error: {str(e)}"

    @staticmethod
    def set_cookies(driver, cookies_dict):
        # - this method installs cookies from cookies_dict
        try:
            # Set cookies
            driver.add_cookie(cookies_dict)
            return True
        except Exception as e:
            # If other errors occur, return an error message
            return f"Error: {str(e)}"

    @staticmethod
    def delete_cookies(driver, cookies_key):
        # - this method deletes cookies by cookies_key
        try:
            # Delete cookies
            driver.delete_cookie(cookies_key)
            return True
        except Exception as e:
            # If other errors occur, return an error message
            return f"Error: {str(e)}"

    @staticmethod
    def insert_from_clipboard(browser, input_xpath):
    # This method for inserting text from the clipboard into the input field
    # on a web page in the field with xpath = input_xpath
        try:
            # Check permission to read from the buffer in the browser
            browser.execute_script(
                "navigator.permissions.query({name: 'clipboard-read'}).then(permissionStatus => "
                "{if (permissionStatus.state == 'denied') {console.log('Permission to read clipboard denied.');}});")

            rezult = MrFixUI.click_element_by_xpath(browser, input_xpath)
            if rezult != True: return "Checking permission to read from the buffer in the browser - False"

            # Simulating keystrokes to copy text
            actions = ActionChains(browser)
            actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            return True

        except Exception as e:
            # If other errors occur, return an error message
            return f"Error: {str(e)}"

    @staticmethod
    def scroll_to_element(browser, xpath):
        """
        Finds an element by the specified XPath and smoothly scrolls to it.

        :param browser: WebDriver - Selenium browser object.
        :param xpath: str - XPath of the element to scroll to.
        """
        try:
            # Find the element
            element = browser.find_element(By.XPATH, xpath)
            # Scroll to the element
            browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
            return True
        except Exception as e:
            # Handle errors
            print(f"Error while scrolling to the element: {e}")

    @staticmethod
    def intercept_failed_requests_after_click(driver, element_xpath, wait_time=10):
        """
        Clicks a element on a web page and intercepts requests with errors (4xx, 5xx) for a specified duration.

        :param element_xpath: XPath selector for the element to click.
        :param wait_time: Time in seconds to intercept requests.
        :param driver: It is a variable of the Selenium Webdriver type.
        :return: Tuple (driver, message: str, errors: list)
        """
        try:
            # Wait for the button to be clickable and click it
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()

            # Start intercepting requests
            print(f"Intercepting requests with errors for {wait_time} seconds...")
            start_time = time.time()

            error_requests = []

            while time.time() - start_time < wait_time:
                # Intercept requests and filter by response status
                for request in driver.requests:
                    if request.response and 400 <= request.response.status_code < 600:
                        error_requests.append({
                            "url": request.url,
                            "method": request.method,
                            "status_code": request.response.status_code,
                            "response_headers": dict(request.response.headers),
                            "response_body": request.response.body.decode("utf-8", errors="ignore"),
                        })

            # Check for errors and return appropriate message
            if error_requests:
                message = "Errors detected!"
                return driver, message, error_requests
            else:
                message = "No errors in Network and Console."
                return driver, message, []

        except Exception as e:
            return driver, f"An error occurred: {str(e)}", []

    @staticmethod
    def check_Console_and_Network_errors(browser, url):
        try:
            # Enabling network log interception (Chrome DevTools Protocol)
            browser.execute_cdp_cmd("Network.enable", {})

            # Opening the page
            browser.get(url)

            # We get errors from the browser console
            logs = browser.get_log("browser")
            console_errors = [entry["message"] for entry in logs if "SEVERE" in entry["level"]]

            # We get network errors (HTTP 4xx и 5xx)
            network_errors = []
            performance_logs = browser.get_log("performance")  # Taking away all network events

            for entry in performance_logs:
                log_message = json.loads(entry["message"])["message"]

                if log_message["method"] == "Network.responseReceived":  # Filtering the necessary events
                    response = log_message["params"]["response"]
                    status = response["status"]
                    url = response["url"]

                    if 400 <= status < 600:  # Filtering all 4xx and 5xx errors
                        network_errors.append(f"URL: {url} | Status: {status}")

            # If there are no errors, we return True
            if not console_errors and not network_errors:
                return True

            # Returning a list of errors
            return {"console_errors": console_errors, "network_errors": network_errors}

        except Exception as e:
            return {"error": str(e)}


class MrFixSQL:

    @staticmethod
    def run_openvpn_commands(ovpn_file):
        try:
            # Stop the OpenVPN service
            stop_command = "sudo systemctl stop openvpn@server"
            subprocess.run(stop_command, shell=True, check=True)

            # Enable the OpenVPN service
            enable_command = "sudo systemctl enable openvpn@server.service"
            subprocess.run(enable_command, shell=True, check=True)

            # Start OpenVPN client with the specified configuration file
            config_file = ovpn_file
            openvpn_command = f"sudo openvpn --client --config {config_file}"
            subprocess.run(openvpn_command, shell=True, check=True)

            # If all commands succeed, return True
            return True

        except subprocess.CalledProcessError as e:
            # If any command fails, return the error message
            return f"Error: {e}"



    @staticmethod
    # Launches OpenVPN with a command with administrator privileges on the Linux command line using the ".ovpn" settings file
    # Returns a success message or error text
    def run_openvpn_for_linux(config_path: str, pas: str):
        try:
            with sh.contrib.sudo(pas, _with=True):
                rezult = subprocess.run(['sudo', '-S', 'openvpn', '--client', '--config', config_path])

            return rezult.stderr

        except FileNotFoundError:
            return "OpenVPN executable not found. Please ensure it is installed and in your system's PATH."

        except subprocess.CalledProcessError as e:
            return f"OpenVPN connection failed with error: {e}"


    @staticmethod
    # Launches OpenVPN with a command with administrator privileges on the Windows command line using the ".ovpn" settings file
    # Returns a success message or error text
    def run_openvpn_for_Windows(config_path: str, pas: str):
        try:
            args = ['openvpn', '--client', '--config', config_path]
            subprocess.run(args, input=pas, check=True, text=True)
            return "OpenVPN connection established."

        except FileNotFoundError:
            return "OpenVPN executable not found. Please ensure it is installed and in your system's PATH."

        except subprocess.CalledProcessError as e:
            return f"OpenVPN connection failed with error: {e}"


    @staticmethod
    # Launches OpenVPN with a command with administrator privileges on the Windows 11 command line using the ".ovpn" settings file
    # Returns a success message or error text
    def run_openvpn_for_Windows_11(config_path: str, pas: str):
        try:
            rezult = subprocess.run(['openvpn', '--config', config_path], input=pas, encoding='utf-8',
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            return rezult.stderr

        except FileNotFoundError:
            return "OpenVPN executable not found. Please ensure it is installed and in your system's PATH."

        except subprocess.CalledProcessError as e:
            return f"OpenVPN connection failed with error: {e}"


    @staticmethod
    # Stops OpenVPN with a command with administrator privileges on the Linux command line
    # Returns a success message or error text
    def stop_openvpn_for_linux(pas: str):
        try:
            # Use the appropriate command to stop OpenVPN
            password = pas
            with sh.contrib.sudo(password, _with=True):
                subprocess.call(['sudo', 'service', 'openvpn', 'stop'])  # Example command for Linux

            # If you're using a different operating system, you might need to use a different command
            # For example, on Windows, you could use subprocess.call(['taskkill', '/F', '/IM', 'openvpn.exe'])

            return "OpenVPN stopped successfully."

        except Exception as e:
            return f"An error occurred while stopping OpenVPN: {e}"


    @staticmethod
    # Stops OpenVPN with a command with administrator privileges on the Windows command line
    # Returns a success message or error text
    def stop_openvpn_for_Windows(pas: str):
        try:
            # Use the appropriate command to stop OpenVPN
            password = pas
            args = ['taskkill', '/F', '/IM', 'openvpn.exe']
            subprocess.run(args, input=password, check=True, text=True)
            return "OpenVPN stopped successfully."

        except subprocess.CalledProcessError as e:
            return f"An error occurred while stopping OpenVPN: {e}"



    @staticmethod
    # из таблицы в базе данных PostgreSQL получает все данные по SQL-запросу и сохраняет их в текстовый файл
    # From a table in the database, PostgreSQL gets all the data for the SQL query and saves it to a text file
    # (name the file and the full path to it are in txt_file_path). The table is defined by the sql_query SQL query.
    # The database access parameters are specified in the connection_data dictionary in the values
    # of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    def export_SQL_request_result_table_to_text_file(connection_data: dict, sql_query: str, txt_file_path: str):
        global connection
        global cursor
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=connection_data['host'],
                port=connection_data['port'],
                database=connection_data['database'],
                user=connection_data['user'],
                password=connection_data['password']
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Retrieve all data from the specified table
            cursor.execute(sql_query)
            data = cursor.fetchall()

            # Save the data to a text file
            with open(txt_file_path, 'w') as file:
                for row in data:
                    file.write(','.join(str(value) for value in row))
                    file.write('\n')

            return f"Data from table exported to '{txt_file_path}' successfully."

        except psycopg2.Error as e:
            return f"Error accessing the PostgreSQL database: {e}"

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


    @staticmethod
    # экспорт таблицы из PostgreSQL в csv-файл
    # Exports a table from PostgreSQL to a csv file
    # (name the file and the full path to it are in csv_file_path). The table is defined by the sql_query SQL query.
    #  The database access parameters are specified in the connection_data dictionary in the values
    #  of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    def export_SQL_request_result_table_to_csv_file(connection_data: dict, sql_query: str, table_name: str, csv_file_path: str):
        global connection
        global cursor
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host = connection_data['host'],
                port = connection_data['port'],
                database = connection_data['database'],
                user = connection_data['user'],
                password = connection_data['password']
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Select all rows from the table
            cursor.execute(sql_query)

            # Fetch all rows
            rows = cursor.fetchall()

            # Get the column names
            column_names = [desc[0] for desc in cursor.description]

            # Write the data to the CSV file
            with open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                # Write the column names as the first row
                writer.writerow(column_names)
                # Write the data rows
                writer.writerows(rows)

            return f"Data from table '{table_name}' exported to '{csv_file_path}' successfully."

        except psycopg2.Error as e:
            return f"Error accessing the PostgreSQL database: {e}"

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


    @staticmethod
    # SQL-запрос на несколько строк со вставкой данных в таблицу
    # Performs the insertion of several rows of data "data" in PostgreSQL using sql_query SQL query.
    # The database access parameters are specified in the connection_data dictionary in the values
    # of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    def insert_data_in_postgesql(connection_data: dict, sql_query: str, data: str):
        global connection
        global cursor
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=connection_data['host'],
                port=connection_data['port'],
                database=connection_data['database'],
                user=connection_data['user'],
                password=connection_data['password']
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the query for each set of data
            for row in data:
                cursor.execute(sql_query, row)

            # Commit the changes to the database
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return "Insert data successful"

        except (Exception, psycopg2.Error) as error:
            return f"Error inserting data: {error}"

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()



    @staticmethod
    #  изменяет одну запись в таблице и сообщает о результате выполнения (успешно или ошибка)
    # Changes record in PostgreSQL using sql_query SQL query.
    # The database access parameters are specified in the connection_data dictionary in the values
    # of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    def modify_record_in_postgesql(connection_data:dict, sql_query:str):
        global connection
        global cursor
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=connection_data['host'],
                port=connection_data['port'],
                database=connection_data['database'],
                user=connection_data['user'],
                password=connection_data['password']
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the SQL query to modify the record
            cursor.execute(sql_query)

            # Commit the changes to the database
            connection.commit()

            # Check if any rows were affected by the update
            # Check the number of rows affected
            if cursor.rowcount > 0:
                return "Record updated successfully."
            else:
                return "No record found to update."

        except (psycopg2.Error, psycopg2.DatabaseError) as error:
            # Handle the error and return the error message
            return f"Error occurred: {str(error)}"

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()



    @staticmethod
    # Searches for data in PostgreSQL using sql_query SQL query.
    # The database access parameters are specified in the connection_data dictionary in the values
    # of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    def find_record_in_postgresql(connection_data: dict, sql_query: str):

        global connection
        global cursor
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=connection_data['host'],
                port=connection_data['port'],
                database=connection_data['database'],
                user=connection_data['user'],
                password=connection_data['password']
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the query
            cursor.execute(sql_query)

            # Fetch the first record found
            record = cursor.fetchone()

            if record is not None:
                return record
            else:
                return "No record found with the specified parameters."

        except psycopg2.Error as e:
            return f"Error accessing the PostgreSQL database: {e}"

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


class MrFixAPI:

    @staticmethod
    # Makes POST request with used requests_url (requests url), requests_body (requests body),
    # requests_headers (requests_headers) and pre_script (pre-request script, optional)
    # Returns response in JSON file
    def post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None):
    # the method executes the POST request using url = requests_url and header = requests_headers, after executing the pre_script (optional parameter)

        # Execute the pre-script
        if pre_script != None:
            exec(pre_script)

        body = json.dumps(requests_body)
        response = requests.post(requests_url, auth=auth, data=body, headers=requests_headers)

        if response.status_code == 200 or response.status_code == 201:
            print('POST request successful')
            print('Response:', response.text)
            return response.json()
        else:
            print('POST request failed')
            print('Response:', response.text)
            return response.json()


    @staticmethod
    # Makes GET request with used requests_url (requests url), requests_headers (requests_headers)
    # Returns response in JSON file
    def get_request(requests_url: str, requests_headers: dict, auth: list = None):
    # the method executes a GET request using url = requests_url and headers = requests_headers

        # Make the GET request
        response = requests.get(requests_url, auth=auth, params=requests_headers)

        # Process the response
        if response.status_code == 200:
            # Successful request
            print("Request successful!")
            print("Response:", response.text)
            return response.json()
        else:
            # Request failed
            print("Request failed. Status code:", response.status_code)
            return response.json()


    @staticmethod
    # Makes PUT request with used requests_url (requests url), requests_body (requests body),
    # requests_headers (requests_headers) and pre_script (pre-request script, optional)
    # Returns response in JSON format
    def put_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None):
        # the method executes the PUT request using url = requests_url and header = requests_headers,
        # after executing the pre_script (optional parameter)

        # Execute the pre-script
        if pre_script is not None:
            exec(pre_script)

        body = json.dumps(requests_body)
        response = requests.put(requests_url, auth=auth, data=body, headers=requests_headers)

        if response.status_code == 200:
            print('PUT request successful')
            print('Response:', response.text)
            return response.json()
        else:
            print('PUT request failed')
            print('Response:', response.text)
            return response.json()


    @staticmethod
    # Makes DELETE request with used requests_url (requests url) and requests_headers (request headers)
    # Returns response in JSON format
    def delete_request(requests_url: str, requests_headers: dict, auth: list = None):
        # the method executes a DELETE request using url = requests_url and headers = requests_headers

        # Make the DELETE request
        response = requests.delete(requests_url, headers=requests_headers, auth=auth)

        # Process the response
        if response.status_code == 200:
            # Successful request
            print("DELETE request successful!")
            print("Response:", response.text)
            return response.json()
        else:
            # Request failed
            print("DELETE request failed. Status code:", response.status_code)
            print("Response:", response.text)
            return response.json()





class MrFixSecurity:

    @staticmethod
    def is_port_open(host, port):
        # The method checks whether the port number = port (integer value) is open or not
        # Return "True" or "False"

        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Set a timeout for the connection attempt
                s.settimeout(1)
                # Try to connect to the host and port
                s.connect((host, port))
            return True  # Port is open

        except (ConnectionRefusedError, socket.timeout):
            return False  # Port is closed

        except socket.error as e:
            print(f"An error occurred: {e}")
            return False  # Port is closed


    @staticmethod
    def check_open_ports(host, ports_list, timeout=1):
        # The method checks whether each of the ports in the ports_list list is open
        # (contains integer values of port numbers) or not
        # Return a dictonary of type: {<port number> : <status - "open" or "closed">, ...}
        ports_dictonary = {}
        def check_port(host, port, timeout):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(timeout)
                    s.connect((host, port))
                return "open"
            except (ConnectionRefusedError, socket.timeout):
                return "closed"
            except Exception as e:
                return str(e)

        for i in range(len(ports_list)):  # Check all possible ports in ports_list
            result = check_port(host, ports_list[i], timeout)
            if result == "open":
                ports_dictonary[ports_list[i]] = "open"
            elif result == "closed":
                ports_dictonary[ports_list[i]] = "closed"
            else:
                ports_dictonary[ports_list[i]] = f"Error on port {ports_list[i]}: {result}"

        return ports_dictonary


    @staticmethod
    def generate_key(filename):
        # Generate a random encryption key and save the encryption key to a file
        # Return "True" or error's text

        try:
            # Generate a random encryption key
            key = Fernet.generate_key()
            # Save the encryption key to a file
            with open(filename, 'wb') as key_file:
                key_file.write(key)
            return True
        except Exception as e:
            return str(e)

    @staticmethod
    def encrypt_file(input_file, output_file, key_file):
        # Encrypt a file using a given key_file and save the encrypted data to another file
        # Return "True" or error's text

        try:
            # Load the encryption key from a file
            with open(key_file, 'rb') as my_key_file:
                key = my_key_file.read()

            # Encrypt a file and save the encrypted data to another file
            fernet = Fernet(key)
            with open(input_file, 'rb') as file:
                file_data = file.read()
                encrypted_data = fernet.encrypt(file_data)
            with open(output_file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            return True

        except Exception as e:
            return str(e)

    @staticmethod
    def decrypt_file(input_file, output_file, key_file):
        # - Decrypt a file using a given key and save the decrypted data to another file
        # - Return "True" or error's text

        try:
            # Load the encryption key from a file
            with open(key_file, 'rb') as my_key_file:
                key = my_key_file.read()

            # Decrypt a file and save the decrypted data to another file
            fernet = Fernet(key)
            with open(input_file, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()
                decrypted_data = fernet.decrypt(encrypted_data)
            with open(output_file, 'wb') as file:
                file.write(decrypted_data)
            return True

        except Exception as e:
            return str(e)


class MrFixTime:

    @staticmethod
    def get_start_time():
        try:
            start_time = time.time()
            return start_time

        except Exception as e:
            return str(e)

    @staticmethod
    def get_delta_time(start_time):
        try:
            stop_time = time.time()
            delta_time = stop_time - start_time
            return delta_time

        except Exception as e:
            return str(e)


class MrFixLoad:
    @staticmethod
    @pytest.mark.asyncio
    async def make_get_request(url):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                return url, response.text
        except Exception as e:
            return url, f"Error: {str(e)}"

    @staticmethod
    @pytest.mark.asyncio
    async def concurrent_get_requests(urls):
        tasks = [MrFixLoad.make_get_request(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

    @staticmethod
    @pytest.mark.asyncio
    async def load_method_of_get_requests(url, n):
        urls_to_test = [url] * n
        results_of_requests = await MrFixLoad.concurrent_get_requests(urls_to_test)

        # Output of results
        print()
        for url, response_text in results_of_requests:
            s = f"URL: {url}, Response: {response_text}"
            print(f'Count = {n},  {s}')

    @staticmethod
    async def run_load_method_of_get_requests(requests_url, count):
        await MrFixLoad.load_method_of_get_requests(requests_url, count)

    @staticmethod
    async def run_load_method_of_get_requests_in_range(min_count: int, max_count: int, step: int, url: str):
        for i in range(min_count, max_count, step):
            await MrFixLoad.run_load_method_of_get_requests(url, i)

    @staticmethod
    @pytest.mark.asyncio
    async def make_post_request(url, headers: dict, body: dict):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, data=body)
                response.raise_for_status()  # Raise an error for bad responses
                return url, response.text
        except Exception as e:
            return url, f"Error: {str(e)}"

    @staticmethod
    @pytest.mark.asyncio
    async def concurrent_post_requests(urls, headers: dict , body: dict):
        tasks = [MrFixLoad.make_post_request(url, headers=headers, body=body) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

    @staticmethod
    @pytest.mark.asyncio
    async def load_method_of_post_requests(url, n, headers: dict, body: dict):
        urls_to_test = [url] * n
        results_of_requests = await MrFixLoad.concurrent_post_requests(urls_to_test, headers=headers, body=body)

        # Output of results
        print()
        for url, response_text in results_of_requests:
            s = f"URL: {url}, Response: {response_text}"
            print(f'Count = {n}, {s}')

    @staticmethod
    async def run_load_method_of_post_requests(requests_url, count, headers: dict, body: dict):
        await MrFixLoad.load_method_of_post_requests(requests_url, count, headers=headers, body=body)

    @staticmethod
    async def run_load_method_of_post_requests_in_range(min_count: int, max_count: int, step: int, url: str,
                                                        headers: dict, body: dict):
        for i in range(min_count, max_count, step):
            await MrFixLoad.run_load_method_of_post_requests(url, i, headers=headers, body=body)


class MrBrowserManager:
    def __init__(self, config_browser='chrome', width="1920", high="1080", wait_time=20, headless=False):
        self.config_browser = config_browser
        self.width = width
        self.high = high
        self.headless = headless
        self.wait_time = wait_time
        self.driver = None

    def get_driver(self, width, high, headless):
        directory = os.path.abspath(os.curdir)

        # Initialize the driver based on the selected browser
        if self.config_browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.set_capability("goog:loggingPrefs", {
                "browser": "ALL",
                "performance": "ALL"  # Enabling network log interception
            })
            service = Service()
            downloads_path = os.path.join(str(pathlib.Path.cwd()), 'downloads')

            # Set preferences for Chrome, such as download directory and security settings
            prefs = {
                "download.default_directory": downloads_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument(f"--window-size={width},{high}")

            # Enable headless mode if specified
            if headless:
                options.add_argument('--headless')

            # Set path to Chrome binary if the OS is not Windows
            if os.name != 'nt':
                options.binary_location = '/opt/google/chrome'

            # Create Chrome driver with specified options
            self.driver = webdriver.Chrome(service=service, options=options)

        elif self.config_browser == 'firefox':
            options = webdriver.FirefoxOptions()

            # Enable reading from clipboard in Firefox
            options.add_argument("--enable-features=ClipboardReadWrite")

            # Set download preferences for Firefox
            options.set_preference("browser.download.dir", directory)
            options.set_preference("browser.download.folderList", 2)  # Use custom download directory
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            options.add_argument(f'--width={width}')
            options.add_argument(f'--height={high}')

            # Set path to Firefox binary if the OS is not Windows
            if os.name != 'nt':
                options.binary_location = '/usr/bin/firefox'

            # Create Firefox driver with specified options
            self.driver = webdriver.Firefox(options=options)
        else:
            # Raise an error if an unsupported browser is specified
            raise Exception(f'"{self.config_browser}" is not a supported browser')

        # Set an implicit wait for the driver
        self.driver.implicitly_wait(self.wait_time)
        return self.driver

    def quit_driver(self):
        # Quit the driver if it exists
        if self.driver:
            self.driver.quit()


class MrLoggerHelper:
    @staticmethod
    @pytest.fixture(autouse=True)
    def add_logger(request):
        # Configuration for logging
        Rep = pathlib.Path.cwd()
        Repoz = str(Rep)
        logs_catalog = os.path.join(Repoz, 'logs')
        prefix_name = 'log_'
        today = str(datetime.today())

        if os.name == 'nt':
            today = today.replace(':', '_')

        logger.info('# Setting the log file name')
        main_test_file = os.path.basename(request.module.__file__)

        global log_file_name
        log_file_name = os.path.join(logs_catalog, f"{main_test_file}---{prefix_name}{today}.txt")

        logger.remove()
        logger.add(log_file_name, level='INFO', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
        logger.info('# Recording test start date and time: ' + datetime.today().strftime('%d.%m.%Y'))

        logger_instance = logger
        os.environ['test_status'] = '0'
        os.environ['test_case_id'] = ''

        yield logger_instance

        # Additional actions to complete the test
        pass

class MrPerformance:
    @staticmethod
    def convert_curl_to_postman(input_folder=os.path.join(".", "PerformanceTestsData"),
                                output_folder=os.path.join(".", "PerformanceTestsData"),
                                input_filename='curl.txt'):

        import os
        import json
        from urllib.parse import urlparse

        # Reading the original curl.txt file
        input_path_curl = os.path.join(input_folder, input_filename)
        if not os.path.exists(input_path_curl):
            raise FileNotFoundError(f"Input file not found: {input_path_curl}")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with open(input_path_curl, 'r') as file:
            curl_data = file.read()

        requests = []
        variables = {}

        curl_blocks = [block.strip() for block in curl_data.strip().split('curl') if block.strip()]

        for block in curl_blocks:
            lines = block.strip().split('\\')
            method = 'GET'
            url = ''
            headers = {}
            body = None

            for line in lines:
                line = line.strip()
                if line.startswith('-X'):
                    method = line.split(' ', 1)[1].strip()
                elif line.startswith('-H'):
                    header = line[3:].strip().split(':', 1)
                    headers[header[0].strip()] = header[1].strip()
                elif line.startswith('-d'):
                    raw_body = line[3:].strip()
                    try:
                        body = json.loads(raw_body)
                    except json.JSONDecodeError:
                        body = raw_body.strip("'")
                else:
                    if not url:
                        url = line.strip()

            # Parse and replace variables in URL
            parsed_url = urlparse(url)
            url_var_name = "base_url"
            variables[url_var_name] = parsed_url.netloc
            url_with_variable = url.replace(parsed_url.netloc, f"{{{{{url_var_name}}}}}")

            # Replace headers values with variables
            cleaned_headers = {}
            for key, value in headers.items():
                clean_key = key.strip("'").strip()  # Удаляем апострофы из ключей
                header_var_name = clean_key.lower().replace('-', '_')
                clean_value = value.strip("'").strip()  # Удаляем апострофы из значений
                variables[header_var_name] = clean_value
                cleaned_headers[clean_key] = f"{{{{{header_var_name}}}}}"
            headers = cleaned_headers

            # Replace body values with variables if it's a JSON object
            if body and isinstance(body, dict):
                for key, value in body.items():
                    body_var_name = key.lower()
                    variables[body_var_name] = value
                    body[key] = f"{{{{{body_var_name}}}}}"

            # Add request in JSON format
            requests.append({
                "name": parsed_url.path.split('/')[-1] or "Request",
                "request": {
                    "method": method,
                    "header": [
                        {"key": k, "value": v} for k, v in headers.items()
                    ],
                    "body": {
                        "mode": "raw",
                        "raw": json.dumps(body, ensure_ascii=False, indent=2) if isinstance(body, dict) else body
                    },
                    "url": {
                        "raw": url_with_variable,
                        "protocol": parsed_url.scheme,
                        "host": [f"{{{{{url_var_name}}}}}"],
                        "path": parsed_url.path.strip('/').split('/')
                    }
                }
            })

        # Saving a collection of queries
        postman_collection_file = os.path.join(output_folder, "postman_collection.json")
        postman_collection = {
            "info": {
                "name": "Converted Collection",
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": requests
        }

        with open(postman_collection_file, 'w') as file:
            json.dump(postman_collection, file, indent=2)

        # Saving variables
        postman_environment_file = os.path.join(output_folder, "postman_environment.json")
        postman_environment = {
            "id": "environment_id",
            "name": "Converted Environment",
            "values": [
                {"key": key, "value": value, "enabled": True} for key, value in variables.items()
            ]
        }

        with open(postman_environment_file, 'w') as file:
            json.dump(postman_environment, file, indent=2)


    @staticmethod
    def install_newman():
        """
        Universal method for installing Node.js, npm, and Newman on any OS (Windows, Linux, macOS).
        """

        def is_tool_installed(tool):
            """
            Checks if a tool (Node.js, npm, or Newman) is installed.
            """
            try:
                subprocess.run([tool, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                return True
            except (OSError, subprocess.CalledProcessError):
                return False

        def install_nodejs():
            """
            Automatically installs Node.js depending on the OS.
            """
            if sys.platform.startswith("win"):
                print("Installing Node.js for Windows...")
                node_installer_url = "https://nodejs.org/dist/v18.18.2/node-v18.18.2-x64.msi"
                installer_path = os.path.join(os.getcwd(), "node_installer.msi")
                subprocess.run(["curl", "-o", installer_path, node_installer_url], check=True)
                subprocess.run(["msiexec", "/i", installer_path, "/quiet", "/norestart"], check=True)
                os.remove(installer_path)
            elif sys.platform.startswith("darwin"):
                print("Installing Node.js for macOS...")
                subprocess.run(["brew", "install", "node"], check=True)
            elif sys.platform.startswith("linux"):
                print("Installing Node.js for Linux...")
                distro = subprocess.run(["lsb_release", "-is"], stdout=subprocess.PIPE).stdout.decode().strip().lower()
                if distro in ["ubuntu", "debian"]:
                    subprocess.run(["sudo", "apt", "update"], check=True)
                    subprocess.run(["sudo", "apt", "install", "-y", "nodejs"], check=True)
                elif distro in ["centos", "fedora", "redhat"]:
                    subprocess.run(["sudo", "dnf", "install", "-y", "nodejs"], check=True)
                elif distro == "arch":
                    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "nodejs"], check=True)
                else:
                    print("Unknown Linux distribution. Please install Node.js manually from https://nodejs.org/")
                    sys.exit(1)
            else:
                print("Unknown operating system. Please install Node.js manually from https://nodejs.org/")
                sys.exit(1)

        def install_npm():
            """
            Installs npm if it is missing, depending on the OS.
            """
            if sys.platform.startswith("win"):
                print("npm should have been installed with Node.js. Please check your Node.js installation.")
                sys.exit(1)
            elif sys.platform.startswith("darwin"):
                print("Reinstalling npm for macOS...")
                subprocess.run(["brew", "install", "npm"], check=True)
            elif sys.platform.startswith("linux"):
                print("Reinstalling npm for Linux...")
                distro = subprocess.run(["lsb_release", "-is"], stdout=subprocess.PIPE).stdout.decode().strip().lower()
                if distro in ["ubuntu", "debian"]:
                    subprocess.run(["sudo", "apt", "install", "-y", "npm"], check=True)
                elif distro in ["centos", "fedora", "redhat"]:
                    subprocess.run(["sudo", "dnf", "install", "-y", "npm"], check=True)
                elif distro == "arch":
                    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "npm"], check=True)
                else:
                    print("Unknown Linux distribution. Please install npm manually from https://www.npmjs.com/")
                    sys.exit(1)
            else:
                print("Unknown operating system. Please install npm manually from https://www.npmjs.com/")
                sys.exit(1)

        # Check for Node.js
        if not is_tool_installed("node"):
            print("Node.js not found! Installing Node.js...")
            install_nodejs()

        # Check for npm
        if not is_tool_installed("npm"):
            print("npm not found! Installing npm...")
            install_npm()

        # Check for Newman
        if not is_tool_installed("newman"):
            print("Newman not found! Installing Newman...")
            try:
                subprocess.run(["npm", "install", "-g", "newman"], check=True)
                print("Newman successfully installed!")
            except subprocess.CalledProcessError as e:
                print(f"Error installing Newman: {e}")
                sys.exit("Failed to install Newman.")
        else:
            print("Newman is already installed.")

    @staticmethod
    def performance_testing_with_postman_collections(
            collection_path=os.path.join(".", "PerformanceTestsData", "postman_collection.json"),
            environment_path=os.path.join(".", "PerformanceTestsData", "postman_environment.json"),
            log_file_path=os.path.join(".", "PerformanceTestsLogs", "performance_test.log"),
            result_file_path=os.path.join(".", "PerformanceTestsResult",
                                          "performance_testing_result.txt"),
            requests_per_second=2, total_requests=10, mode="AABB", max_task=2):
        output_dir = os.path.join(".", "PerformanceRequests")

        # Check if the result file exists, and create it if not
        if not os.path.exists(result_file_path):
            os.makedirs(os.path.dirname(result_file_path), exist_ok=True)
            with open(result_file_path, "w") as file:
                file.write("Performance Testing Results\n")

        # The performance_testing_with_postman_collections method performs load testing of APIs using Newman
        # for Postman collections. It automatically simulates API requests, measures performance,
        # logs request successes and failures, and generates statistics.
        # It supports two request execution modes (AABB and ABAB) and saves results in reports for analysis.

        def setup_output_directory():
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)
            os.makedirs(output_dir)

        async def run_newman(request_name, request_index):
            """Asynchronous call to Newman with logging."""
            request_output_path = os.path.join(output_dir, f"newman_output_{request_name}_{request_index}.json")
            command = [
                "newman", "run", collection_path,
                "-e", environment_path,
                "--reporters", "json",
                "--reporter-json-export", request_output_path
            ]
            async with semaphore:
                start_time = datetime.now()
                if statistics[request_name]["start_time"] is None:
                    statistics[request_name]["start_time"] = start_time

                print(f"Executing command: {' '.join(command)} for request '{request_name}'")
                try:
                    process = await asyncio.create_subprocess_exec(
                        *command,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE
                    )
                    stdout, stderr = await process.communicate()
                    end_time = datetime.now()
                    duration = (end_time - start_time).total_seconds()

                    statistics[request_name]["end_time"] = end_time
                    statistics[request_name]["individual_times"].append(duration)

                    success = process.returncode == 0
                    statistics[request_name]["success" if success else "failure"] += 1

                    # Generate result file name
                    status = "Success" if success else "Fail"
                    timestamp = start_time.strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"{request_name}-{request_index}_{status}_{timestamp}.txt"
                    file_path = os.path.join(output_dir, filename)

                    # Extract request and response data after the current request is executed
                    try:
                        with open(request_output_path, "r") as json_file:
                            data = json.load(json_file)
                            executions = data.get("run", {}).get("executions", [])
                            if executions:
                                request_data = json.dumps(executions[0].get("request", {}), indent=4)
                                response_data = json.dumps(executions[0].get("response", {}), indent=4)
                            else:
                                request_data = "Request data is missing"
                                response_data = "Response data is missing"
                    except (FileNotFoundError, json.JSONDecodeError):
                        request_data = "Result file is missing or corrupted"
                        response_data = "Result file is missing or corrupted"

                    # Save data to a file
                    with open(file_path, "w") as file:
                        file.write("Request:\n")
                        file.write(request_data + "\n\n")
                        file.write("Response:\n")
                        file.write(response_data + "\n")

                    if not success:
                        print(f"[ERROR] Newman failed for request '{request_name}'. Return code: {process.returncode}")
                        with open(log_file_path, "a") as log_file:
                            log_file.write(stderr.decode() + "\n")
                except Exception as e:
                    statistics[request_name]["failure"] += 1
                    print(f"[CRITICAL ERROR] Error executing request '{request_name}': {e}")
                finally:
                    # Remove temporary result file
                    if os.path.exists(request_output_path):
                        os.remove(request_output_path)

        async def main():
            """Main method to manage the load."""
            if requests_per_second <= 0:
                print("[CRITICAL ERROR] The value of requests_per_second must be greater than 0.")
                return

            interval = 1 / requests_per_second
            start_time = datetime.now()

            total_request_types = len(request_names)
            if total_request_types == 0:
                print("[CRITICAL ERROR] The collection does not contain any requests.")
                return

            requests_per_type = total_requests

            if mode == "AABB":
                # Execute all requests of one type, then another
                for request_name in request_names:
                    remaining_requests = requests_per_type
                    request_index = 1
                    while remaining_requests > 0:
                        current_batch_size = min(max_task, remaining_requests)
                        tasks = [run_newman(request_name, request_index + i) for i in range(current_batch_size)]
                        await asyncio.gather(*tasks)
                        request_index += current_batch_size
                        remaining_requests -= current_batch_size
                        await asyncio.sleep(interval)

            elif mode == "ABAB":
                # Alternate requests of different types
                remaining_requests = {name: requests_per_type for name in request_names}
                request_indices = {name: 1 for name in request_names}
                while any(count > 0 for count in remaining_requests.values()):
                    for request_name in request_names:
                        if remaining_requests[request_name] > 0:
                            current_batch_size = min(max_task, remaining_requests[request_name])
                            tasks = [run_newman(request_name, request_indices[request_name] + i) for i in
                                     range(current_batch_size)]
                            await asyncio.gather(*tasks)
                            request_indices[request_name] += current_batch_size
                            remaining_requests[request_name] -= current_batch_size
                            await asyncio.sleep(interval)

            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()

            # Final results
            results = generate_results(total_time, total_requests * total_request_types)
            print("".join(results))
            with open(result_file_path, "w") as file:
                file.writelines(results)

        def generate_results(total_time, total_requests):
            """Generate the final report."""
            results = [f"Total real execution time for all requests: {total_time:.2f} seconds\n"]
            results.append(f"Total requests: {total_requests}\n")
            for request_name, stats in statistics.items():
                avg_time = (sum(stats["individual_times"]) / len(stats["individual_times"])) if stats[
                    "individual_times"] else 0
                min_time = min(stats["individual_times"], default=0)
                max_time = max(stats["individual_times"], default=0)

                results.append(f"Request '{request_name}':\n")
                results.append(f"  Successful: {stats['success']}, Failures: {stats['failure']}\n")
                results.append(f"  Average execution time: {avg_time:.2f} sec\n")
                results.append(f"  Minimum execution time: {min_time:.2f} sec\n")
                results.append(f"  Maximum execution time: {max_time:.2f} sec\n")
            return results

        # Configuration
        setup_output_directory()
        MAX_CONCURRENT_TASKS = max(max_task, requests_per_second)
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
        statistics = defaultdict(
            lambda: {"success": 0, "failure": 0, "individual_times": [], "start_time": None, "end_time": None})

        try:
            with open(collection_path, "r") as file:
                collection_data = json.load(file)
                request_names = [item["name"] for item in collection_data.get("item", [])]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"[CRITICAL ERROR] Error loading collection: {e}")
            return

        asyncio.run(main())









