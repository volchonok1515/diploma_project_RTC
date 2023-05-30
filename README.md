Итоговый проект по автоматизированному тестированию функционала страницы https://b2c.passport.rt.ru сайта "Ростелеком"

ТЗ описаны в документе по ссылке https://lms.skillfactory.ru/assets/courseware/v1/f78e146f0eb3ace247a28b07e66467de/asset-v1:SkillFactory+QAP-3.0+2021+type@asset+block/Требования_SSO_для_тестирования_last.doc

Тест-кейсы описаны здесь https://docs.google.com/spreadsheets/d/1ypMUlILAqULSM9YgRieUaa6FSsZ_7m1K8Weul-fXCzs/edit?usp=sharing

В закладке Bug-reports описаны ошибки которые были обнаружены в процессе тестировани и в несоответсвии с ТЗ.

При написании тест-кейса использовались методики позитивного и негативного тестирования.

При тестировании применялись библиотеки:

- Selenium
- Pytest

Selenium использывался по причине того что это оптимальный инструмент для автоматизированного управления браузера, он отлдично справляется с большинством операций которые выполняет юзер пользуясь браузером.

Pytest использывался так как эта библиотека обладает широким функционалом для запуска тестов, в данном контексте использывался только функционал запуска тестов и маркировки упавших тестов.

В папке helpers содежится файл data_generator.

Папка pages содержит файлы:

- base_page 
- code_auth_page 
- password_auth_page
- register_page
- restore_password_page

Папка tests содержит файлы:

- test_auth_by_login
- test_auth_by_phone
- test_regist

В корне еще содержатся файлы
conftest и requirements.txt
