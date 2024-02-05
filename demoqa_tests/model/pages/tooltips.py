import time
from selene import have, be
from selene.support.shared import browser


class TooltipPage:

    def open(self):
        browser.open('/tool-tips')
        if browser.element('.fc-button-label').should(be.visible):
            browser.element('.fc-button-label').click()
        else:
            pass
        browser.driver.execute_script('$("#fixedban").remove()')
        return self

    def set_focus_in_field(self):
        browser.element('#toolTipTextField').click()
        time.sleep(1)
        browser.element('#toolTipTextField').click()
        return self

    def assert_text(self):
        browser.element('.tooltip-inner').should(have.text('You hovered over the text field'))
        return self