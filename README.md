<h1 align="center"> Проект по автоматизации тест-кейсов мобильного приложения Wikipedia </h1>

## Используемые инструменты

<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" title="python" alt="python" width="40" height="40"/>&nbsp  
<img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" title="pytest" alt="pytest" width="40" height="40"/>&nbsp  
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184103699-d1b83c07-2d83-4d99-9a1e-83bd89e08117.png" title="selene" alt="selene" width="40" height="40"/>&nbsp  
<img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp  
<img src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" title="jenkins" alt="jenkins" width="40" height="40"/>&nbsp
<img src="/resources/images/allure-icon.png" title="allure" alt="allure" width="40" height="40"/>&nbsp
<img src="/resources/images/AllureTestOps.png" title="allure" alt="allure" width="40" height="40"/>&nbsp
<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="40" height="40"/>&nbsp
</div>

## Запуск тестов и получение отчета

### **Для локального запуска тестов необходимо:**

1. Открыть Android Studio и запустить эмулятор
2. В терминале запустить Appium

<details><summary>2. Склонировать репозиторий</summary>

```
https://github.com/yulya9999/wikipedia-mobile-project-tests.git
```

</details>

<details><summary>3. Установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=local_emulator  # запуск теста в контексте local_emulator
pytest --context=bstack          # запуск теста в контексте bstack
```

</details>

<details><summary>4. Получить отчет о прохождении тестов в allure</summary>

```
allure serve test/allure-results/
```

</details>

После выполнения команды откроется браузер с отчетом

<details><summary>Пример отчета</summary>

<img src="resources/images/allure-report-1.png">

</details>

### **Для удаленного запуска тестов необходимо:**

1. Открыть [проект на Jenkins](https://jenkins.autotests.cloud/job/wikipedia-mobile-project-tests/)
2. Нажать на кнопку "Build Now" и дождаться окончания выполнения тестов

<details><summary>Пример</summary>

<img src="resources/images/jenkins-build-now.png">

</details>

3. Для получения отчета о прохождении тестов
   в [Allure](https://jenkins.autotests.cloud/job/wikipedia-mobile-project-tests/5/allure/), следует нажать на
   иконку<img src="/resources/images/allure-icon.png" title="allure" alt="allure" width="20" height="20"/>

- ***Пример отчета в Allure***

<img src="resources/images/allure-report-2.png">

5. После прохождения тестов, в telegram придет сообщение с отчетом

<details><summary>Пример отчета в telegram</summary>

<img src="resources/images/telegram-report.png" alt="report Telegram">

</details>


