from datetime import date

import allure

from demoqa_tests.model.data.student import Student, Hobby
from demoqa_tests.model.pages import student_registration_form_module
from demoqa_tests.model.pages.student_registration_form import PracticePage
from demoqa_tests.utils.parser_files import read_txt_file

practice_form = PracticePage()


@allure.label('owner', 'Alexey Telnov')
@allure.title('Successful registration')
@allure.tag('Form')
@allure.link('https://demoqa.com/automation-practice-form', name="Demo QA")
@allure.epic('Forms')
@allure.feature('Practice Form')
@allure.story('Отправка формы cо всеми валидно заполненным полями')
def test_registration():
    student = Student(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivanov@gmail.com',
        phone='8988888888',
        address='Rostovskaya srt',
        birthday=date(2000, 7, 5),
        gender='Male',
        subject='Economics',
        hobby=[Hobby.Music, Hobby.Sports],
        image='picture.jpg',
        state='Haryana',
        city='Karnal')
    with allure.step('Открываем форму регистрации'):
        practice_form.open()
    with allure.step('Заполняем форму регистрации'):
        practice_form.fill(student).submit()
    with allure.step('Проверяем значения в итоговом окне'):
        practice_form.assert_results_registration(student)


@allure.label('owner', 'Alexey Telnov')
@allure.title('Successful registration with required fields')
@allure.tag('Form')
@allure.link('https://demoqa.com/automation-practice-form', name="Demo QA")
@allure.epic('Forms')
@allure.feature('Practice Form')
@allure.story('Отправка  формы с валидно заполненными основными полями ')
def test_registration_required_field():
    with allure.step('Открываем форму регистрации'):
        student_registration_form_module.opening()
    with allure.step('Заполняем основные поля на форме регистрации'):
        student_registration_form_module.fill_registration_form(*read_txt_file('student.txt'))
    with allure.step('Проверяем значения в итоговом окне'):
        student_registration_form_module.assert_results_registration(
            [('Student Name', 'Ivan Ivanov'),
             ('Gender', 'Male'),
             ('Mobile', '8988888888'),
             ('Date of Birth', '07 February,2024')
            ])