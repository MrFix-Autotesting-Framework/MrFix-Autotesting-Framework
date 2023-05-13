MrFix - модуль для UI-автотестов на Python

Предисловие

Несколько лет назад я поменял свою сферу деятельности, уйдя в IT из другой сферы, где я проработал около 20 лет. IT-сообщество дало мне возможность пройти переобучение практически бесплатно, потраченные мною суммы были минимальны.Теперь я QA automation engineer и тимлид небольшой, но качественно и сплоченно работающей команды. И я решил, что пришло время "вернуть долги" IT-сообществу и сделать для него бесплатно тоже что-то более-менее значимое. Так и родилась идея оформить в виде модуля с методами-декораторами те мои методы, которые я использовал в обычной повседневной работе для написания автотестов. Да, их пришлось немного "причесать", но это и хорошо, т.к. всегда до этого руки не доходили. Так и  появился мой модуль MrFix. Вы не ошиблись, "Мистер Фикс" - так я его назвал. Да-да, именно в честь того вредного персонажа из романа Жюль Верна "Вокруг света за 80 дней", который (персонаж) постоянно строил козни главным героям романа. А что, чем не пример идеального QA-инженера? Неутомим, настойчив и постоянно устроивает проверки отличным парням-разработчикам) А те их успешно преодолевают и идут дальше писать свой код. Но мистер Фикс уже ждет их за углом с очередной проверкой) Извините за это лирическое отступление, отвлекся) Итак, перейдем к модулю "Мистер Фикс".

MrFix. Общая информация.

MrFix — модуль с набором методов-декораторов для написания UI-автотестов на Python + Selenium. Он содержит все основные методы, необходимые для написания UI-автотестов. Является продуктом с открытым исходным кодом. Распространяется на условиях бесплатного программного обеспечеия (т.е. позволяет на законных основаниях использовать его в т.ч. и на коммерческих проектах). Поддерживает принцип «все в одном и в одном месте». Позволяет начинающему (и не начинающему тоже) автотестировщику не искать решение по различным мануалам и сайтам, а сразу найти его и использовать проверенные рабочие методы в модуле MrFix.

Также преимуществом модуля является:
• уменьшение объема кода при применении методов модуля; 
• бОльшая сосредоточенность автотестировщика на правильной реализации логики автотеста, а не на технической его части; 
• однотипность подхода всех методов к форме организации входных данных, что упрощает запоминание и применение методов; 
• надежность («рабочесть») методов модуля; 
• преемственность версий методов модуля, т. е. те же самые методы из новых версий модуля будут иметь тот же самый набор и очередность входных параметров, чтобы обновление модуля не привело к нарушению работы уже готовых автотестов, где были применены более старые версии методов, также для этого методы с новым набором и расширенным функционалом будут получать другие названия;

Модуль MrFiх является упорядоченной и доработанной автором «сборной солянкой» решений, как найденных в различных мануалах и на различных сайтах и в последствие отредактированных автором модуля, так и написанных непосредственно самим автором.

Ссылка на исходный код: https://github.com/MrFix-Autotesting-Framework/MrFix-Autotesting-Framework

Установка модуля MrFix: 

  pip install mrfix
  
Пример импорта модуля:
  from mrfix.mrfix import MrFixUI as Mr

Методы модуля MrFix (mrfix)

Здесь и далее в каждом методе driver - это драйвер для работы с Вашим браузером, переменная, которая определяется как класс Webdriver из модуля Selenium:

from selenium import webdriver driver = webdriver.Firefox() или driver = webdriver.Chrome()

Список и краткое описание методов:

check_exists_xpath(driver, xpath_element) - - проверяет наличие на данный момент на странице элемента с xpath = xpath_element и возвращает True или False

click_element(driver, xpath_element)  - находит и кликает по элементу с xpath = xpath_element, если не находит этот элемент, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit()

click_drop_down_text(driver, xpath_element, element_text) - выбирает из выпадающего списка с xpath = xpath_element элемент с текстом, равным значению element_text, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit()

send_input_text(driver, xpath_input, input_text) - отправляет в элемент типа input с xpath = xpath_input данные send_message (символ, строка, целое или вещественное число), при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_input} not exists' и роняет тест с помощью sys.exit()

return_elements_array(driver, xpath_elements) - возвращает на выходе список элементов, у которых xpath = xpath_elements, при  этом предварительно проверяет существование этого xpath_elements, и если его нет, то выдает сообщение 'Element {xpath_elements} not exists' и роняет тест с помощью sys.exit()

return_elements_array2(driver, xpath_elements) - метод аналогичен return_elements_array, только использует немного другие методы "под капотом"

scroll_down_click_element(driver, xpath_down_link) - прокручивает страницу вниз и нажимает на элемент внизу страницы с указанным xpath_down_link, применяется, когда элемент находится внизу страницы, вне видимой для автотеста части экрана, при этом если элемента с таким xpath_down_link не существует, то выдает сообщение 'Element {xpath_down_link} not exists'

click_element_key_enter(driver, xpath_element) - выполняет клик клавишей "Enter" на элементе, при  этом предварительно проверяет существование этого xpath_element, и если его нет, то выдает сообщение 'Element {xpath_element} not exists' и роняет тест с помощью sys.exit() :

uploading_file(driver, xpath_input_file, file_path) - загружает в поле для загрузки файлов с xpath = xpath_input_file локальный файл, у которого полный путь к файлу + имя файла = file_path, , при  этом предварительно проверяет существование этого xpath_input_file, и если его нет, то выдает сообщение 'Element {xpath_input_file} not exists' и роняет тест с помощью sys.exit()

switch_to_current_window(driver) - переключает автотест на текущее активно окно (бывает акутально, когда при выполнении автотеста по нажатию на кнопку или ссылку открылась страница в новом окне)

get_elements_attribute(driver, xpath_element, attribute) - возвращает значение атрибута attribute элемента, у которого xpath = xpath_element, при этом если элемента с таким xpath_element не существует, то выдает сообщение 'Element {xpath_element} not exists'

get_elements_text(driver, xpath_element) - возвращает отображаемый текст элемента, у которого xpath = xpath_element, при этом если элемента с таким xpath_element не существует, то выдает сообщение 'Element {xpath_element} not exists'

select_drop_down_value(driver, xpath_drop_down, drop_down_value) - выбирает из выпадающего списка с xpath = xpath_drop_down элемент с value, равным значению drop_down_value, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_drop_down} not exists' и роняет тест с помощью sys.exit()

select_drop_down_text(driver, xpath_drop_down, drop_down_text) - метод аналогичен click_drop_down_text, только использует немного другие методы "под капотом"

clear_input_element(driver, xpath_input_element) - очищает поле для ввода данных (причем используется двойная очистка поля, двумя различными методами для более надежного срабатывания, т.к. одного метода иногда бывает недостаточно), у которого xpath = xpath_input_element, при  этом предварительно проверяет существование этого элемента, и если его нет, то выдает сообщение 'Element {xpath_input_element} not exists' и роняет тест с помощью sys.exit()

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

get_clipboard_text(driver) - возвращает текстовое содержимое из Clipboard

convert_string_to_float(string_value) - преобразует строку string_value в число с плавающей точкой (возвращает это число), корректно обрабатывает в строке пробелы, точки и запятые, если string_value = '' (пустая строка), то метод возвращает 0 (ноль)

find_text_on_page(driver, text) - проверяет наличие текста text на странице, выполяет клик на по тексту и возвращает True в случае успеха, а в противном случае возвращает False

for_down_make_element_displayed_and_click(driver, xpath_element, time_in_second) - нажимает клавишу "стрелка вниз" до тех пор, пока элемент с xpath = xpath_element не станет is_displayed, затем кликает на этот элемент, причем если за time_in_second секунд элемент не станет is_displayed, то метод тогда завершает свою работу

for_up_make_element_displayed_and_click(driver, xpath_element, time_in_second) - нажимает клавишу "стрелка вверх" до тех пор, пока элемент с xpath = xpath_element не станет is_displayed, затем кликает на этот элемент, причем если за time_in_second секунд элемент не станет is_displayed, то метод тогда завершает свою работу

for_down_make_element_displayed_and_send(driver, xpath_element, send_text, time_in_second) - нажимает клавишу "стрелка вниз" до тех пор, пока поле для ввода с xpath = xpath_element не станет is_displayed, затем отправляет в это поле строку send_text, причем если за time_in_second секунд элемент не станет is_displayed, то метод тогда завершает свою работу

for_up_make_element_displayed_and_send(driver, xpath_element, send_text, time_in_second) - нажимает клавишу "стрелка вверх" до тех пор, пока поле для ввода с xpath = xpath_element не станет is_displayed, затем отправляет в это поле строку send_text, причем если за time_in_second секунд элемент не станет is_displayed, то метод тогда завершает свою работу

find_href_on_page(driver, link) - ищет во всех имеющихся на странице href значение link и возвращает True в случае успеха, иначе возвращает False

waiting_process_complete(driver, xpath_proccess, time_in_second) - ждет и каждые 0.5 секунды проверяет, перестал ли элемент с xpath = xpath_proccess быть is_displayed, в случае исчезновения элемента метод завершает свою работу, также метод завершает свою работу по истечении time_in_second секунд, даже если элемент с xpath_proccess не исчезнет

waiting_appearance_element (driver, xpath_element, time_in_second) - ждет и каждые 0.5 секунды проверяет, появился ли (стал ли is_displayed) элемент с xpath = xpath_element, в случае появления элемента метод завершает свою работу, также метод завершает свою работу по истечении time_in_second секунд, даже если элемент с xpath_proccess не появится

check_class_in_element(driver, xpath_element, text_in_class) - проверяет у элемента с xpath = xpath_element, содержится ли в его class текст text_in_class как часть значения class, если да, то метод возвращает True, иначе - False

Пока на этом все. Могу только добавить, что функционал модуля будет расширяться и улучшаться, планы по развитию уже есть. Буду благодарен за любые отзывы, мнения и комментарии по модулю.

P.S. Для примера раболы модуля MrFix сделал небольшой автотест. Он здесь в репозитории, в файле test_mrfix2.py. Все данные и селекторы тоже размещены в самом файле автотеста, хотя конечно же, по-правильному, их надо разносить в отдельные файлы, здесь это сделано только для того, чтобы показать весь код в одном файле. Зато код сразу можно скопировать себе в IDE и запустить, должен сработать, проверял.
