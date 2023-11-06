Module MrFix

What's new in version 4.0.2 ?
    - Change the description of the methods of class MrFixSecurity

What's new in version 4.0.1 ?
    - Added class MrFixSecurity. Added methods in this class.

What's new in version 3.0.2 ?
    - Corrected several mistakes in class MrFixSQL

What's new in version 3.0.1 ?
    - Added classes MrFixSQL and MrFixAPI. Added methods in these classes.

General information 

The Mr Fix module is designed to create autotests written in Python for testing UI, API and PostgreSQL.
Mr Fix is a module with a set of decorators methods for writing autotests for frontend and backend. It contains all the basic methods needed to write UI-, API- and SQL-autotests. 
It is an open source product. It is distributed on the terms of free software (i.e. it allows you to legally use it, including on commercial projects). Supports the principle of "all in one and in one place". 
Allows a beginner (and not just a beginner) specialist in quality control automation not to search for a solution through various manuals and websites, but to immediately find it and use proven methods of work in the MrFix module.

The advantages of the module are also:

    • reducing the amount of code when using methods of  module;
    
    • a great concentration of the autotester on the correct implementation of the autotest logic, and not on the technical part of autotest;
    
    • the uniformity of the approach of all methods to the form of organization of input data, which simplifies the memorization and application of methods of module
    
Link of source code:

https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

ATTENTION! You can check the security of using the MrFix module on this website:  https://app.snyk.io/advisor/python/mrfix

All methods are static (@staticmethod)

If there is a variable "driver" in the method, it is a variable of the Selenium Webdriver type. For example: driver = webdriver.Chrome()

A brief description of the methods of all classes

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

    def post_request(requests_url: str, requests_body: dict, requests_headers: dict, pre_script: str = None):
    # - Makes POST request with used requests_url (requests url), requests_body (requests body),
    # - requests_headers (requests_headers) and pre_script (pre-request script, optional)
    # - Returns response in JSON file

    def get_request(requests_url: str, requests_headers: dict):
    # - Makes GET request with used requests_url (requests url), requests_headers (requests_headers)
    # - Returns response in JSON file


class MrFixUI:

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


