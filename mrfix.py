import time
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
from datetime import datetime
import sys
import os



class MrFixUI:

    @staticmethod
    def check_exists_xpath(driver, check_xpath):
        # - checks for the presence of an element with xpath=check_xpath on the page at the moment and returns True or False

        original_timeout = driver.get_timeout()
        try:
            driver.implicitly_wait(1)
            # Find the element using XPath
            element = driver.find_element(By.XPATH, check_xpath)

            # If the element is found, return True
            return True
        except NoSuchElementException:
            # If the element is not found, return False
            return False

        finally:
            driver.implicitly_wait(original_timeout)

    @staticmethod
    def click_element_by_xpath(driver, element_xpath):
        # - performs a click on an element with xpath=element_xpath and returns True or error text
        success = False
        try:
            # Find the element by XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Click the element
            element.click()
            # element.send_keys("\n")

            success = True
            return True  # Click successful

        except NoSuchElementException as e:
            error_message = f"Element not found: {str(e)}"
            return error_message

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def select_from_dropdown_text(driver, dropdown_xpath, dropdown_text):
        # - selects a line with text = dropdown_text from the drop-down list with xpath = dropdown_xpath and returns True or error text
        success = False
        try:
            # Find the dropdown element by XPath
            dropdown = Select(driver.find_element(By.XPATH, dropdown_xpath))

            # Select the option by its text
            dropdown.select_by_visible_text(dropdown_text)
            success = True
            return True  # Option selected successfully

        except NoSuchElementException as e:
            error_message = f"Element not found: {str(e)}"
            return error_message

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def send_text_to_input(driver, input_xpath, send_text):
        # - sends to the input element with xpath = input_xpath text = send_text and returns True or error text
        success = False
        try:
            # Find the input element using XPath
            input_element = driver.find_element(By.XPATH, input_xpath)

            # Clear the input field
            input_element.clear()

            # Send text to the input element
            input_element.send_keys(send_text)
            input_element.send_keys(Keys.ENTER)
            success = True

            # Return True to indicate successful text entry
            return True

        except NoSuchElementException:
            # If the input element is not found, return the error message
            return f"Input element not found for XPath: {input_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def return_list_elements_by_xpath(driver, elements_xpath):
        # - returns a list of elements with xpath = elements_xpath or returns the error text
        success = False
        try:
            # Find the elements using XPath
            elements = driver.find_elements(By.XPATH, elements_xpath)
            success = True

            # Return the list of elements
            return elements

        except NoSuchElementException:
            # If no elements are found, return the error message
            return f"No elements found for XPath: {elements_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def press_enter_on_element(driver, element_xpath):
        # - click Enter on element with xpath = elements_xpath and returns True or error text
        success = False
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Simulate pressing the Enter key on the element
            element.send_keys(Keys.ENTER)
            success = True

            # Return True to indicate successful key press
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def press_space_on_element(driver, element_xpath):
        # and returns True or error text
        success = False
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Simulate pressing the Enter key on the element
            element.send_keys(Keys.SPACE)
            success = True

            # Return True to indicate successful key press
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def upload_file(driver, input_xpath, file_path):
        # and returns True or error text
        success = False
        try:
            # Find the file input element using XPath
            file_input = driver.find_element(By.XPATH, input_xpath)

            # Clear the file input field (optional)
            file_input.clear()

            # Send the file path to the file input element
            file_input.send_keys(file_path)
            success = True

            # Return True to indicate successful file upload
            return True

        except NoSuchElementException:
            # If the file input element is not found, return the error message
            return f"File input element not found for XPath: {input_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def switch_to_current_window(driver):
        # and returns True or error text

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
        # and returns the attribute value or error text
        success = False
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Get the attribute value of the element
            attribute_value = element.get_attribute(element_attribute)
            success = True

            # Return the attribute value
            return attribute_value

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def get_element_text(driver, element_xpath):
        success = False
        try:
            # Find the element using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Get the text of the element
            element_text = element.text

            # Return the element text
            success = True
            return element_text

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)
        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def select_dropdown_value(driver, dropdown_xpath, dropdown_value):
        success = False
        try:
            # Find the drop-down list element using XPath
            dropdown = Select(driver.find_element(By.XPATH, dropdown_xpath))

            # Select the value from the drop-down list
            dropdown.select_by_value(dropdown_value)
            success = True

            # Return True to indicate successful selection
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {dropdown_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def clear_input_element(driver, element_xpath):
        success = False
        try:
            # Find the input element using XPath
            input_element = driver.find_element(By.XPATH, element_xpath)

            # Clear the input element

            # method 1
            input_element.clear()

            # method 2
            # input_element.click()
            # actions = ActionChains(driver)
            # Press Ctrl + A
            # actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
            # Press BACKSPACE key
            # actions.send_keys(Keys.BACKSPACE)

            # Perform the actions
            # actions.perform()
            # Return True to indicate successful clearing
            success = True
            return True

        except NoSuchElementException:
            # If the element is not found, return the error message
            return f"Element not found for XPath: {element_xpath}"

        except Exception as e:
            # If any other error occurs, return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def press_down_arrow_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_up_arrow_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_UP)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_left_arrow_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_LEFT)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_right_arrow_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.ARROW_RIGHT)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_enter_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.RETURN)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_tab_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.TAB)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_backspace_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.BACKSPACE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_delete_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.DELETE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_char_key(driver, char_key, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(char_key)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def press_space_key(driver, n):
        action = ActionChains(driver)
        for _ in range(n):
            action.send_keys(Keys.SPACE)
            time.sleep(.1)
        action.perform()

    @staticmethod
    def check_url_exists(driver, check_url):
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
        success = False
        try:
            # Open a new tab
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])

            # Open the URL in the new tab
            driver.get(open_url)
            success = True

            # Return True if the URL was opened successfully
            return True

        except WebDriverException as e:
            # Handle any exceptions that occur and return the error message
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def check_element_is_displayed(driver, element_xpath):
        success = False
        try:
            # Find the element on the page using XPath
            element = driver.find_element(By.XPATH, element_xpath)

            # Check if the element is displayed
            if element.is_displayed():
                success = True
                return True
            else:
                success = True
                return False

        except NoSuchElementException as e:
            # Element not found on the page
            return str(e)

        except Exception as e:
            # Other exceptions
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def get_clipboard_text():
        return str(pyperclip.paste())

    @staticmethod
    def convert_string_to_float(string_for_convert):
        success = False
        try:
            float_value = string_for_convert.replace(',', '.')
            if float_value != '':
                float_value = float_value.replace(' ', '', 100)
                float_value = float(float_value)
                success = True
                return float_value
        except ValueError as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def check_text_is_present_on_page(driver, heck_text):
        success = False
        try:
            # Check if the text is present in the page source
            page_source = driver.page_source
            if heck_text in page_source:
                success = True
                return True
            else:
                success = True
                return False

        except Exception as e:
            # Handle any exceptions that occur
            return f"An error occurred: {e}"

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_down_and_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element
                        element.click()
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_up_and_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element
                        element.click()
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_down_and_enter_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element "Enter"
                        element.send_keys(Keys.ENTER)
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_up_and_enter_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element "Enter"
                        element.send_keys(Keys.ENTER)
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_down_and_space_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element "Space"
                        element.send_keys(Keys.SPACE)
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_up_and_space_click(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
            delta = 0
            while delta <= timeout:
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(.1)
                try:
                    element = driver.find_element(By.XPATH, element_xpath)
                    if element.is_displayed():
                        # Click on the element "Space"
                        element.send_keys(Keys.SPACE)
                        break
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and clicked successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_down_and_send(driver, element_xpath, send_text, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
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
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            success = True
            # Return True if the element is displayed and send successfully
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def make_displayed_with_arrow_up_and_send(driver, element_xpath, send_text, waiting_time):
        success = False
        try:
            # Wait for the element to be displayed by pressing the "arrow down" key
            actions = ActionChains(driver)
            timeout = waiting_time  # Maximum waiting time in seconds
            start_time = datetime.datetime.now()
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
                    stop_time = datetime.datetime.now()
                    delta = stop_time - start_time
                except:
                    pass

            # Return True if the element is displayed and send successfully
            success = True
            return True

        except TimeoutException:
            return "Element not displayed within the timeout"

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def find_href_on_page(driver, find_href):
        success = False
        try:
            # Find all anchor elements on the page
            anchor_elements = driver.find_elements_by_tag_name("a")

            # Check if the href is present in any anchor element
            for anchor in anchor_elements:
                try:
                    if anchor.get_attribute("href") == find_href:
                        success = True
                        return True
                except NoSuchElementException:
                    pass

            # Return False if the href is not found
            return False

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def wait_for_element_to_disappear(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to disappear
            wait = WebDriverWait(driver, waiting_time)  # Maximum wait time in seconds
            wait.until(EC.invisibility_of_element_located((By.XPATH, element_xpath)))
            success = True
            # Return True once the element has disappeared
            return True

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def wait_for_element_to_appear(driver, element_xpath, waiting_time):
        success = False
        try:
            # Wait for the element to appear
            wait = WebDriverWait(driver, waiting_time)  # Maximum wait time in seconds
            wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
            success = True
            # Return True once the element has appeared
            return True

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def check_text_in_class(driver, element_xpath, class_text, waiting_time):
        success = False
        try:
            # Wait for the element to be available
            wait = WebDriverWait(driver, waiting_time)  # Maximum wait time in seconds
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))

            # Check if the element's class attribute contains the specified text
            if class_text in element.get_attribute("class"):
                success = True
                return True
            else:
                success = True
                return False

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def double_click_element(driver, element_xpath):
        success = False
        try:
            # Find the element by XPath
            element = driver.find_element_by_xpath(element_xpath)

            # Perform a double click on the element
            actions = ActionChains(driver)
            actions.double_click(element).perform()

            # Return True once the double click is performed
            success = True
            return True

        except Exception as e:
            return str(e)

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def click_ok_in_alert(driver, waiting_time):
        success = False
        try:
            # Wait for the alert to appear
            wait = WebDriverWait(driver, waiting_time)  # Adjust the timeout value as needed
            alert = wait.until(EC.alert_is_present())

            # Switch to the alert and accept it (click "OK")
            # alert = browser.switch_to.alert
            # alert.accept()
            Alert(driver).accept()
            success = True
            return True  # Clicked the "OK" button successfully

        except NoAlertPresentException:
            return "No alert window present"

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

        finally:
            if success == False:
                sys.exit()

    @staticmethod
    def click_ok_button_modal_footer(driver):
        error = True
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
            error = False

            return True  # Return True if the button is clicked successfully

        except NoSuchElementException as e:
            return str(e)  # Return the error's text if the button is not found

        except Exception as e:
            return str(e)  # Return the error's text if any other exception occurs

        finally:
            if error == True:
                sys.exit()

    @staticmethod
    def get_chrome_default_download_folder():
        # Get the path to the downloads folder from the command "xdg-user-dir"
        try:
            output = subprocess.check_output(['xdg-user-dir', 'DOWNLOAD'], universal_newlines=True)
            download_folder = output.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "Error: Could not get the path to the downloads folder in Google Chrome"

        # Check if the downloads folder exists
        if not os.path.isdir(download_folder):
            return "Error: The downloads folder in Google Chrome was not found"

        # folder_name = os.path.basename(download_folder)

        return download_folder  # , folder_name

    @staticmethod
    def get_last_modified_file(folder):
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

# ********************************************************************************************************
