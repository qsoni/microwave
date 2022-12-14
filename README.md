## Публикация комиксов
Этот проект ищет и загружает комиксы на странницу вк группы.

### Как установить 
Перед запуском пргограммы нужно создать свою группу Вконтакте и своё приложение. 

Создать приложение можно в разделе 'Мои приложения'. Ссылка на него в шапке страницы. [Страница для разработчиков](https://vk.com/dev).

Псоле этого нужно получить свой личный ключ(access_token). Для этого стоит ознакомиться с процедурой [Implicit Flow](https://vk.com/dev/implicit_flow_user). 

 - Вам потребуются следующие права: photos, groups, wall и offline.
 - Так как вы используете standalone приложение, для получения ключа пользователя стоит использовать Implicit Flow.
 - Вам нужно убрать параметр redirect_uri у запроса на ключ. 
 - А Параметр scope указать через запятую, вот так: scope=photos,groups,wall,offline.
 - Токен выглядит как строка наподобие 533bacf01e1165b57531ad114461ae8736d6506a3, она появится в адресной строке, подписанная как access_token.

А также вам нужно получить id своей группы Вконтакте. Как это сделать можно понять из этой [статьи](https://vk.com/faq18062).

Все токены и id, которые были описаны выше, нужно поместить в .env файл, его вы должны создать сами.

Пример .env файла: 
```
VK_ACCESS_TOKEN=vk1.a.DFLUYR28OLIHGFLIUT9pIF9P785P9tfrp969Ppo98tP80T888oRODUYTRO86Edo8FILYfyifydyiskYTDYJTSJRFHGSJYRSZNGRASJSJ
VK_GROUP_ID=465364262
```
Советую использовать [vetrualenv/venv](https://pypi.org/project/python-dotenv/0.9.1/) для изоляции проекта.

Python3 уже должен быть установлен,
затем используйте `pip` ( или `pip3`, если есть конфликт с Python2 ) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить
Чтобы запустить код, в консоли следует прописать `cd` и название папки, в которой находится `main.py`. После нужно прописать `python`, через пробел `main.py`.

Пример запуска:
```
python main.py
```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

