# 🤖 Telegram text summarization bot туторіал
Telegram text summarization bot туторіал. У даних туторіалах ми створимо телеграм-бот для аналізу тексту. Розглянемо написання коду на мові програмування Python, використаємо сайт Hugging Face з моделями штучного інтелекту для **обробки природної мови**.


## 🎬 Відео-туторіали
* [Туторіал по Telegram text summarization bot. Частина-1](https://www.tiktok.com/@learn.ai.python/video/7249049863529221382?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-2](https://www.tiktok.com/@learn.ai.python/video/7250570710949858565?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-3](https://www.tiktok.com/@learn.ai.python/video/7251675261559770373?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-4](https://www.tiktok.com/@learn.ai.python/video/7252769036990254341?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-5](https://www.tiktok.com/@learn.ai.python/video/7254275181596691718?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-6](https://www.tiktok.com/@learn.ai.python/video/7255008544326487301?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-7](https://www.tiktok.com/@learn.ai.python/video/7257631608868539653?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-8](https://www.tiktok.com/@learn.ai.python/video/7261326752302042373?lang=uk-UA)
* [Туторіал по Telegram text summarization bot. Частина-9](https://www.tiktok.com/@learn.ai.python/video/7262431491018247430?lang=uk-UA)

## 1️⃣ Крок-1
Спочатку ми знаходимо у Telegram ```@BotFather``` для ініціалізації бота. Для старту ```@BotFathe```r виконуємо команду ```/start```. Створюємо нового бота за допомогою команди ```/newbot```. Назвемо цього бота як *Telegram NLP Bot* (заголовок). Придумаємо йому унікальний нікнейм (посилання). І після цього отримаємо секретний токен.

## 2️⃣ Крок-2
Тепер створимо унікальний токен на сайті **[Hugging Face](https://huggingface.co/)**. Це американська компанія, яка розробляє інструменти для створення програм за допомогою машинного навчання. На їх сайті можна знайти купу безкоштовних моделей, готових до використання. Реєструємося, натискаємо на авартку свого профіля. Заходимо у налаштування і у розділі Access Tokens створюємо унікальний токен.

## 3️⃣ Крок-3
У цій частині розпочнемо писати код до бота на мові програмування Python. Спочатку імпортуємо бібліотеки та встановимо необхідні. Після цього авторизуємося у системі власним Hugging Face токеном, власним ```@BotFather``` токеном та задамо шлях до обраної моделі.

<img width="995" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/a07908a1-5632-45cf-a7cc-f06911e2d217">

## 4️⃣ Крок-4
Описуємо функцію ```query()```, за допомогою якої відправлятимемо запити до Hugging Face. Після цього описуємо функцію бота, яка буде спрацьовувати на команду ```/start```. Ця функція міститиме привітальну інформацію для користувача.

<img width="1015" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/41080514-5e44-4f70-a537-e2f579693da6">


## 5️⃣ Крок-5
У цій частині продовжуємо писати код до бота. Опишемо функцію на команду ```\start```.

<img width="1332" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/c591a173-2d3e-4223-8c77-87e977c7bea8">

Також, тут опишемо функцію, що буде спрацьовувати на команду ```/text_summarization.``` Вона містиме підказку для користувача у рядку ```46```, після якої юзер відправляє текст на обробку. Після отримання тексту у рядку ```52``` виводимо відповідну інформацію на екран. У рядках ```56-60``` відправляємо отриманий текст на модель нейромережі для узагальнення тексту. У рядках ```66-67``` парсимо отриманий результат і відправляємо його користувачу.

<img width="819" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/2dd4a6dc-0649-45ff-8ba5-a7a6269866d0">


## 6️⃣ Крок-6
У цій частині продовжуємо писати код до бота. Для краси бота, описуємо функцію ```/help``` для користувача, що міститиме підказку із доступними командами. 

<img width="887" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/39254be0-20c5-4a54-ab86-0515f03666bf">

І у рядках ```85-86``` запускаємо бота.

<img width="795" alt="image" src="https://github.com/learn-ai-python/Telegram_text_summarization_bot/assets/108177042/d654bb94-6859-4980-baec-90f06f2fbda4">

## 7️⃣ Крок-7
У цій частині завершимо оформлення бота. Додаємо опис бота та інформацію, що буде світитися при першому запускові бота. За бажананням, можна відредагувати інші параметри чи додати аватарку до бота.

## 8️⃣ Крок-8
Тепер ми налаштуємо запуск нашого коду. Для цього ми використаємо хмарний сервіс **[PythonAnywhere](https://www.pythonanywhere.com/)**. Для тестування такого бота буде достатньо безкоштовної версії. Тому, реєструємося та створюємо чи заливаємо туди новий файл із розширенням ```*.py```, що буде містити код до бота. Відкриваємо наш файл та натискаємо на кнопку ```Run``` на сайті PythonAnywhere.

## 9️⃣ Крок-9
У заключній частині ми протестуємо нашого бота. Відкриваємо наш телеграм. Переходимо за посиланням до нашого бота. І тестуємо: виконуємо команду ```/start``` для запуску бота. Тепер викличемо команду ```/text_summarization``` для узагальнення тексту. Для прикладу візьмемо текст про штучний інтелект із вікіпедії.

На цьому створення нашого бота завершено! Ставте лайк та підписуйтеся на мій канал, якщо вам сподобалися туторіали!

