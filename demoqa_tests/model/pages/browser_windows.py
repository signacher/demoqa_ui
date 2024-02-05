from selene import have, be
from selene.support.shared import browser


class WindowPage:

    def open(self):
        browser.open('/browser-windows')
        if browser.element('.fc-button-label').should(be.visible):
            browser.element('.fc-button-label').click()
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def click_btn_new_tab(self):
        browser.element('#tabButton').click()
        return self

    def assert_open_new_tab(self):
        browser.switch_to.window(browser.driver.window_handles[1])
        browser.element('#sampleHeading').should(have.text('This is a sample page'))
        return self
