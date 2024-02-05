from datetime import date

import allure

from demoqa_tests.model.data.student import Student, Hobby
from demoqa_tests.model.pages import student_registration_form_module
from demoqa_tests.model.pages.student_registration_form import PracticePage
from demoqa_tests.utils.parser_files import read_txt_file

practice_form = PracticePage()


@allure.label('owner', 'Alexey Telnov')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration')
@allure.tag('Form')
@allure.link('https://demoqa.com/automation-practice-form', name="Demo QA")
@allure.epic('Forms')
@allure.feature('Practice Form')
@allure.story('Отправка валидно заполненной формы')
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
    with allure.step('Opening the registration page'):
        practice_form.open()
    with allure.step('Filling out the form'):
        practice_form.fill(student).submit()
    with allure.step('Checking the values of the resulting form'):
        practice_form.assert_results_registration(student)


@allure.label('owner', 'Alexey Telnov')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration with required fields')
def test_registration_required_field():
    with allure.step('Opening the registration page'):
        student_registration_form_module.opening()
    with allure.step('Filling out the form'):
        student_registration_form_module.fill_registration_form(*read_txt_file('student.txt'))
    with allure.step('Checking the values of the resulting form'):
        student_registration_form_module.assert_results_registration(
            [('Student Name', 'Ivan Ivanov'),
             ('Gender', 'Male'),
             ('Mobile', '8988888888'),
             ('Date of Birth', '05 February,2024')
            ])