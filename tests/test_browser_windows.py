import allure
from demoqa_tests.model.pages.browser_windows import WindowPage

browser_windows = WindowPage()


@allure.label('owner', 'Alexey Telnov')
@allure.tag('Tab')
@allure.link('https://demoqa.com/browser-windows', name="Demo QA")
@allure.epic('Alerts, Frame & Windows')
@allure.feature('Browser windows')
@allure.story('Открытие второй вкладки в браузере')
@allure.title("Открытие второй вкладки в браузере")
def test_confirm_alert():
    with allure.step('Open browser window page'):
        browser_windows.open()
    with allure.step('Opening a second tab'):
        browser_windows.click_btn_new_tab()
    with allure.step('Check text on open tab'):
        browser_windows.assert_open_new_tab()