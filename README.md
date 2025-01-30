Module MrFix

General information 

The Mr Fix module is designed to create autotests written in Python for testing UI, API, PostgreSQL, Security and Perfomance Testing.
Mr Fix is a module with a set of decorators methods for writing autotests for frontend and backend. It contains all the basic methods needed to write UI-, API- and SQL-autotests. 
It is an open source product. It is distributed on the terms of free software (i.e. it allows you to legally use it, including on commercial projects). Supports the principle of "all in one and in one place". 
Allows a beginner (and not just a beginner) specialist in quality control automation not to search for a solution through various manuals and websites, but to immediately find it and use proven methods of work in the MrFix module.


All versions of the mrfix module are safe to install in a corporate environment. Here's what it says, for example, about the previous version:
"The latest version of mrfix with no known security vulnerabilities is 8.0.1. We recommend installing version 8.0.1."            

                                                    Safety CLI Cybersecurity Inc
                                                    https://data.safetycli.com/packages/pypi/mrfix/

The advantages of the module are also:

    • reducing the amount of code when using methods of  module;
    
    • a great concentration of the autotester on the correct implementation of the autotest logic, and not on the technical part of autotest;
    
    • the uniformity of the approach of all methods to the form of organization of input data, which simplifies the memorization and application of methods of module
    
Link of source code:

https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

Almost all methods are static (@staticmethod)

If there is a variable "driver" in the method, it is a variable of the Selenium Webdriver type. For example: driver = webdriver.Chrome()

What's new in Version 8.0.5 ?
    - Added the method "check_Console_and_Network_errors" (class MrFixUI) for Google Chrome browser. This method must used with method "get_driver" (class MrBrowserManager)

What's new in Version 8.0.4 ?
    - Corrected the method "convert_curl_to_postman"

What's new in Version 8.0.3 ?
    - Added the method "intercept_failed_requests_after_click". This method clicks a element on a web page and intercepts requests with errors (4xx, 5xx) for a specified duration.
    - Corrected the method "performance_testing_with_postman_collections"

What's new in Version 8.0.2 ?
    - New method added: a new method, "convert_curl_to_postman", has been introduced in the MrPerformance class.
    - Functionality of "convert_curl_to_postman":
        This method converts a curl.txt file containing API requests in the curl format into two separate files:
            1) postman_collections.json
            2) postman_environments.json
    Ensure that the curl.txt file contains valid API requests written in the curl format.

What's new in version 8.0.1 ?
    - Added class MrPerformance.
    - Added two methods to the MrPerformance class: "install_newman" and "performance_testing_with_postman_collections".
    - The "install_newman" method is a universal solution for installing Node.js, npm, and Newman on any OS (Windows, Linux, macOS).
    - The "performance_testing_with_postman_collections" method performs load testing of APIs using Newman for Postman collections. It automatically simulates API requests, measures performance, logs successes and failures, and generates statistics. It supports two execution modes (AABB and ABAB) and saves results in reports for analysis.

What's new in version 7.0.4 ?
    - The list of required packages additionally installed during mrfix installation has been corrected

What's new in version 7.0.3 ?
    - Changed "setup.py" file to install additional packages

What's new in version 7.0.2 ?
    - Added a "scroll_to_element" method that finds an element by the specified XPath and smoothly scrolls to it.

            @staticmethod
            def scroll_to_element(browser, xpath):
                """
                Finds an element by the specified XPath and smoothly scrolls to it.
        
                :param browser: WebDriver - Selenium browser object.
                :param xpath: str - XPath of the element to scroll to.
                """

What's new in version 7.0.1 ?
    - Fixed bugs in a new method "add_logger"

What's new in version 7.0.0 ?
    - Added installation of all necessary additional libraries when installing MrFix itself.
    - Added MrBrowserManager class for setting browser settings in conftest.py file.
    - Added "get_driver" method as a fixture for setting Google Chrome and Firefox browser settings for tests and passing the "driver" variable to UI tests
    - Added MrLoggerHelper class for configuring logging settings in conftest.py file and using it in tests.
    - Added "add_logger" method as a fixture for setting logging settings for tests and passing the "add_logger" method and "log_file_name" variable to tests

What's new in version 6.1.1 ?
    - Due to the change in access to the clipboard in Google Chrome, a new method has been created for inserting text from the clipboard into the input field on the browser page
        insert_from_clipboard(browser, input_xpath)
What's new in version 6.1.0 ?
    - Added 3 methods for work of cookies: 
            get_all_cookies(driver) - this method receives all cookies
            set_cookies(driver, cookies_dict) - this method installs cookies from cookies_dict
            delete_cookies(driver, cookies_key) - this method deletes cookies by cookies_key

What's new in version 6.0.6 ?
    - Minor fixes to optimize the performance of the MrFix module on Windows. Some modules imported into mrfix are only available for Linux and cannot be imported into Windows. Previously, this could lead to problems with the module's operation MrFix in Windows.

What's new in version 6.0.5 ?
    - Fixed bugs in a new method 

What's new in version 6.0.4 ?
    - Code optimization, fixed bugs

What's new in version 6.0.3 ?
    - Added the method get_text_list_in_select(driver, select_xpath) in class MrFixUI
        This method This method returns, as a list of text strings, a list of all dropdown list values with xpath = select_xpath if successful, or error text otherwise.

What's new in version 6.0.2 ?
    - The descriptions of the following methods have been changed:
        post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None)
        get_request(requests_url: str, requests_headers: dict, auth: list = None)
        put_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None)
        delete_request(requests_url: str, requests_headers: dict, auth: list = None)


What's new in version 6.0.1 ?
    - Added in class MrFixUI a method "delete_disable_attribute"
    - Added the ability to add authorization to methods for API requests (optional parameter: auth : list = None 
        as a list of two values: login and password, for example auth = (login, password)). The authorization parameter
        has been added for the following methods:

        post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None)
        get_request(requests_url: str, requests_headers: dict, auth: list = None)
        put_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None)
        delete_request(requests_url: str, requests_headers: dict, auth: list = None)

What's new in version 6.0.0 ?
    - Added class MrFixLoad. Added methods in this class.
    - Added methods "put_request" and "delete_request" in class MrFixAPI
    - Added descriptions of this methods


What's new in version 5.0.0 ?
    - Added class MrFixTime. Added methods in this class.
    - Added a method "change_element_text" in class MrFixUI
    - Added descriptions of several methods of class MrFixUI

What's new in version 4.0.2 ?
    - Change the description of the methods of class MrFixSecurity

What's new in version 4.0.1 ?
    - Added class MrFixSecurity. Added methods in this class.

What's new in version 3.0.2 ?
    - Corrected several mistakes in class MrFixSQL

What's new in version 3.0.1 ?
    - Added classes MrFixSQL and MrFixAPI. Added methods in these classes.



A brief description of the methods of all classes

class MrBrowserManager:

    def get_driver(self, width, high, headless):
        # - returns fixture "driver" for UI tests
        # - width - this is the width of the browser window in pixels when you run your tests (for example: "1920")
        # - high - this is the high of the browser window in pixels when you run your tests (for example: "1080")
        # - headless - this is set headless mode for browser in UI tests (for example: False)
        #
        # For example: how to use this method in conftest.py:
        # 
        #    from mrfix.mrfix import MrBrowserManager
        #
        #    @pytest.fixture
        #    def browser():
        #        manager = BrowserManager(config_browser='chrome', wait_time = 20)  # или 'firefox'
        #        driver = manager.get_driver(width="1920", high="1080", headless=False)
        #    
        #        # Transferring the driver to the tests
        #        yield driver
        #    
        #        # End of the session
        #        manager.quit_driver()
        #
        # For example: how to use this method in test:
        #
        # def test(browser):
        #
        #   start_url = 'google.com'
        #   browser.get(start_url)


class MrLoggerHelper:

    def add_logger(request):
        # - returns the "add_logger" method for logging tests
        #
        # For example: how to use this method in conftest.py:
        # 
        #    from mrfix.mrfix import MrLoggerHelper
        #
        #    # To have pytest automatically use the `add_logger` fixture
        #    add_logger = LoggerHelper.add_logger
        #
        # For example: how to use in test:
        #
        # def test(browser, add_logger):
        #    my_message = "Hi, I'm starting this test"
        #    add_logger.info(f'My message: {my_message}')


class MrFixLoad

    def run_load_method_of_get_requests_in_range(min_count: int, max_count: int, step: int, url: str)
        # - This load testing method executes get requests to a specific URL in a loop. 
        # - All queries at each 
        # - All queries in each step of the loop are executed in parallel. 
        # - The number of parallel queries executed for each step of the cycle varies from "min" to "max" with an interval of "step".

        # # Usage example:
        # requests_url = '<your url for request>'
        # min_count = 10
        # max_count = 11
        # step = 5
        # def test_load_get_methods():
        #     # Calling a method from another module
        #     asyncio.run(MrFixLoad.run_load_method_of_get_requests_in_range(min_count, max_count, step, requests_url))
        # test_load_get_methods()

    def run_load_method_of_post_requests_in_range(min_count: int, max_count: int, step: int, url: str, headers: dict, body: dict)
        # - This load testing method executes post requests to a specific URL in a loop.  
        # - The queries are all the same, with the same "headers" and "body". 
        # - All queries at each step of the loop are executed in parallel. 
        # - The number of parallel queries executed for each step of the loop varies from "min" to "max" with an interval of "step".

        # # Usage example:
        # requests_url2 = '<your url for request>'
        # headers = {}
        # body = {
             "parametr1": "value1",  # for str type
             "parametr2": value2     # for int and another type
        #    }

        # def test_load_post_methods():
        #     # Calling a method from another module
        #     asyncio.run(MrFixLoad.run_load_method_of_post_requests_in_range(min_count, max_count, step, requests_url2,
                                                                            headers, body))
        # test_load_post_methods()


class MrFixTime

    def get_start_time():
        # - returns the exact current time
    
    def get_delta_time(start_time):
        # - returns the difference between the exact current time and the exact time value obtained earlier (start_time)

class MrFixSecurity

    def is_port_open(host, port):
        # - The method checks whether the port number = port (integer value) is open or not
        # - Return "True" or "False"

    def check_open_ports(host, ports_list, timeout=1):
        # - The method checks whether each of the ports in the ports_list list is open
        # (contains integer values of port numbers) or not
        # - Return a dictonary of type: {<port number> : <status - "open" or "closed">, ...}

    def generate_key(filename):
        # - Generate a random encryption key and save the encryption key to a file
        # - Return "True" or error's text

    def encrypt_file(input_file, output_file, key_file):
        # - Encrypt a file using a given key_file and save the encrypted data to another file
        # - Return "True" or error's text

    def decrypt_file(input_file, output_file, key_file):
        # - Decrypt a file using a given key and save the decrypted data to another file
        # - Return "True" or error's text


class MrFixSQL

    def run_openvpn_for_linux(config_path: str, pas: str):
    # - Launches OpenVPN with a command with administrator privileges on the Linux command line using the ".ovpn" settings file
    # - Returns a success message or error text

    def run_openvpn_for_Windows(config_path: str, pas: str):
    # - Launches OpenVPN with a command with administrator privileges on the Windows command line using the ".ovpn" settings file
    # - Returns a success message or error text

    def run_openvpn_for_Windows_11(config_path: str, pas: str):
    # - Launches OpenVPN with a command with administrator privileges on the Windows 11 command line using the ".ovpn" settings file
    # - Returns a success message or error text
    

    def stop_openvpn_for_linux(pas: str):
    # - Stops OpenVPN with a command with administrator privileges on the Linux command line
    # - Returns a success message or error text
    

    def stop_openvpn_for_Windows(pas: str):
    # - Stops OpenVPN with a command with administrator privileges on the Windows command line
    # - Returns a success message or error text
    

    def export_SQL_request_result_table_to_text_file(connection_data: dict, sql_query: str, txt_file_path: str):
    # - From a table in the database, PostgreSQL gets all the data for the SQL query and saves it to a text file
    # - (name the file and the full path to it are in txt_file_path). The table is defined by the sql_query SQL query.
    # - The database access parameters are specified in the connection_data dictionary in the values
    # - of the keys "host", "port", "database", "user", "password".
    # - Returns a success message or error text
    

    def export_SQL_request_result_table_to_csv_file(connection_data: dict, sql_query: str, csv_file_path: str):
    # Exports a table from PostgreSQL to a csv file
    # (name the file and the full path to it are in csv_file_path). The table is defined by the sql_query SQL query.
    #  The database access parameters are specified in the connection_data dictionary in the values
    #  of the keys "host", "port", "database", "user", "password".
    # Returns a success message or error text
    

    def insert_data_in_postgesql(connection_data: dict, sql_query: str, data: str):
    # - Performs the insertion of several rows of data "data" in PostgreSQL using sql_query SQL query.
    # - The database access parameters are specified in the connection_data dictionary in the values
    # - of the keys "host", "port", "database", "user", "password".
    # - Returns a success message or error text
    

    def modify_record_in_postgesql(connection_data:dict, sql_query:str):
    # - Changes record in PostgreSQL using sql_query SQL query.
    # - The database access parameters are specified in the connection_data dictionary in the values
    # - of the keys "host", "port", "database", "user", "password".
    # - Returns a success message or error text
    

    def find_record_in_postgresql(connection_data: dict, sql_query: str):
    # - Searches for data in PostgreSQL using sql_query SQL query.
    # - The database access parameters are specified in the connection_data dictionary in the values
    # - of the keys "host", "port", "database", "user", "password".
    # - Returns a success message or error text
    

class MrFixAPI

    def post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None, auth: list = None)):
    # - Makes POST request with used requests_url (requests url), requests_body (requests body),
    # - requests_headers (requests_headers) pre_script (pre-request script, optional), auth (authorization, optional)
    # - Returns response in JSON file

    def get_request(requests_url: str, requests_headers: dict):
    # - Makes GET request with used requests_url (requests url), requests_headers (requests_headers),
    # - auth (authorization, optional)
    # - Returns response in JSON file

    def put_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None):
    # - Makes PUT request with used requests_url (requests url), requests_body (requests body),
    # - requests_headers (requests_headers), pre_script (pre-request script, optional), auth (authorization, optional)
    # - Returns response in JSON file

    def delete_request(requests_url: str, requests_headers: dict):
    # - Makes DELETE request with used requests_url (requests url), requests_headers (requests_headers),
    # - auth (authorization, optional)
    # - Returns response in JSON file


class MrFixUI:

    insert_from_clipboard(driver, input_xpath):
    # This method for inserting text from the clipboard into the input field
    # on a web page in the field with xpath = input_xpath

    delete_disable_attribute(driver, element_xpath):
    # - this method delete attribute "disable" of element with xpath = element_xpath, if this attribute exists, and return True or error's text

    get_all_cookies(driver)
    # - this method receives all cookies
    
    set_cookies(driver, cookies_dict)
    # - this method installs cookies from cookies_dict
    
    delete_cookies(driver, cookies_key)
    # - this method deletes cookies by cookies_key

    check_exists_xpath(driver, check_xpath):
    # - checks the existence of an element with xpath = check_xpath and returns True or False

    click_element_by_xpath(driver, element_xpath, timeout=10):
    # - performs a click on an element with xpath=element_xpath and returns True of success or False

    select_from_dropdown_text(driver, dropdown_xpath, dropdown_text):
    # - selects a line with text = dropdown_text from the drop-down list with xpath = dropdown_xpath and returns True of success or text of error

    send_text_to_input(driver, input_xpath, send_text):
    # - sends to the input element with xpath = input_xpath text = send_text and returns True of success or text of error

    return_list_elements_by_xpath(driver, elements_xpath):
    # - returns a list of elements with xpath = elements_xpath or returns text of error

    press_enter_on_element(driver, element_xpath):
    # - click Enter on element with xpath = elements_xpath and returns True of success or text of error

    press_space_on_element(driver, element_xpath):
    # - click Space on element with xpath = elements_xpathand and returns True of success or text of error

    upload_file(driver, input_xpath, file_path):
    # - upload file with path + file name = "file_path" in element of type "input" with xpath = "input_xpath" and returns True of success or text of error

    switch_to_current_window(driver):
    # - swith to current window in browser and returns True or error text

    get_element_attribute(driver, element_xpath, element_attribute):
    # - get attribute = element_attribute of element with xpath = element_xpath and returns the attribute value or text of error

    get_element_text(driver, element_xpath):
    # - get text of element with xpath = element_xpath and returns the text of success or text of error

    select_dropdown_value(driver, dropdown_xpath, dropdown_value):
    # - select the item with xpath = dropdown_xpath from the drop-down list. value = dropdown_value and return True of success or text of error

    clear_input_element(driver, element_xpath):
    # - clear element with xpath = element_xpath and return True of success or text of error

    press_escape_key(driver, n):
    # - presses the ESCAPE key n-times

    press_down_arrow_key(driver, n):
    # - presses the ARROW DOWN key n-times

    press_up_arrow_key(driver, n):
    # - presses the ARROW UP key n-times

    press_left_arrow_key(driver, n):
    # - presses the ARROW LEFT key n-times

    press_right_arrow_key(driver, n):
    # - presses the ARROW RIGHT key n-times

    press_enter_key(driver, n):
    # - presses the ENTER key n-times

    press_tab_key(driver, n):
    # - presses the TAB key n-times

    press_backspace_key(driver, n):
    # - presses the BACKSPACE key n-times

    press_delete_key(driver, n):
    # - presses the DELETE key n-times

    press_char_key(driver, char_key, n):
    # - presses the key = char_key n-times

    press_space_key(driver, n):
    # - presses the SPACE key n-times

    check_url_exists(driver, check_url):
    # - checks if url = check_url exists and return True of success or False

    open_url_in_new_tab(driver, open_url):
    # - opens url = open_url in a new browser tab and return True of success or text of error

    check_element_is_displayed(driver, element_xpath):
    # - checks the display of an element with xpath = element_xpath on the page and return True of success or False

    get_clipboard_text():
    # - gets the text from the clipboard

    convert_string_to_float(string_for_convert):
    # - converts a string value to a floating point value and return float value or text of error

    check_text_is_present_on_page(driver, check_text):
    # - checks to present text = check_text on page and return True of success or False or text of error

    make_displayed_with_arrow_down(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing the key ARROW DOWN and return True of success or False

    make_displayed_with_arrow_up(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing the key ARROW UP and return True of success or False

    make_displayed_with_arrow_down_and_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks on the element and return True of success or False

    make_displayed_with_arrow_up_and_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks on the element and return True of success or False

    make_displayed_with_arrow_down_and_enter_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks ENTER key on the element and return True of success or False
  
    make_displayed_with_arrow_up_and_enter_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks ENTER key on the element and return True of success or False
 
    make_displayed_with_arrow_down_and_space_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and then clicks SPACE key on the element and return True of success or False
  
    make_displayed_with_arrow_up_and_space_click(driver, element_xpath, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and then clicks SPACE key on the element and return True of success or False
  
    make_displayed_with_arrow_down_and_send(driver, element_xpath, send_text, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW DOWN and send text = send_text in elemet of type "input" with element's xpath = element_xpath and return True or text of error
  
    make_displayed_with_arrow_up_and_send(driver, element_xpath, send_text, waiting_time):
    # - during the time = waiting_time tries to move the element with xpath = element_xpath to the visibility zone by pressing a key ARROW UP and send text = send_text in elemet of type "input" with element's xpath = element_xpath and return True or text of error
  
    find_href_on_page(driver, find_href):
    # - finds href = find_href on page and return True or text of error

    wait_for_element_to_disappear(driver, element_xpath, waiting_time):
    # - during the waiting time, time = waiting_time waits for the element with xpath = element_xpath to disappear and return True or text of error

    wait_for_element_to_appear(driver, element_xpath, waiting_time):
    # - during the waiting time, time = waiting_time waits for the element with xpath = element_xpath to appear and return True or text of error

    check_text_in_class(driver, element_xpath, class_text):
    # - checks to exist text = class_text in class of element with xpath = element_xpath and return True of success or False

    double_click_element(driver, element_xpath):
    # - makes double click on element with xpath = element_xpath and return True or text of error

    click_ok_in_alert(driver, waiting_time):
    # - during the waiting time, time = waiting_time waits and clicks on the "Ok" of alert window and return True or text of error

    click_ok_button_modal_footer(driver):
    # - clicks on the "Ok" of modal footer and return True or text of error

    get_chrome_default_download_folder():
    # - gets path to the downloads folder in Google Chrome and return path or text of error

    get_last_modified_file(folder):
    # - gets last modifierd file in folder and return file name or text of error

    def get_path_separator():
    # - returns the character used by the operating system to separate path elements. For Windows – ‘\\’

    def check_page_errors(driver):
    # - checks for errors on the browser page on the Console and Network tab in the Developer Panel (F12 key)

    def is_element_clickable(driver, xpath):
    # - checks the clickability of this element

    def is_element_present(driver, xpath):
    # - checks for element presence

    def set_implicit_waiting_time(driver, time_in_second):
    # - sets an implicit timeout

    def get_input_value(driver, input_xpath):
    # - gets the element's input value with element's xpath = input_xpath

    def get_separator():
    # get system's separator in files path (It is for example for Windows "\", for Linux "/")

    def change_element_text(driver, span_xpath, new_text):
    # - modify the innerHTML of an element identified by XPath.

    def get_text_list_in_select(driver, select_xpath):
    # - get the list of text of element with type "select'


