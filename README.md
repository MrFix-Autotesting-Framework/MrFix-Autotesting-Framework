Module MrFix

General information 

The MrFix module is designed to create UI autotests written in Python using the Selenium library. Description of the methods of the MrFix module
MrFix is a module with a set of decorators methods for writing UI-autotests in Python + Selenium. It contains all the basic methods needed to write UI-autotests. It is an open source product. It is distributed on the terms of free software (i.e. it allows you to legally use it, including on commercial projects). Supports the principle of "all in one and in one place". Allows a beginner (and not a beginner either) autotester not to search for a solution through various manuals and websites, but to immediately find it and use proven working methods in the MrFix module.

Also the advantage of the module is:

    • reducing the amount of code when using methods of  module;
    
    • a great concentration of the autotester on the correct implementation of the autotest logic, and not on the technical part of autotest;
    
    • the uniformity of the approach of all methods to the form of organization of input data, which simplifies the memorization and application of methods of module
    
Link of source code:

https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

Description of methods

Method Description: check_exists_xpath(driver, check_xpath)

This method is a static method used to check for the presence of an element with a specified XPath expression on a web page. It takes two parameters: driver and check_xpath. The driver parameter represents the WebDriver instance being used for automation, while the check_xpath parameter is the XPath expression used to locate the desired element on the page.
The method temporarily sets a shorter implicit wait timeout to 1 second using driver.implicitly_wait(1) in order to expedite the element search. It then attempts to find the element using the provided XPath expression.
If the element is found, indicating its presence on the page, the method returns True to indicate its existence.
However, if the element is not found, the method catches a NoSuchElementException and returns False to indicate that the element is not present on the page at the moment. This can occur if the XPath is incorrect or if the element is not currently visible or available.
After either finding the element or encountering the NoSuchElementException, the method restores the original implicit wait timeout using driver.implicitly_wait(original_timeout) to revert to the previous wait setting. This ensures that subsequent operations or searches are not affected by the shorter timeout used within this method.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver) and provide the correct XPath expression (check_xpath) to locate the desired element on the page.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.

Method Description: click_element_by_xpath(driver, element_xpath)

This method is a static method used to perform a click action on an element identified by a specified XPath expression on a web page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while the element_xpath parameter is the XPath expression used to locate the desired element on the page.
The method attempts to find the element using the provided XPath expression using driver.find_element(By.XPATH, element_xpath). If the element is found, it performs a click action on the element using element.click().
If the click action is performed successfully, the method returns True to indicate the successful click.
However, if the element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found. This can occur if the XPath is incorrect or if the element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as an error message string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver) and provide the correct XPath expression (element_xpath) to locate the desired element on the page.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.

Method Description: select_from_dropdown_text(driver, dropdown_xpath, dropdown_text)

This method is a static method used to select an option from a dropdown list based on its text. It takes three parameters: driver, dropdown_xpath, and dropdown_text. The driver parameter represents the WebDriver instance being used for automation, dropdown_xpath is the XPath expression used to locate the dropdown element on the page, and dropdown_text is the text of the option to be selected.
The method first attempts to find the dropdown element using the provided XPath expression with driver.find_element(By.XPATH, dropdown_xpath). Once the dropdown element is found, it is wrapped in a Select object to enable selection of options.
Next, the method selects the desired option from the dropdown based on its text using dropdown.select_by_visible_text(dropdown_text).
If the option is selected successfully, the method returns True to indicate the successful selection.
However, if the dropdown element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found. This can occur if the XPath is incorrect or if the dropdown element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as an error message string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (dropdown_xpath) to locate the dropdown element, and specify the desired option's text (dropdown_text) to be selected.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.

Method Description: send_text_to_input(driver, input_xpath, send_text)

This method is a static method used to send text to an input element identified by a specified XPath expression on a web page. It takes three parameters: driver, input_xpath, and send_text. The driver parameter represents the WebDriver instance being used for automation, input_xpath is the XPath expression used to locate the input element on the page, and send_text is the text to be entered into the input field.
The method first attempts to find the input element using the provided XPath expression with driver.find_element(By.XPATH, input_xpath).
Once the input element is found, the method performs the following steps:
    1. Clears the input field using input_element.clear() to ensure any previous text is removed.
    2. Sends the desired text to the input element using input_element.send_keys(send_text).
    3. Simulates pressing the Enter key using input_element.send_keys(Keys.ENTER). This step can be commented out if not needed.
If the text is sent to the input element successfully, the method returns True to indicate the successful text entry.
However, if the input element is not found, the method catches a NoSuchElementException and returns an error message indicating that the input element was not found. This can occur if the XPath is incorrect or if the input element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (input_xpath) to locate the input element, and specify the text (send_text) to be entered.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.

Method Description: return_list_elements_by_xpath(driver, elements_xpath)

This method is a static method used to return a list of elements identified by a specified XPath expression on a web page. It takes two parameters: driver and elements_xpath. The driver parameter represents the WebDriver instance being used for automation, while the elements_xpath parameter is the XPath expression used to locate the desired elements on the page.
The method attempts to find the elements using the provided XPath expression using driver.find_elements(By.XPATH, elements_xpath).
If elements are found, the method returns a list of those elements.
However, if no elements are found, the method catches a NoSuchElementException and returns an error message indicating that no elements were found for the given XPath expression. This can occur if the XPath is incorrect or if no elements matching the expression are present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver) and provide the correct XPath expression (elements_xpath) to locate the desired elements on the page.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.

Method Description: press_enter_on_element(driver, element_xpath)

This method is a static method used to simulate pressing the Enter key on a specified element within a web page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while the element_xpath parameter is the XPath expression used to locate the desired element on the page.
The method attempts to find the element using the provided XPath expression and then simulates pressing the Enter key on that element. If successful, the method returns True to indicate that the key press was performed successfully.
However, if the element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver) and provide the correct XPath expression (element_xpath) to locate the desired element on the page.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.


Method Description: press_space_on_element(driver, element_xpath)

This method is a static method used to simulate pressing the Space key on a specified element within a web page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while the element_xpath parameter is the XPath expression used to locate the desired element on the page.
The method attempts to find the element using the provided XPath expression and then simulates pressing the Space key on that element. It achieves this by using element.send_keys(Keys.SPACE).
If the Space key press is performed successfully, the method returns True to indicate the successful key press.
However, if the element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver) and provide the correct XPath expression (element_xpath) to locate the desired element on the page.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.


Method Description: upload_file(driver, input_xpath, file_path)

This method is a static method used to upload a file to a file input element on a web page. It takes three parameters: driver, input_xpath, and file_path. The driver parameter represents the WebDriver instance being used for automation, input_xpath is the XPath expression used to locate the file input element on the page, and file_path is the path to the file that will be uploaded.
The method first attempts to find the file input element using the provided XPath expression with driver.find_element(By.XPATH, input_xpath).
Once the file input element is found, the method performs the following steps:
    1. (Optional) Clears the file input field using file_input.clear(). This step is optional and can be removed if desired.
    2. Sends the file path to the file input element using file_input.send_keys(file_path).
If the file is uploaded successfully, the method returns True to indicate the successful file upload.
However, if the file input element is not found, the method catches a NoSuchElementException and returns an error message indicating that the file input element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the file input element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (input_xpath) to locate the file input element, and specify the file path (file_path) to be uploaded.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.



Method Description: switch_to_current_window(driver)

This method is a static method used to switch to the current window and close all other windows in a web browser. It takes one parameter: driver, which represents the WebDriver instance being used for automation.
The method first gets the window handle of the current window using driver.current_window_handle.
Then, it iterates over all the window handles using driver.window_handles and closes any window that is not the current window. This is achieved by switching to each window handle using driver.switch_to.window(window_handle) and then closing it using driver.close().
After closing all other windows, the method switches back to the current window using driver.switch_to.window(current_window).
If the window switching process is performed successfully, the method returns True to indicate the successful window switch.
However, if the window handle is not found, the method catches a NoSuchWindowException and returns an error message indicating that the window handle was not found.
In addition to handling the NoSuchWindowException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.


Method Description: get_element_attribute(driver, element_xpath, element_attribute)

This method is a static method used to retrieve the value of a specific attribute of an element on a web page. It takes three parameters: driver, element_xpath, and element_attribute. The driver parameter represents the WebDriver instance being used for automation, element_xpath is the XPath expression used to locate the desired element on the page, and element_attribute is the name of the attribute whose value will be retrieved.
The method first attempts to find the element using the provided XPath expression with driver.find_element(By.XPATH, element_xpath).
Once the element is found, the method retrieves the value of the specified attribute using element.get_attribute(element_attribute).
If the attribute value is successfully retrieved, the method returns the attribute value.
However, if the element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (element_xpath) to locate the desired element, and specify the name of the attribute (element_attribute) whose value you want to retrieve.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.



Method Description: get_element_text(driver, element_xpath)

This method is a static method used to retrieve the text content of an element on a web page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while the element_xpath parameter is the XPath expression used to locate the desired element on the page.
The method attempts to find the element using the provided XPath expression with driver.find_element(By.XPATH, element_xpath).
Once the element is found, the method retrieves the text content of the element using element.text.
If the element text is successfully retrieved, the method returns the element text.
However, if the element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (element_xpath) to locate the desired element, and ensure that the element contains visible text content.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.



Method Description: select_dropdown_value(driver, dropdown_xpath, dropdown_value)

This method is a static method used to select a specific value from a dropdown list on a web page. It takes three parameters: driver, dropdown_xpath, and dropdown_value. The driver parameter represents the WebDriver instance being used for automation, dropdown_xpath is the XPath expression used to locate the dropdown list element, and dropdown_value is the value that needs to be selected from the dropdown list.
The method attempts to find the dropdown list element using the provided XPath expression with driver.find_element(By.XPATH, dropdown_xpath).
Once the dropdown list element is found, the method creates a Select object around the element using Select(driver.find_element(By.XPATH, dropdown_xpath)). This allows for easier interaction with the dropdown list.
The method then selects the specified value from the dropdown list using dropdown.select_by_value(dropdown_value). This selects the option with the matching value attribute.
If the value is successfully selected from the dropdown list, the method returns True to indicate the successful selection.
However, if the dropdown list element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the dropdown list element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (dropdown_xpath) to locate the dropdown list element, and specify the value (dropdown_value) that you want to select from the dropdown list.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.


Method Description: clear_input_element(driver, element_xpath)

This method is a static method used to clear the content of an input element on a web page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while the element_xpath parameter is the XPath expression used to locate the desired input element on the page.
The method attempts to find the input element using the provided XPath expression with driver.find_element(By.XPATH, element_xpath).
Once the input element is found, the method clears its content by calling input_element.clear().
If the content of the input element is successfully cleared, the method returns True to indicate the successful clearing.
However, if the input element is not found, the method catches a NoSuchElementException and returns an error message indicating that the element was not found for the given XPath expression. This can occur if the XPath is incorrect or if the input element is not present on the page.
In addition to handling the NoSuchElementException, the method also catches any other exceptions that may occur during the process. If an unexpected error occurs, the method captures the error message and returns it as a string.
It is important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver), provide the correct XPath expression (element_xpath) to locate the desired input element, and ensure that the element is indeed an input element.
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.



Method Description: press_down_arrow_key(driver, n)

This method is a static method used to simulate pressing the down arrow key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the down arrow key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the down arrow key by calling action.send_keys(Keys.ARROW_DOWN). This simulates a single press of the down arrow key.
After pressing the down arrow key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.



Method Description: press_up_arrow_key(driver, n)

This method is a static method used to simulate pressing the up arrow key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the up arrow key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the up arrow key by calling action.send_keys(Keys.ARROW_UP). This simulates a single press of the up arrow key.
After pressing the up arrow key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.



Method Description: press_left_arrow_key(driver, n)

This method is a static method used to simulate pressing the left arrow key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the left arrow key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the left arrow key by calling action.send_keys(Keys.ARROW_LEFT). This simulates a single press of the left arrow key.
After pressing the left arrow key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.


Method Description: press_right_arrow_key(driver, n)

This method is a static method used to simulate pressing the right arrow key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the right arrow key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the right arrow key by calling action.send_keys(Keys.ARROW_RIGHT). This simulates a single press of the right arrow key.
After pressing the right arrow key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.


Method Description: press_enter_key(driver, n)

This method is a static method used to simulate pressing the Enter key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the Enter key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the Enter key by calling action.send_keys(Keys.RETURN). This simulates a single press of the Enter key.
After pressing the Enter key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.


Method Description: press_tab_key(driver, n)

This method is a static method used to simulate pressing the Tab key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the Tab key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the Tab key by calling action.send_keys(Keys.TAB). This simulates a single press of the Tab key.
After pressing the Tab key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.



Method Description: press_backspace_key(driver, n)

This method is a static method used to simulate pressing the Backspace key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the Backspace key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the Backspace key by calling action.send_keys(Keys.BACKSPACE). This simulates a single press of the Backspace key.
After pressing the Backspace key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.



Method Description: press_delete_key(driver, n)

This static method is used to simulate pressing the Delete key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the Delete key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the Delete key by calling action.send_keys(Keys.DELETE). This simulates a single press of the Delete key.
After pressing the Delete key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using these method. Additionally, the method require the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.

Method Description: press_char_key(driver, char_key, n)

This static method is used to simulate pressing a specific character key a specified number of times. It takes three parameters: driver, char_key, and n. The driver parameter represents the WebDriver instance being used for automation, char_key represents the character key to be pressed, and n represents the number of times to press the key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the character key by calling action.send_keys(char_key). This simulates a single press of the specified character key.
After pressing the character key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using these method. Additionally, the method require the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.


Method Description: press_space_key(driver, n)

This static method is used to simulate pressing the Space key a specified number of times. It takes two parameters: driver and n. The driver parameter represents the WebDriver instance being used for automation, while n represents the number of times to press the Space key.
The method utilizes the ActionChains class from the Selenium WebDriver library to perform the key press actions. It creates an ActionChains object named action with ActionChains(driver).
Inside a loop that runs n times, the method simulates pressing the Space key by calling action.send_keys(Keys.SPACE). This simulates a single press of the Space key.
After pressing the Space key, the method introduces a small delay of 0.1 seconds using time.sleep(.1). This delay allows for the key press action to take effect before the next iteration of the loop.
Once the loop is complete, the method performs all the accumulated actions by calling action.perform().
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the ActionChains class and the Keys class to be imported from the Selenium WebDriver library.


Method Description: check_url_exists(driver, check_url)

This static method is used to check if a URL exists and is accessible by attempting to open it using the provided WebDriver instance. It takes two parameters: driver and check_url. The driver parameter represents the WebDriver instance being used for automation, while check_url represents the URL to be checked.
The method begins by setting a timeout for the page load using driver.set_page_load_timeout(original_timeout). This ensures that the driver waits for the page to load completely before proceeding.
Next, the method attempts to open the specified URL by calling driver.get(check_url). If the URL exists and the page loads successfully, no exception is raised.
If no exception is raised, the method returns True, indicating that the URL exists and is accessible.
However, if a WebDriverException is caught, it implies that the URL either does not exist or failed to load within the specified timeout period. In such cases, the method returns False to indicate that the URL does not exist or is inaccessible.
It's important to note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Please make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method. Additionally, the method requires the WebDriverException class to be imported from the Selenium WebDriver library.



Method Description: open_url_in_new_tab(driver, open_url)

This static method is used to open a URL in a new tab using the provided WebDriver instance. It takes two parameters: driver and open_url. The driver parameter represents the WebDriver instance being used for automation, while open_url represents the URL to be opened.
The method follows the following steps to open the URL in a new tab:
    1. It first sends the keyboard combination Ctrl + t to the <body> element of the current page to open a new tab. This is achieved using the send_keys(Keys.CONTROL + 't') method call on driver.find_element_by_tag_name('body').
    2. After opening the new tab, the method switches the WebDriver's focus to the newly opened tab using driver.switch_to.window(driver.window_handles[-1]). This ensures that subsequent actions are performed on the new tab.
    3. The method then opens the specified URL in the new tab by calling driver.get(open_url). The WebDriver will navigate to the provided URL in the new tab.
    4. If the URL is opened successfully without any WebDriver exceptions being raised, the method returns True to indicate that the URL was opened in the new tab successfully.
    5. However, if a WebDriverException is caught during the execution, it implies that there was an error in opening the URL in the new tab. In such cases, the method returns the error message as a string representation of the exception (str(e)) to provide information about the specific error that occurred.
Please note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Additionally, make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.


Method Description: check_element_is_displayed(driver, element_xpath)
    
This static method is used to check if an element specified by its XPath is displayed on the page. It takes two parameters: driver and element_xpath. The driver parameter represents the WebDriver instance being used for automation, while element_xpath represents the XPath of the element to be checked.
The method follows the following steps to check if the element is displayed:
    1. It attempts to locate the element on the page using the find_element() method of the WebDriver instance. The element is identified by its XPath, which is passed as the element_xpath parameter.
    2. If the element is found, the method proceeds to check if it is displayed by calling the is_displayed() method on the element object. The is_displayed() method returns True if the element is visible on the page, and False otherwise.
    3. If the element is displayed (i.e., is_displayed() returns True), the method returns True to indicate that the element is indeed displayed on the page.
    4. If the element is not found on the page, a NoSuchElementException is raised. In this case, the method returns the error message as a string representation of the exception (str(e)), providing information about the specific error that occurred.
    5. If any other exception occurs during the execution of the method, it is caught by the except Exception as e block. The method returns the error message as a string representation of the exception (str(e)), providing information about the specific error that occurred.
Please note that this method assumes the usage of the Selenium WebDriver library for browser automation. Prior to calling this method, you should have a valid WebDriver instance (driver).
Additionally, make sure to import the necessary dependencies and set up the WebDriver appropriately before using this method.



Method Description: get_clipboard_text()
    
This static method is used to retrieve the text content from the clipboard. It does not require any parameters.
The method utilizes the pyperclip library, which provides cross-platform support for accessing the clipboard. The pyperclip.paste() function is used to retrieve the text content currently stored in the clipboard.
The method follows the following steps to retrieve the clipboard text:
    1. It calls the pyperclip.paste() function, which retrieves the text content from the clipboard.
    2. The retrieved text is then converted to a string using the str() function.
    3. The method returns the clipboard text as a string.
Please note that this method relies on the pyperclip library, so make sure to have it installed before using this method. Additionally, the availability and behavior of clipboard operations may vary across different operating systems and environments.
Ensure that you have the necessary permissions to access the clipboard and that the clipboard contains text content before calling this method.


Method Description: convert_string_to_float(string_for_convert)
    
This static method is used to convert a string to a floating-point number. It takes a single parameter string_for_convert, which is the string that needs to be converted.
The method follows the following steps to convert the string to a float:
    1. It attempts to convert the input string to a float by using the float() function. However, before performing the conversion, it replaces any commas (,) in the string with periods (.) to ensure compatibility with decimal notation.
    2. If the conversion is successful and the resulting float value is not an empty string, the method continues to the next step. Otherwise, it returns an error message indicating a ValueError.
    3. The method further processes the float value by removing any spaces within the string. It replaces all occurrences of spaces with an empty string using the replace() method, with a limit of 100 replacements. This is done to handle cases where the string contains extraneous spaces that might interfere with the conversion.
    4. Finally, the method converts the processed float value to a floating-point number using the float() function.
    5. The resulting float value is returned.
If an error occurs during the conversion process, such as when the input string cannot be converted to a float, a ValueError exception is caught. In such cases, the method returns the error message as a string.
Ensure that the input string represents a valid numerical value before calling this method to avoid conversion errors.



Method Description: check_text_is_present_on_page(driver, check_text)
    
This static method is used to check if a specific text is present on a web page. It takes two parameters: driver represents the web driver instance, and check_text is the text that needs to be checked.
The method performs the following steps to determine if the text is present on the page:
    1. It retrieves the page source of the current web page using the page_source property of the web driver. The page source contains the HTML code of the entire page.
    2. The method then checks if the check_text is present within the page source by using the in operator. It performs a case-sensitive search for an exact match of the text.
    3. If the check_text is found within the page source, the method returns True to indicate that the text is present on the page.
    4. If the check_text is not found within the page source, the method returns False to indicate that the text is not present on the page.
If any exceptions occur during the process, such as issues with retrieving the page source or other unexpected errors, the method catches those exceptions and returns an error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Additionally, provide the check_text parameter with the exact text you want to check for on the page.



Method Description: make_displayed_with_arrow_down_and_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow down" key press and then clicking on the element. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and click on it:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow down" key press using Actions.send_keys(Keys.ARROW_DOWN).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow down" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method performs a click on the element using element.click().
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and clicked successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.


Method Description: make_displayed_with_arrow_up_and_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow up" key press and then clicking on the element. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and click on it:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow up" key press using Actions.send_keys(Keys.ARROW_UP).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow up" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method performs a click on the element using element.click().
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and clicked successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.


Method Description: make_displayed_with_arrow_down_and_enter_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow down" key press and then triggering a click on the element using the "Enter" key. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and trigger a click using the "Enter" key:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow down" key press using actions.send_keys(Keys.ARROW_DOWN).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow down" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method triggers a click on the element by sending the "Enter" key using element.send_keys(Keys.ENTER).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the "Enter" key was triggered successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.



Method Description: make_displayed_with_arrow_up_and_enter_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow up" key press and then triggering a click on the element using the "Enter" key. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and trigger a click using the "Enter" key:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow up" key press using actions.send_keys(Keys.ARROW_UP).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow up" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method triggers a click on the element by sending the "Enter" key using element.send_keys(Keys.ENTER).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the "Enter" key was triggered successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.



Method Description: make_displayed_with_arrow_down_and_space_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow down" key press and then triggering a click on the element using the "Space" key. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and trigger a click using the "Space" key:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow down" key press using actions.send_keys(Keys.ARROW_DOWN).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow down" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method triggers a click on the element by sending the "Space" key using element.send_keys(Keys.SPACE).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the "Space" key was triggered successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.


Method Description: make_displayed_with_arrow_up_and_space_click(driver, element_xpath, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow up" key press and then triggering a click on the element using the "Space" key. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and trigger a click using the "Space" key:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow up" key press using actions.send_keys(Keys.ARROW_UP).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow up" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method triggers a click on the element by sending the "Space" key using element.send_keys(Keys.SPACE).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the "Space" key was triggered successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.


Method Description: make_displayed_with_arrow_down_and_send(driver, element_xpath, send_text, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow down" key press and then sending text to the element. It takes four parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, send_text is the text to be sent to the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and send text:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow down" key press using actions.send_keys(Keys.ARROW_DOWN).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow down" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method sends the send_text parameter to the element using element.send_keys(send_text).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the text was sent successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed and send text to. The send_text parameter should contain the text you want to send to the element. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.



Method Description: make_displayed_with_arrow_up_and_send(driver, element_xpath, send_text, waiting_time)
    
This static method is used to make an element displayed on a web page by simulating the "arrow up" key press and then sending text to the element. It takes four parameters: driver represents the web driver instance, element_xpath is the XPath expression used to locate the element, send_text is the text to be sent to the element, and waiting_time is the maximum waiting time in seconds.
The method performs the following steps to make the element displayed and send text:
    1. It initializes an ActionChains instance to perform keyboard actions on the web page.
    2. The method starts a timer to keep track of the waiting time. The waiting_time parameter determines the maximum time the method waits for the element to become displayed.
    3. Within a loop, the method sends the "arrow up" key press using actions.send_keys(Keys.ARROW_UP).perform() to simulate pressing the key. This action is performed repeatedly until the element is displayed or the waiting time is exceeded.
    4. After each "arrow up" key press, the method tries to locate the element using the provided element_xpath with driver.find_element(By.XPATH, element_xpath). If the element is found, it checks if it is displayed using the is_displayed() method.
    5. If the element is displayed, the method sends the send_text parameter to the element using element.send_keys(send_text).
    6. The method breaks out of the loop and returns True to indicate that the element is displayed and the text was sent successfully.
    7. If the waiting time is exceeded and the element is not displayed, the method catches the TimeoutException and returns the error message "Element not displayed within the timeout".
    8. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression that uniquely identifies the element you want to make displayed and send text to. The send_text parameter should contain the text you want to send to the element. The waiting_time parameter determines the maximum time the method waits for the element to become displayed before timing out.


Method Description: find_href_on_page(driver, find_href)
    
This static method is used to find a specific href attribute value on a web page. It takes two parameters: driver represents the web driver instance, and find_href is the href value to search for.
The method performs the following steps to find the href value on the page:
    1. It uses driver.find_elements_by_tag_name("a") to find all anchor elements (<a>) on the page.
    2. The method iterates over each anchor element in the anchor_elements list.
    3. Inside the loop, it attempts to retrieve the href attribute value of the anchor element using anchor.get_attribute("href").
    4. If the retrieved href value matches the find_href parameter, the method returns True to indicate that the href value is found.
    5. If any NoSuchElementException occurs during the attribute retrieval, it is ignored and the loop continues to the next anchor element.
    6. If none of the anchor elements have a matching href value, the method returns False to indicate that the href is not found on the page.
    7. If any other exceptions occur during the process, the method catches them and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the find_href parameter with the specific href value you want to search for.


Method Description: wait_for_element_to_disappear(driver, element_xpath, waiting_time)
    
This static method is used to wait for an element to disappear from the web page. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression to locate the element, and waiting_time is the maximum time to wait for the element to disappear, in seconds.
The method performs the following steps to wait for the element to disappear:
    1. It uses the WebDriverWait class to create a wait object, specifying the driver instance and the waiting_time parameter as the maximum wait time.
    2. The method uses the wait.until(EC.invisibility_of_element_located((By.XPATH, element_xpath))) statement to wait until the element located by the provided element_xpath disappears from the page.
    3. Once the element has disappeared within the specified waiting time, the method returns True to indicate that the element has successfully disappeared.
    4. If the element does not disappear within the waiting time or if any exceptions occur during the wait, the method catches the exception and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression to locate the element you want to wait for. The waiting_time parameter determines the maximum time to wait for the element to disappear.



Method Description: wait_for_element_to_appear(driver, element_xpath, waiting_time)
    
This static method is used to wait for an element to appear on the web page. It takes three parameters: driver represents the web driver instance, element_xpath is the XPath expression to locate the element, and waiting_time is the maximum time to wait for the element to appear, in seconds.
The method performs the following steps to wait for the element to appear:
    1. It uses the WebDriverWait class to create a wait object, specifying the driver instance and the waiting_time parameter as the maximum wait time.
    2. The method uses the wait.until(EC.presence_of_element_located((By.XPATH, element_xpath))) statement to wait until the element located by the provided element_xpath appears on the page.
    3. Once the element has appeared within the specified waiting time, the method returns True to indicate that the element has successfully appeared.
    4. If the element does not appear within the waiting time or if any exceptions occur during the wait, the method catches the exception and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression to locate the element you want to wait for. The waiting_time parameter determines the maximum time to wait for the element to appear.



Method Description: check_text_in_class(driver, element_xpath, class_text, waiting_time)
    
This static method is used to check if a specified text is present in the class attribute of an element on a web page. It takes four parameters: driver represents the web driver instance, element_xpath is the XPath expression to locate the element, class_text is the text to search for in the element's class attribute, and waiting_time is the maximum time to wait for the element to be available, in seconds.
The method performs the following steps to check the presence of the specified text in the element's class attribute:
    1. It uses the WebDriverWait class to create a wait object, specifying the driver instance and the waiting_time parameter as the maximum wait time.
    2. The method uses the wait.until(EC.presence_of_element_located((By.XPATH, element_xpath))) statement to wait until the element located by the provided element_xpath becomes available on the page.
    3. Once the element is available within the specified waiting time, the method retrieves the value of the element's class attribute using element.get_attribute("class").
    4. It checks if the class_text is present in the retrieved class attribute. If the text is found, the method returns True to indicate that the specified text is present in the element's class attribute. Otherwise, it returns False.
    5. If the element is not available within the waiting time or if any exceptions occur during the process, the method catches the exception and returns the error message as a string.
Ensure that the driver instance is properly initialized and represents a loaded web page before calling this method. Provide the element_xpath parameter with the XPath expression to locate the element of interest. Specify the class_text parameter with the text you want to search for within the element's class attribute. The waiting_time parameter determines the maximum time to wait for the element to be available.



Method Description: double_click_element(driver, element_xpath)
    
This static method is used to perform a double click on a specific element identified by its XPath on a web page. It takes two parameters: driver represents the web driver instance, and element_xpath is the XPath expression to locate the target element.
The method executes the following steps to perform a double click on the element:
    1. It locates the element using the provided element_xpath by calling driver.find_element_by_xpath(element_xpath).
    2. An ActionChains object is created to enable performing advanced interactions. This object is assigned to the actions variable.
    3. The actions.double_click(element).perform() statement is used to perform a double click on the identified element. The double_click() method is called on the actions object, passing the element as the argument. The perform() method executes the double click action.
    4. Once the double click action is performed successfully, the method returns True to indicate the successful execution.
    5. If any exceptions occur during the process, the method catches the exception and returns the error message as a string.
Make sure to initialize the driver instance and navigate to a web page before calling this method. Provide the element_xpath parameter with the XPath expression to locate the element that you want to double click.


Method Description: click_ok_in_alert(driver, waiting_time)
    
This static method is used to handle an alert window on a web page by clicking the "OK" button. It takes two parameters: driver represents the web driver instance, and waiting_time is the maximum time to wait for the alert to appear.
The method executes the following steps to handle the alert:
    1. It waits for the alert to appear using the provided waiting_time by creating a WebDriverWait object and calling the until() method with EC.alert_is_present() condition.
    2. Once the alert is present, the method switches the driver's focus to the alert using Alert(driver) and accepts it by calling the accept() method. This action clicks the "OK" button on the alert.
    3. If the "OK" button is clicked successfully, the method returns True to indicate the successful execution.
    4. If no alert window is present within the specified waiting time, the method returns the string "No alert window present".
    5. If any exceptions occur during the process, the method catches the exception and returns an error message containing the exception details.
Make sure to initialize the driver instance and navigate to a web page before calling this method. Adjust the waiting_time parameter as needed to accommodate the time it takes for the alert to appear.



