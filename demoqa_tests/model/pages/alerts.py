from selene import have, be
from selene.support.shared import browser


class AlertsPage:

    def open(self):
        browser.open('/alerts')
        if browser.element('.fc-button-label').should(be.visible):
            browser.element('.fc-button-label').click()
        else:
            pass
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def click_btn_with_confirm(self):
        browser.element('#confirmButton').click()
        return self

    def click_btn_alert(self):
        browser.element('#alertButton').click()
        return self

    def get_alert_text(self):
        alert_window = browser.driver.switch_to.alert
        ttach.add_screenshot()
        alert_text = alert_window.text
        browser.driver.switch_to.alert.accept()
        return alert_text

    def assert_confirm_alert(self):
        browser.driver.switch_to.alert.accept()
        browser.element('#confirmResult').should(have.text("You selected Ok"))
        return self

    def click_btn_with_prompt(self):
        browser.element('#promtButton').click()
        return self

    def type_to_alert(self, text):
        browser.driver.switch_to.alert.send_keys(text)
        browser.driver.switch_to.alert.accept()
        return self

    def assert_prompt_alert(self, text):
        browser.element('#promptResult').should(have.text(f"You entered {text}"))
        return self

    def accept_alert(self):
        browser.driver.switch_to.alert.accept()
