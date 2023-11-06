import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
import pyperclip
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import subprocess
import psycopg2
import sh
import csv
import socket
from cryptography.fernet import Fernet
import os



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
        return os.sep

    @staticmethod
    def check_page_errors(driver):
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
        try:
            element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            return True
        except:
            return False

    @staticmethod
    def is_element_present(driver, xpath):
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
        driver.implicitly_wait(time_in_second)

    @staticmethod
    def get_input_value(driver, input_xpath):

        try:
            # Найти элемент по XPath
            input_element = driver.find_element(By.XPATH, input_xpath)

            # Получить значение, введенное в поле input
            input_value = input_element.get_attribute('value')

            return input_value

        except Exception as e:
            # Если возникает ошибка, возвращаем False
            print(f"Ошибка: {e}")
            return False

    @staticmethod
    def get_separator():
    # get system's separator in files path (It is for example for Windows "\", for Linux "/")
        return os.altsep


class MrFixSQL:

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
    def post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None):
    # the method executes the POST request using url = requests_url and header = requests_headers, after executing the pre_script (optional parameter)

        # Execute the pre-script
        if pre_script != None:
            exec(pre_script)

        body = json.dumps(requests_body)
        response = requests.post(requests_url, data=body, headers=requests_headers)

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
    def get_request(requests_url: str, requests_headers: dict):
    # the method executes a GET request using url = requests_url and headers = requests_headers

        # Make the GET request
        response = requests.get(requests_url, params=requests_headers)

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







