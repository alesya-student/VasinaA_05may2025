import allure
import pytest
from time import sleep
from selenium.webdriver.common.by import By

from pages.page import Sibdar


@allure.title('Добавление товар в корзину,'
              'проверка счетчика на плашке значка корзины.')
@allure.severity("Blocker")
def test_add_to_cart():
    test = Sibdar()
    try:
        with allure.step('Открыть сайт.'):
            test.open_sibdar_spb()
        with allure.step('Добавить товар.'):
            test.add_product()
            sleep(3)
        with allure.step('Проверить счетчик.'):
            counter = test.get_cart_counter()
            assert counter == 1
    finally:
        test.close()


@allure.title('Изменение количества товара в корзине.')
@allure.severity("Blocker")
def test_change_cart():
    test = Sibdar()
    try:
        with allure.step('Открыть сайт.'):
            test.open_sibdar_spb()
        with allure.step('Добавить товар.'):
            test.add_product()
            sleep(3)
        with allure.step('Перейти в корзину.'):
            test.go_to_contener()
        with allure.step('Проверить количество товара в корзине.'):
            total = test.get_cart_quantity()
        with allure.step('Изменить количество товара в корзине на +1.'):
            test.change_quantity()
            sleep(3)
        with allure.step('Проверить, что количество товара в корзине'
                         'увеличилось на 1 еденицу.'):
            total_new = test.get_cart_quantity()
        assert total_new == total + 1
    finally:
        test.close()


@allure.title('Удаление товара из корзины.')
@allure.severity("Blocker")
def test_delete_product():
    test = Sibdar()
    try:
        with allure.step('Открыть сайт.'):
            test.open_sibdar_spb()
        with allure.step('Добавить товар.'):
            test.add_product()
            sleep(3)
        with allure.step('Перейти в корзину.'):
            test.go_to_contener()
        with allure.step('Проверить колчество товара в корзине.'):
            total = test.get_cart_quantity()
            assert total == 1
        with allure.step('Удалить товар.'):
            test.delete_product()
        with allure.step('Проверить, что корзина пуста.'
                         'Получаем сообщение: "Корзина пуста,'
                         'необходимо это исправить"'):
            message = test.browser.find_element(By.CSS_SELECTOR,
                                                '#order-list').text
            assert message == 'Корзина пуста, необходимо это исправить'
    finally:
        test.close()
