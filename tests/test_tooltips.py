import allure
from demoqa_tests.model.pages.tooltips import TooltipPage

tooltips = TooltipPage()


@allure.label('owner', 'Alexey Telnov')
@allure.tag('Tooltip')
@allure.link('https://demoqa.com/tool-tips', name="Demo QA")
@allure.epic('Widgets')
@allure.feature('Tool Tips')
@allure.story('Проверка поля с тултипом')
@allure.title('Text field tooltip')
def test_field_tooltip():
    with allure.step('Opening the hint page'):
        tooltips.open()
    with allure.step('Setting focus on the field'):
        tooltips.set_focus_in_field()
    with allure.step('Check hint text'):
        tooltips.assert_text()
