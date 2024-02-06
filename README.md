<table width="100%" border='0'>
 <tr><td width="40%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/demoqa.png" title="shop" alt="demoqa" width="380" height="200"/></td><td valign="middle">
 <h2>Пример организации автотестирования сайта <a target="_blank" href="https://www.demoqa.com/">www.demoqa.com</a></h2>
 </td></tr>
</table>

### *Проект создан в рамках прохождения курса  школы QA GURU "Автоматизация тестирования на Python"*

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Реализованные проверки](#ballot_box_with_check-реализованные-проверки)
- [Запуск тестов в Jenkins](#-как-запускать-тесты)
- [Allure отчет](#-allure-отчет-о-прохождении-тестов)
- [Видео прохождения тестов](#movie_camera-примеры-видео-прохождения-тестов)
- [Уведомления в Telegram](#-уведомление-в-telegram)
- [Интеграция с Allure TestOps](-интеграция-с-allure-testops)
  
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
> Для перехода в отчет из Jenkins иконки 1 или 2 на скрине

![Screen jenkins1](images/Jenkins3.png)

###### Главный экран (Overview)
![Screen Allure1](images/AllureReport1.png)

*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображается дату и время прохождения теста, общее количество тест кейсов, а также диаграмма с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты 
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют

<details><summary><strong>Пример описания шагов теста</strong></summary>

![Screen Allure2](images/AllureReport2.png)
</details> 
<details><summary><strong>Пример описания шагов теста c подшагами</strong></summary>
 
![Screen Allure4](images/AllureReport4.png)
</details> 

<details><summary><strong>Вложения для каждого теста: Page sourse, Скриншот, Видео прохождения, Лог.</strong></summary>
 
![Screen Allure3](images/AllureReport3.png)
</details>


## :movie_camera: Примеры видео прохождения тестов:

<details><summary><strong>Отправка формы и проверка данных только с заполнением основных полей</strong></summary>

![This is an image1](images/9cbf866543d960a7eebbbad2ff458039.gif)
</details>

<details><summary><strong>Проверка всплывающей подсказки в текстовом поле</strong></summary>
 
![This is an image2](images/cee079fcebf0ff95a88dd3d06edd86fc.gif)
</details>

## <img width="3%" title="Telegram" src="https://github.com/signacher/signacher/blob/main/images/tg.png"> Уведомление в telegram

После прохождения тестов в телеграмм канал бот присылает уведомление с краткой информацией и ссылкой на отчет. Так же можно добавить уведомления на почту, в `Discord`, `Slack` и другие мессенджеры

<img width="40%" title="Telegram" src="images/telegram.jpg">

### <img width="3%" title="Allure TestOps" src="https://github.com/signacher/signacher/blob/main/images/allure_testops.png"> Интеграция с Allure TestOps
### [Dashboard](https://allure.autotests.cloud/project/4025/dashboards)
Для перехода из Jenkins нажать 3
![Testops1](images/Jenkins3.png)

Все данные о запусках тестов также хранятся в Allure TestOps
![Testops1](images/AllureTestOps1.png)

> <details><summary><strong>TestOps автоматически формирует тест кейсы на основе результатов прохождения тестов</strong></summary>
>
>![Testops4](images/AllureTestOps4.png)
></details>
>
><details><summary><strong>Можно фильтровать тесты и запускать их выборочно непосредственно из TestOps</strong></summary>
>
>![Testops3](images/AllureTestOps3.png)
></details>
>
> - Можно создавать ручные тест кейсы и импортировать их в IDE с помощью плагина
> - Результаты тестирования отображаются в реальном времени во время прохождения теста
> - Можно настроить интеграцию с `Jira`


