from telebot import TeleBot, types

bot = TeleBot(token='', parse_mode='html') 

DEFINITOINS = {
    'тн': 'товарная накладная',
    'трн': 'транспортная накладная',
    'ттн': 'товарно-транспортная накладная',
    'торг-12': 'унифицированная форма товарной накладной',
    'торг-2': 'унифицированная форма Акта расхождений',
    'рц': 'распределительный центр',
    '3pl-provider': '3rd party logistics provider; компания, оказывающая логистические услуги',
    'edi': 'Electronic Documents Interchange; Обмен электронными сообщениями (не юридически значимыми)',
    'эдо': 'электронный документооборот (юридически значимые документы)',
    'упд счф': 'универсальный передаточный документ с функцией счета-фактуры',
    'упд счфдоп': 'универсальный передаточный документ с функциями счета-фактуры и товарной накладной',
    'wms': 'Warehouse Management System; система управления складом',
    'tms': 'Transportation Management System; система управления транспортом',
    'sku': 'Stock Keeping Unit; код товара',
    'гтд': 'грузовая таможенная декларация',
    'orders': 'EDI-сообщение: заказ',
    'ordrsp': 'EDI-сообщение: подтверждение заказа',
    'desadv': 'EDI-сообщение: подтверждение отгрузки',
    'recadv': 'EDI-сообщение: подтверждение приемки',
    'invoic': 'EDI-сообщение: счет-фактура',
    'kpi': 'ключевые показатели эффективности; метрики процессов в цепях поставок',
    'cf': 'Case Fill; уровень сервиса при выполнении заказа клиента (отношение количества доставленного количества к заказанному)',
    'otif': 'On-time & In-Full; количество заказов, доставленных вовремя и в полном объеме, к общему количеству заказов',
    'oos': 'Out-of-Stock; отсутствие товара на стоке',
}

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины логистики 🤓\nВведи интересующую аббревиатуру, например, SKU', 
    )

@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
        message.text.lower(), 
    )
    if definition is None:
        bot.send_message(
            chat_id=message.chat.id,
            text='Пока не знаю эту аббревиатуру, но обязательно выучу - возвращайся чуть позже :)',
        )
        return
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Какую аббревиатуру расшифруем следующей?',
    )

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
