(Смотрите описание на русском языке ниже после описания на английском)

MrFix. General information.

MrFix is a module with a set of decorator methods for writing UI autotests in Python + Selenium. It contains all the basic methods needed to write UI autotests. It is an open source product. Distributed under the terms of free software. Supports the principle of "all in one and in one place". Allows a beginner (and not a beginner either) autotester not to search for a solution through various manuals and websites, but to immediately find it and use proven working methods in the MrFix module.

Also, the advantage of the module is: • reducing the amount of code when using the module methods; • greater concentration of the autotester on the correct implementation of the autotest logic, and not on its technical part; • the uniformity of the approach of all methods to the form of organization of input data, which simplifies the memorization and application of methods; • reliability ("workability") methods of the module; • continuity of versions of the methods of the module, i.e. the same methods from the new versions of the module will have the same set and sequence of input parameters, so that updating the module does not lead to disruption of the work of ready-made autotests, where older versions of methods were used, also for this, methods with a new set and expanded functionality will receive other names.;

The MrFix module is an ordered and modified by the author of a "combined hodgepodge" of solutions, both found in various manuals and on various websites and subsequently edited by the author of the module, and written directly by the author himself.

Link to the source code:
https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

Installing the MrFix module:
pip install mrfix


Methods of the MrFix module (mrfix)

Here and further in each method, driver is a driver for working with your browser, a variable that is defined as the Webdriver class from the Selenium package:

from selenium import webdriver
driver = webdriver.Firefox()
or
driver = webdriver.Chrome()


List and brief description of methods:


check_exists_xpath(driver, xpath_element) - - checks for the presence of an element with xpath = xpath_element on the page at the moment and returns True or False


click_element(driver, xpath_element) - finds and clicks on an element with xpath = xpath_element, if it does not find this element, it issues the message 'Element {xpath_element} not exists' and drops the test using sys.exit()


click_drop_down_text(driver, xpath_element, element_text) - selects an element with a text equal to the value of element_text from the drop-down list with xpath = xpath_element, while pre-checking the existence of this element, and if it does not exist, it issues the message 'Element {xpath_element} not exists' and drops the test using sys.exit()


send_input_text(driver, xpath_input, input_text) - sends send_message data (character, string, integer or real number) to an input type element with xpath = xpath_input, while pre-checking the existence of this element, and if it does not exist, it issues the message 'Element {xpath_input} not exists' and drops the test using sys.exit()


return_elements_array(driver, xpath_elements) - gets a list of elements with xpath = xpath_elements at the output, while first checking the existence of this xpath_elements, and if it does not exist, it issues the message 'Element {xpath_elements} not exists' and drops the test using sys.exit()


return_elements_array2(driver, xpath_elements) - the method is similar to return_elements_array, only uses slightly different methods "under the hood"


scroll_down_click_element(driver, xpath_down_link) - scrolls the page down and clicks on the element at the bottom of the page with the specified xpath_down_link, it is applied when the element is at the bottom of the page, outside of the part of the screen visible to the autotest, while if the element with such xpath_down_link does not exist, it outputs the message 'Element {xpath_down_link} not exists'


click_element_key_enter(driver, xpath_element) - clicks the "Enter" key on an element, while first checking the existence of this xpath_element, and if it does not exist, it issues the message 'Element {xpath_element} not exists' and drops the test using sys.exit() :

uploading_file(driver, xpath_input_file, file_path) - loads a local file in the field for uploading files with xpath = xpath_input_file, which has the full path to the file + filename = file_path, while pre-checking the existence of this xpath_input_file, and if it does not exist, it outputs the message 'Element {xpath_input_file} not exists' and drops the test using sys.exit()


switch_to_current_window(driver) - switches the autotest to the current active window (it happens acutally when when performing an autotest by clicking on a button or link, a page opens in a new window)


get_elements_attribute(driver, xpath_element, attribute) - returns the value of the attribute attribute of an element with xpath = xpath_element, while if an element with such xpath_element does not exist, it outputs the message 'Element {xpath_element} not exists'

get_elements_text(driver, xpath_element) - returns the displayed text of an element with xpath = xpath_element, while if an element with such an xpath_element does not exist, it outputs the message 'Element {xpath_element} not exists'


select_drop_down_value(driver, xpath_drop_down, drop_down_value) - selects an element with a value equal to drop_down_value from the drop-down list with xpath = xpath_drop_down, while pre-checking the existence of this element, and if it does not exist, it issues the message 'Element {xpath_drop_down} not exists' and drops the test using sys.exit()


select_drop_down_text(driver, xpath_drop_down, drop_down_text) - the method is similar to click_drop_down_text, only uses slightly different methods "under the hood"


clear_input_element(driver, xpath_input_element) - clears the data entry field (and double clearing of the field is used, using two different methods for more reliable operation), which has xpath = xpath_input_element, while pre-checking the existence of this element, and if it does not exist, it issues the message 'Element {xpath_input_element} not exists' and drops test using sys.exit()


pressing_down_arrow_key(driver, n) - presses the "Down arrow" button n-times


pressing_up_arrow_key(driver, n) - presses the "Up arrow" button n-times


pressing_left_arrow_key(driver, n) - presses the "Left arrow" button n-times


pressing_right_arrow_key(driver, n) - presses the "Right arrow" button n-times


pressing_enter_key(driver, n) - presses the "Enter" button n-times


pressing_tab_key(driver, n) - presses the "TAB" button n-times


pressing_backspace_key(driver, n) - presses the "BACKSPACE" button n-times


pressing_delete_key(driver, n) - presses the "DELETE" button n-times


pressing_char_key(driver, char, n) - - presses the symbol (button) char n-times


check_url(url) - checks the existence of the page at the url, returns True or False:


open_url_in_new_tab(driver, url) - opens a page with the url address in a new tab in the browser


check_clickable_element(driver, xpath_element) - checks the "clickability" of an element with xpath = xpath_element, if the element exists, then clicks on it and returns True, otherwise it gives the message "Element is not clickable" and returns False


check_visible_element(driver, xpath_element) - checks an element with xpath = xpath_element by the is_visible() method and returns True or False (if the element does not exist, it also returns False)


check_displayed_element(driver, xpath_element) - checks an element with xpath = xpath_element by the is_displayed() method and returns True or False (if the element does not exist, it also returns False)


get_clipboard_text(driver) - returns ntreott value from Clipboard


convert_string_to_float(string_value) - converts string string_value to a floating-point number (returns this number), correctly processes spaces, dots and commas in the string, if string_value = " (empty string), the method returns 0 (zero)



find_text_on_page(driver, text) - checks for the presence of text on the page, performs a click on the text and returns True if successful, and otherwise returns False


make_element_displayed_and_click(driver, xpath_element) - presses the down arrow key until the element with xpath = xpath_element becomes is_displayed, then clicks on this element


make_element_displayed_and_send(driver, xpath_element, send_text) - presses the down arrow key until the input field with xpath = xpath_element becomes is_displayed, then sends the string send_text to this field


find_href_on_page(driver, link) - searches for the link value in all available hrefs on the page and returns True if successful, otherwise returns False


waiting_process_complete(driver, xpath_process, time_in_second) - waits and checks every 0.5 seconds whether the element with xpath = xpath_process has stopped being is_displayed, in case the element disappears, the method terminates its work, also the method terminates its work after time_in_second seconds, even if the element with xpath_process does not disappear


waiting_appearance_element (driver, xpath_element, time_in_second) - waits and checks every 0.5 seconds whether an element with xpath = xpath_element has appeared (has become is_displayed), if an element appears, the method terminates its work, also the method terminates its work after time_in_second seconds, even if an element with xpath_process does not appear


check_class_in_element(driver, xpath_element, text_in_class) - checks an element with xpath = xpath_element whether its class contains text_in_class as part of the class value, if so, the method returns True, otherwise False








MrFix. Общая информация.

MrFix — модуль с набором методов-декораторов для написания UI-автотестов на Python + Selenium. Он содержит все основные методы, необходимые для написания UI-автотестов. Является продуктом с открытым исходным кодом. Распространяется на условиях бесплатного программного обеспечеия. Поддерживает принцип «все в одном и в одном месте». Позволяет начинающему (и не начинающему тоже) автотестировщику не искать решение по различным мануалам и сайтам, а сразу найти его и использовать проверенные рабочие методы в модуле MrFix.

Также преимуществом модуля является: • уменьшение объема кода при применении методов модуля; • бОльшая сосредоточенность автотестировщика на правильной реализации логики автотеста, а не на технической его части; • однотипность подхода всех методов к форме организации входных данных, что упрощает запоминание и применение методов; • надежность («рабочесть») методов модуля; • преемственность версий методов модуля, т. е. те же самые методы из новых версий модуля будут иметь тот же самый набор и очередность входных параметров, чтобы обновление модуля не привело к нарушению работы уже готовых автотестов, где были применены более старые версии методов, также для этого методы с новым набором и расширенным функционалом будут получать другие названия;

Модуль MrFiх является упорядоченной и доработанной автором «сборной солянкой» решений, как найденных в различных мануалах и на различных сайтах и в последствие отредактированных автором модуля, так и написанных непосредственно самим автором.

Ссылка на исходный код:
https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

Установка модуля MrFix:
pip install mrfix


Методы модуля MrFix (mrfix)

Здесь и далее в каждом методе driver - это драйвер для работы с Вашим браузером, переменная, которая определяется как класс Webdriver из пакета Selenium:

from selenium import webdriver
driver = webdriver.Firefox()
или
driver = webdriver.Chrome()


Список и краткое описание методов:


check_exists_xpath(driver, xpath_element) - - проверяет наличие на данный момент на странице элемента с xpath = xpath_element и возвращает True или False


click_element(driver, xpath_element)  - находит и кликает по элементу с xpath = xpath_element, если не находит этот элемент, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit()


click_drop_down_text(driver, xpath_element, element_text) - выбирает из выпадающего списка с xpath = xpath_element элемент с текстом, равным значению element_text, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit()


send_input_text(driver, xpath_input, input_text) - отправляет в элемент типа input с xpath = xpath_input данные send_message (символ, строка, целое или вещественное число), при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_input} not exists' и роняет тест с помощью sys.exit()


return_elements_array(driver, xpath_elements) - получает на выходе список элементов, у которых xpath = xpath_elements, при  этом предварительно проверяет существование этого xpath_elements, и если его нет, то выдает сообщение 'Element {xpath_elements} not exists' и роняет тест с помощью sys.exit()


return_elements_array2(driver, xpath_elements) - метод аналогичен return_elements_array, только использует немного другие методы "под капотом"


scroll_down_click_element(driver, xpath_down_link) - прокручивает страницу вниз и нажимает на элемент внизу страницы с указанным xpath_down_link, применяется, когда элемент находится внизу страницы, вне видимой для автотеста части экрана, при этом если элемента с таким xpath_down_link не существует, то выдает сообщение 'Element {xpath_down_link} not exists'


click_element_key_enter(driver, xpath_element) - выполняет клик клавишей "Enter" на элементе, при  этом предварительно проверяет существование этого xpath_element, и если его нет, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit() :

uploading_file(driver, xpath_input_file, file_path) - загружает в поле для загрузки файлов с xpath = xpath_input_file локальный файл, у которого полный путь к файлу + имя файла = file_path, , при  этом предварительно проверяет существование этого xpath_input_file, и если его нет, то выдает сообщение 'Element {xpath_input_file} not exists' и роняет тест с помощью sys.exit() 


switch_to_current_window(driver) - переключает автотест на текущее активно окно (бывает акутально, когда при выполнении автотеста по нажатию на кнопку или ссылку открылась страница в новом окне)


get_elements_attribute(driver, xpath_element, attribute) - возвращает значение атрибута attribute элемента, у которого xpath = xpath_element, при этом если элемента с таким xpath_element не существует, то выдает сообщение 'Element {xpath_element} not exists'

get_elements_text(driver, xpath_element) - возвращает отображаемый текст элемента, у которого xpath = xpath_element, при этом если элемента с таким xpath_element не существует, то выдает сообщение 'Element {xpath_element} not exists'


select_drop_down_value(driver, xpath_drop_down, drop_down_value) - выбирает из выпадающего списка с xpath = xpath_drop_down элемент с value, равным значению drop_down_value, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_drop_down} not exists' и роняет тест с помощью sys.exit()


select_drop_down_text(driver, xpath_drop_down, drop_down_text) - метод аналогичен click_drop_down_text, только использует немного другие методы "под капотом"


clear_input_element(driver, xpath_input_element) - очищает поле для ввода данных (причем используется двойная очистка поля, двумя различными методами для более надежного срабатывания), у которого xpath = xpath_input_element, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_input_element} not exists' и роняет тест с помощью sys.exit()


pressing_down_arrow_key(driver, n) - нажимает кнопку "Стрелка вниз" n-раз


pressing_up_arrow_key(driver, n) - нажимает кнопку "Стрелка вверх" n-раз


pressing_left_arrow_key(driver, n) - нажимает кнопку "Стрелка влево" n-раз


pressing_right_arrow_key(driver, n) - нажимает кнопку "Стрелка вправо" n-раз


pressing_enter_key(driver, n) - нажимает кнопку "Enter" n-раз


pressing_tab_key(driver, n) - нажимает кнопку "TAB" n-раз


pressing_backspace_key(driver, n) - нажимает кнопку "BACKSPACE" n-раз 


pressing_delete_key(driver, n) - нажимает кнопку "DELETE" n-раз


pressing_char_key(driver, char, n) - - нажимает символ (кнопку) char n-раз


check_url(url) - проверяет существование страницы по адресу url, выдает True или False:


open_url_in_new_tab(driver, url) - открывает в браузере страницу с адресом url в новой вкладке


check_clickable_element(driver, xpath_element) - проверяет "кликабельность" элемента с xpath = xpath_element, если элемент существует, то кликает на него и возвращает True, иначе выдает сообщение "Element is not clickable" и возвращает False


check_visible_element(driver, xpath_element) - проверяет элемент с xpath = xpath_element методом is_visible() и возвращает True или False (если элемент не существует, то тоже возвращает False)


check_displayed_element(driver, xpath_element) - проверяет элемент с xpath = xpath_element методом is_displayed() и возвращает True или False (если элемент не существует, то тоже возвращает False)


get_clipboard_text(driver) - возвращает ntreott значение из Clipboard


convert_string_to_float(string_value) - преобразует строку string_value в число с плавающей точкой (возвращает это число), корректно обрабатывает в строке пробелы, точки и запятые, если string_value = '' (пустая строка), то метод возвращает 0 (ноль)



find_text_on_page(driver, text) - проверяет наличие текста text на странице, выполяет клик на по тексту и возвращает True в случае успеха, а в противном случае возвращает False


make_element_displayed_and_click(driver, xpath_element) - нажимает клавишу "стрелка вниз" до тех пор, пока элемент с xpath = xpath_element не станет is_displayed, затем кликает на этот элемент


make_element_displayed_and_send(driver, xpath_element, send_text) - нажимает клавишу "стрелка вниз" до тех пор, пока поле для ввода с xpath = xpath_element не станет is_displayed, затем отправляет в это поле строку send_text

    
find_href_on_page(driver, link) - ищет во всех имеющихся на странице href значение link и возвращает True в случае успеха, иначе возвращает False

        
waiting_process_complete(driver, xpath_proccess, time_in_second) - ждет и каждые 0.5 секунды проверяет, перестал ли элемент с xpath = xpath_proccess быть is_displayed, в случае исчезновения элемента метод завершает свою работу, также метод завершает свою работу по истечении time_in_second секунд, даже если элемент с xpath_proccess не исчезнет


waiting_appearance_element (driver, xpath_element, time_in_second) - ждет и каждые 0.5 секунды проверяет, появился ли (стал ли is_displayed) элемент с xpath = xpath_element, в случае появления элемента метод завершает свою работу, также метод завершает свою работу по истечении time_in_second секунд, даже если элемент с xpath_proccess не появится


check_class_in_element(driver, xpath_element, text_in_class) - проверяет у элемента с xpath = xpath_element, содержится ли в его class текст text_in_class как часть значения class, если да, то метод возвращает True, иначе - False




