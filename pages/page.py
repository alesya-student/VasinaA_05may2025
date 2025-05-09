from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Sibdar:
    def __init__(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.implicitly_wait(10)
    
    def open_sibdar_spb(self):
        """Открытие сайта 'Дикий Сбор'"""
        self.browser.get("https://www.sibdar-spb.ru/")
        self.browser.maximize_window()


    # Добавление товара в корзину.
    def add_product(self):
        # Находим элемент
        button = self.browser.find_element(By.CSS_SELECTOR, "[attr_item='Грузди соленые'][onclick*=\"'204'\"]")
        # Скролл до кнопки "В Корзину".
        self.browser.execute_script("arguments[0].scrollIntoView();", button)
        # Клик по кнопке "В Корзину".
        button.click()


    #  Проверить счетчик товаров на значке корзины:
    def get_cart_counter(self):
    #  получить текущее значение, вытаскиваем текстовое значение, преобразуем в числовое
        counter = self.browser.find_element(By.CSS_SELECTOR, "[class='count_bask_right']")
        return int(counter.text.split()[0])


    # Переход в корзину.
    def go_to_contener(self):
        self.browser.find_element(By.CSS_SELECTOR, "[class='bask_icon']").click()


    # Получение количества товаров в корзине.
    def get_cart_quantity(self):
        quantity = self.browser.find_element(By.CSS_SELECTOR, "[value*='шт']")
        return int(quantity.get_attribute("value").split()[0])


    # Изменение количества товара в корзине (+1)
    def change_quantity(self):
        self.browser.find_element(By.CSS_SELECTOR, "[class='plus_prod']").click()


    # Удаление товара из корзины.
    def delete_product(self):
        self.browser.find_element(By.CSS_SELECTOR, "[class='delet_pr_bas']").click()


    # Закрытие браузера.
    def close(self):
        self.browser.quit()
