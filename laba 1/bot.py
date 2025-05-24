import random
import telebot

bot = telebot.TeleBot('7902473274:AAHknkD97QtQz7Rc-v3FAGfpwtnZ7MxGaKA')

CARDS = {
    "Гигант": 5,
    "Пека": 7,
    "Ведьма": 5,
    "Принц": 5,
    "Дракончик": 4,
    "Метка": 3,
    "Огненный дух": 1,
    "Лук": 3,
    "Шар": 4,
    "Валькирия": 4,
    "Рыцарь": 3,
    "Мушкетёр": 4,
    "Мини-ПЕККА": 4,
    "Мега-рыцарь": 7,
    "Принцесса": 3,
    "Ледяной дух": 1,
    "Скелеты": 1,
    "Гоблинский бочонок": 2,
    "Огненный шар": 4
}

META_DECKS = {
    "Гигант + Ведьма": ["Гигант", "Ведьма", "Мушкетёр", "Огненный шар", "Валькирия", "Лук", "Гоблинский бочонок",
                        "Ледяной дух"],
    "Мега-рыцарь + Принцесса": ["Мега-рыцарь", "Принцесса", "Мини-ПЕККА", "Шар", "Метка", "Скелеты", "Огненный дух",
                                "Гоблинский бочонок"],
    "Пека + Дракончик": ["Пека", "Дракончик", "Принц", "Огненный шар", "Рыцарь", "Лук", "Ледяной дух", "Метка"]
}

TOP_PLAYERS = [
    "1. Mohamed Light (8234 trophies)",
    "2. Anaban (8215 trophies)",
    "3. Surgical Goblin (8199 trophies)",
    "4. iAmJP (8187 trophies)",
    "5. Mugi (8175 trophies)",
    "6. Richie (8169 trophies)",
    "7. YersonCz (8162 trophies)",
    "8. DiegoB (8158 trophies)",
    "9. Vulkan (8153 trophies)",
    "10. KFC | ZIMMY (8149 trophies)"
]

YOUTUBERS = [
    "🔹 Александр Kplay (https://www.youtube.com/c/KplayCR)",
    "🔹 Clash with Ash (https://www.youtube.com/c/ClashwithAsh)",
    "🔹 Chief Pat (https://www.youtube.com/c/ChiefPat)",
    "🔹 Orange Juice (https://www.youtube.com/c/OrangeJuice)",
    "🔹 Coltonw83 (https://www.youtube.com/c/Coltonw83)",
    "🔹 Clash Royale Россия (https://www.youtube.com/c/ClashRoyaleRussiaOfficial)"
]

CARD_WIN_RATES = {
    "Мега-рыцарь": "53.2%",
    "Ведьма": "48.7%",
    "Гигант": "51.4%",
    "Принцесса": "49.8%",
    "Пека": "52.1%",
    "Мушкетёр": "50.3%",
    "Огненный дух": "47.9%",
    "Лук": "49.5%"
}

def create_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🎲 Случайная колода', '🏆 Топовые колоды')
    markup.row('🔍 Колода по карте', '🏟️ Колода под арену')
    markup.row('📊 Винрейт карт', '👑 Топ игроков')
    markup.row('🎥 Ютуберы по CR', '🧪 Счетчик эликсира')
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "🎮 Привет! Я бот для Clash Royale с полезной информацией.\nВыбери действие:",
        reply_markup=create_keyboard()
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text

    if text == '🎲 Случайная колода':
        deck = random.sample(list(CARDS.keys()), 8)
        response = "🔮 Случайная колода:\n\n" + "\n".join(f"▪️ {card} ({CARDS[card]} эликсира)" for card in deck)
        avg_cost = sum(CARDS[card] for card in deck) / 8
        response += f"\n\nСредняя стоимость: {avg_cost:.1f} эликсира"
        bot.send_message(message.chat.id, response)

    elif text == '🏆 Топовые колоды':
        response = "🏆 Топовые колоды:\n\n"
        for name, deck in META_DECKS.items():
            avg_cost = sum(CARDS[card] for card in deck) / 8
            response += f"🔹 {name} (Сред. стоимость: {avg_cost:.1f}):\n"
            response += "\n".join(f"▪️ {card} ({CARDS[card]} эликсира)" for card in deck) + "\n\n"
        bot.send_message(message.chat.id, response)

    elif text == '🔍 Колода по карте':
        msg = bot.send_message(message.chat.id, "Введите название карты (например, Гигант):",
                               reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_card_request)

    elif text == '🏟️ Колода под арену':
        msg = bot.send_message(message.chat.id, "Введите номер арены (от 1 до 16):",
                               reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_arena_request)

    elif text == '📊 Винрейт карт':
        response = "📊 Винрейт карт (последние данные):\n\n"
        for card, rate in CARD_WIN_RATES.items():
            response += f"{card}: {rate} (стоимость: {CARDS.get(card, '?')})\n"
        bot.send_message(message.chat.id, response)

    elif text == '👑 Топ игроков':
        response = "👑 Топ-10 игроков в мире:\n\n" + "\n".join(TOP_PLAYERS)
        bot.send_message(message.chat.id, response)

    elif text == '🎥 Ютуберы по CR':
        response = "🎥 Популярные русскоязычные ютуберы по Clash Royale:\n\n" + "\n".join(YOUTUBERS)
        bot.send_message(message.chat.id, response)

    elif text == '🧪 Счетчик эликсира':
        msg = bot.send_message(message.chat.id,
                               "Отправьте мне колоду из 8 карт (каждую с новой строки или через запятую):",
                               reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, calculate_elixir_cost)

    else:
        bot.send_message(message.chat.id, "Используйте кнопки для взаимодействия", reply_markup=create_keyboard())

def process_card_request(message):
    card = message.text.strip()
    if card not in CARDS:
        bot.send_message(message.chat.id, "❌ Такой карты нет в базе. Попробуйте ещё раз.",
                         reply_markup=create_keyboard())
        return

    other_cards = [c for c in CARDS.keys() if c != card]
    deck = [card] + random.sample(other_cards, 7)
    avg_cost = sum(CARDS[c] for c in deck) / 8
    response = f"🃏 Колода с картой {card} ({CARDS[card]} эликсира):\n\n"
    response += "\n".join(f"▪️ {c} ({CARDS[c]} эликсира)" for c in deck)
    response += f"\n\nСредняя стоимость: {avg_cost:.1f} эликсира"
    bot.send_message(message.chat.id, response, reply_markup=create_keyboard())


def process_arena_request(message):
    try:
        arena = int(message.text)
        if 1 <= arena <= 16:
            deck = random.sample(list(CARDS.keys()), 8)
            avg_cost = sum(CARDS[card] for card in deck) / 8
            response = f"🏟️ Колода для арены {arena}:\n\n"
            response += "\n".join(f"▪️ {card} ({CARDS[card]} эликсира)" for card in deck)
            response += f"\n\nСредняя стоимость: {avg_cost:.1f} эликсира"
            bot.send_message(message.chat.id, response, reply_markup=create_keyboard())
        else:
            bot.send_message(message.chat.id, "❌ Арена должна быть от 1 до 16.", reply_markup=create_keyboard())
    except ValueError:
        bot.send_message(message.chat.id, "❌ Пожалуйста, введите число от 1 до 16.", reply_markup=create_keyboard())


def calculate_elixir_cost(message):
    try:
        if "," in message.text:
            deck = [card.strip() for card in message.text.split(",")]
        else:
            deck = [card.strip() for card in message.text.split("\n")]

        deck = [card for card in deck if card]  # Удаляем пустые строки

        if len(deck) != 8:
            raise ValueError

        total_elixir = 0
        unknown_cards = []
        valid_cards = []

        for card in deck:
            if card in CARDS:
                total_elixir += CARDS[card]
                valid_cards.append(card)
            else:
                unknown_cards.append(card)

        avg_elixir = total_elixir / 8

        if avg_elixir > 4.0:
            deck_type = "Тяжелая (контроль/бейн)"
        elif avg_elixir > 3.3:
            deck_type = "Средняя (универсальная)"
        else:
            deck_type = "Быстрая (цикловая)"

        response = f"🧮 Счетчик эликсира:\n\n"
        response += f"Средняя стоимость: {avg_elixir:.1f}\n"
        response += f"Тип колоды: {deck_type}\n\n"
        response += "Стоимость карт:\n"

        for card in valid_cards:
            response += f"{card}: {CARDS[card]} эликсира\n"

        if unknown_cards:
            response += f"\n⚠ Неизвестные карты: {', '.join(unknown_cards)}"

        bot.send_message(message.chat.id, response, reply_markup=create_keyboard())

    except:
        bot.send_message(message.chat.id,
                         "❌ Ошибка! Пожалуйста, отправьте ровно 8 карт, каждую с новой строки или через запятую.",
                         reply_markup=create_keyboard())


print("Бот запущен...")
bot.infinity_polling()