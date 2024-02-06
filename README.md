<table width="100%" border='0'>
 <tr><td width="40%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/demoqa.png" title="shop" alt="demoqa" width="300" height="200"/></td><td valign="middle">
 <h2>Пример организации автотестирования сайта <a target="_blank" href="https://www.demoqa.com/">www.demoqa.com</a></h2>
 </td></tr>
</table>

### *Проект создан в рамках прохождения курса  школы QA GURU "Автоматизация тестирования на Python"*

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Реализованные проверки](#ballot_box_with_check-реализованные-проверки)
- [Запуск тестов в Jenkins](#on-как-запускать-тесты)
- [Allure отчет](#bar_chart-allure-отчет-о-прохождении-тестов)
  
## :heavy_check_mark: Описание:
> - Демо проект по автоматизации тестирования UI сайта <a target="_blank" href="https://demoqa.com/"> demoqa.com<a>
> - Проект создан в рамках обучения на курсе <a target="_blank" href="https://qa.guru/python"> QA GURU Автоматизация тестирования на Python</a>
> - Тесты написаны на языке <code>Python</code> с помощью библиотеки <code>Selene</code>
> - Запуск тестов осуществляется в <code>Jenkins</code> с вариантами выбора браузера и его версии
> - Браузеры запускаются в <code>Docker</code> контейнере с помощью <code>Selenoid</code>
> - По результатам тестов формируется <code>Allure</code> отчет с вложениями (скриншоты, логи, видео прохождения теста)
> - Отправляется уведомление о результатах прохождения тестов в <code>Telegram</code> 
> - Реализована интеграция с <code>AllureTestOps</code> и <code>Jira</code> 
## :gear: Технологии и инструменты:
<div align="center">
  <img src="https://github.com/signacher/signacher/blob/main/images/python.png" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/jenkins.png" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/github.png" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/docker.png" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/selenoid.png" title="Selenoid" alt="Selenoid" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure.png" title="Allure" alt="Allure" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure_testops.png" title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/jira.png" title="Jira" alt="Jira" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/tg.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
</div>

## :ballot_box_with_check: Реализованные проверки:
- [x] Отправка формы и проверка данных всей заполненной формы
- [x] Отправка формы и проверка данных только с заполнением основных полей
- [x] Открытие второй вкладки в браузере
- [x] Проверка всплывающей подсказки в текстовом поле
- [x] Проверка всплывающего окна оповещения
- [x] Проверка всплывающего окна оповещения с вводом текста

## <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> Как запускать тесты:
<h3>Тесты запускаются в <a target="_blank" href="https://jenkins.autotests.cloud/job/demo_qa_ui/"> Jenkins.</a></h3>

1. Нажать кнопку Собрать с параметрами (Build with parameters)
<br></br>
  ![Screen Actions1](images/Jenkins1.png)
<br></br>
2. Выбрать параметры Браузер на котором будут запускаться тесты и версию этого браузера и нажать Собрать (Build)
 <br></br>
  ![Screen Actions1](images/Jenkins2.png)
   <br></br>



## <img width="3%" title="Allure" src="https://github.com/signacher/signacher/blob/main/images/allure_report.png"> Allure отчет о прохождении тестов

Пример отчета по ссылке <a target="_blank" href="https://jenkins.autotests.cloud/job/demo_qa_ui/allure/"> https://jenkins.autotests.cloud/job/demo_qa_ui/allure/</a>

*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображается дату и время прохождения теста, общее количество тест кейсов, а также диаграмма с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты 
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют

###### Главный экран (Owerview)
![Screen Allure1](images/AllureReport1.png)
###### Пример описания шагов теста
![Screen Allure2](images/AllureReport2.png)






