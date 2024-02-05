import allure
from demoqa_tests.model.pages.alerts import AlertsPage
import pytest
alerts = AlertsPage()


@allure.label('owner', 'Alexey Telnov')
@allure.title('Alert confirmation')
@allure.tag('Alerts')
@allure.link('https://demoqa.com/alerts', name="Demo QA")
@allure.epic('Alerts, Frame & Windows')
@allure.feature('Alerts')
@allure.story('Проверка текста оповещения')
@pytest.mark.skip
def test_text_alert():
    with allure.step('Открываем страницу с оповещениями'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_alert()
    with allure.step('Assert alert text'):
        text_alert = alerts.get_alert_text()
        assert text_alert == 'You clicked a button'


@allure.label('owner', 'Alexey Telnov')
@allure.title('Alert confirmation')
@allure.tag('Alerts')
@allure.link('https://demoqa.com/alerts', name="Demo QA")
@allure.epic('Alerts, Frame & Windows')
@allure.feature('Alerts')
@allure.story('Подтверждение оповещения')
@pytest.mark.skip
def test_confirm_alert():
    with allure.step('Открываем страницу с оповещениями'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_confirm()
    with allure.step('Check alert confirmation'):
        alerts.assert_confirm_alert()


@allure.label('owner', 'Alexey Telnov')
@allure.title('Alert confirmation')
@allure.tag('Alerts')
@allure.link('https://demoqa.com/alerts', name="Demo QA")
@allure.epic('Alerts, Frame & Windows')
@allure.feature('Alerts')
@allure.story('Подтверждение оповещения с заполнением текстового поля')
@pytest.mark.skip
def test_prompt_alert():
    with allure.step('Открываем страницу с оповещениями'):
        alerts.open()
    with allure.step('Нажимаем кнопку Click me'):
        alerts.click_btn_with_prompt()
    with allure.step('Вводим значение в текстовое поле'):
        alerts.type_to_alert('ivanivanov')
    with allure.step('Проверям текст оповещения'):
        alerts.assert_prompt_alert('ivanivanov')
