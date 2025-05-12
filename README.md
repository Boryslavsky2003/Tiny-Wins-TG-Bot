
---

# **Tiny-Wins-TG-Bot** ✨

**Tiny-Wins-TG-Bot** — це телеграм-бот, створений для автоматизації публікації контенту на каналі **Маленькі перемоги**, що включає пости на різноманітні теми, орієнтовані на жінок.

Цей бот допомагає генерувати та публікувати мотиваційний контент на кожен день, забезпечуючи автоматизацію для зручності адміністрування каналу.

---

## **Інсталяція:**

1. **Клонувати репозиторій:**

   ```bash
   git clone https://github.com/boryslavsky2003/Tiny-Wins-TG-Bot.git
   cd Tiny-Wins-TG-Bot
   ```

2. **Встановити залежності:**

   Для початку, вам потрібно встановити всі необхідні бібліотеки Python:

   ```bash
   pip install -r requirements.txt
   ```

3. **Налаштування Telegram API:**
   - Створіть нового бота через [BotFather](https://core.telegram.org/bots#botfather).
   - Отримайте токен вашого бота та збережіть його в `.env` файлі:

     ```bash
     TELEGRAM_TOKEN=your-telegram-bot-token
     ```
     ```
     Для того щоб користуватися ботом, обов'язково потрібно в .env файлі вказати всі параметри
     ```

4. **Запуск бота:**
   - Тепер ви можете запустити бота командою:

     ```bash
     python -m bot.main
     ```

---

## **Підтримка та внесок:**

- Якщо ви хочете запропонувати покращення чи виправлення, будь ласка, створюйте **пул-реквести**.
- Залишайте **зауваження** або **питання** у [Issues](https://github.com/Boryslavsky2003/Tiny-Wins-TG-Bot).

---

## **Ліцензія:**

Цей проект ліцензується на умовах [MIT ліцензії](LICENSE).

---

# .env

### Telegarm Bot Configuration
BOT_TOKEN=

ADMIN_ID=

### Webhook Configuration
WEBHOOK_DOMAIN=

### Channel IDs
UA_CHANNEL_ID=

US_CHANNEL_ID=

### API Keys
HUGGINGFACE_TOKEN=

MODEL_TEXT_URL=

MODEL_IMAGE_URL=

### Scheduling | Format: HH:MM (24-hour)
1_SCHEDULED_TIME=13:30

2_SCHEDULED_TIME=18:30

---

# Commands Bot:

#### start - Start bot
#### get_id - get channel or user ID

---
