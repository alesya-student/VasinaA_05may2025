import allure
import requests
import pytest


base_url_api = 'https://www.sibdar-spb.ru/ajax/basketOrder.php'
"""URL для проверки содержимого корзины:"""
basket_url = 'https://www.sibdar-spb.ru/ajax/basketList.php'
"""Обновлять значение перед новой сессией:"""
Cookie = {"PHPSESSID": "q2gr3cchOVl6UVwXATgBGmE8tbGt9TJi"}
Product_id = "204"
"""следить за актуальностью idCookie в теле запроса"""


@allure.title("Добавление товар в корзину.")
@allure.severity("Blocker")
def test_add_to_cart():
    with allure.step("Отправить POST-запрос для добавления товара."):
        body = {
            "idCookie": "451952",
            "idProd": Product_id,
            "type": "add"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})
    with allure.step("Проверка статус кода."):
        assert response.status_code == 200
    with allure.step("Проверка, что корзина не пустая."):
        cart_response = requests.get(basket_url, cookies=Cookie)
        assert cart_response.text.strip() != ""
        assert cart_response.status_code == 200
    with allure.step("Отправить POST-запрос для удаления товара."):
        body = {
            "idCookie": "451952",
            "idProd": Product_id,
            "type": "delete"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})


@allure.title("Изменение количества товара в корзине.")
@allure.severity("Blocker")
def test_change_cart():
    with allure.step("Отправить POST-запрос для добавления товара."):
        body = {
            "idCookie": "451952",
            "idProd": Product_id,
            "type": "add"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})
    with allure.step("Отправить POST-запрос для изменения"
                     "количества товара на +1."):
        body = {
            "idCookie": "451952",
            "idProd": "204",
            "type": "plus"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})
    with allure.step("Проверить статус код."):
        assert response.status_code == 200


@allure.title("Удаление товара из корзины.")
@allure.severity("Blocker")
def test_delete_product():
    with allure.step("Отправить POST-запрос для добавления товара."):
        body = {
            "idCookie": "451952",
            "idProd": Product_id,
            "type": "add"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})
    with allure.step("Проверка статус кода."):
        assert response.status_code == 200
    with allure.step("Проверка, что корзина не пустая."):
        cart_response = requests.get(basket_url, cookies=Cookie)
        assert cart_response.text.strip() != ""
        assert cart_response.status_code == 200
    with allure.step("Отправить POST-запрос для удаления товара."):
        body = {
            "idCookie": "451952",
            "idProd": Product_id,
            "type": "delete"
        }
        response = requests.post(base_url_api, cookies=Cookie, data=body,
                                 headers={'Content-Type':
                                          'application/x-www-form-urlencoded;'
                                          'charset=UTF-8'})
    with allure.step("Проверит, что корзина пуста."):
        empty_cart_response = requests.get(basket_url, cookies=Cookie)
        assert response.status_code == 200
        assert "Корзина пуста, необходимо это исправить" in empty_cart_response.text
