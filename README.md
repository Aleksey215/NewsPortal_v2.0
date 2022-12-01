# NewsPortal_v2.0
Учебный проект SillFactory<br>
Данный ресурс создан для публикации статей и новостей в определенных категориях.<br>

Регистрация пользователей осуществляется через подтверждение по email.<br>
Без регистрации можно только просматривать публикации, а после регистрации можно
подписываться на интересующие разделы, комментировать публикации и получить возможность стать автором.<br>
Авторы, по мимо прочего, могут публиковать новость или статью в выбранной категории или категориях.<br>
Есть уведомление подписчиков (по почте) при появлении новых публикаций в категориях, на которые они подписаны.<br>
Раз в неделю всем(в 8:00 в Понедельник), всем подписчикам приходят сообщения о новых публикациях за прошлую неделю<br>
- Для визуализации используется "Bootstrap"
- Для осуществления регистрации используется "Django-allauth"
- Уведомления и рассылка реализованы через "Celery и Redis"

