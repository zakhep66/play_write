import os
import time

import dotenv
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(
        headless=False
    )  # Вы можете установить headless=True для работы в фоновом режиме
    page = browser.new_page()
    page.goto("https://mail.tm/ru/", wait_until='load')  # URL страницы входа почтового сервиса

    dotenv.load_dotenv()

    page.click('button[title="Выйти"]')  # Иконка нынешнего пользователя

    button_xpath = "//button[.//span[text()='Войти']]"
    page.click(button_xpath)  # Кнопка Войти

    # Заполнение полей формы и выполнение входа
    page.fill('input[name="address"]', os.environ.get("EMAIL_ADDRESS"))
    page.fill('input[name="password"]', os.environ.get("EMAIL_PASSWORD"))

    button_xpath1 = "//span[.//button[text()='Войти']]"
    page.click(button_xpath1)  # Кнопка Войти

    a_xpath = "//ul[.//li[.//a]]"
    page.click(a_xpath)

    print(page.inner_text("h2"))
    print(page.inner_text('div[dir="ltr"]'))

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
