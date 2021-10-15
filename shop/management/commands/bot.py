from django.conf import settings
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler
from shop.models import Property, Product, Category, Description
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

token = settings.TOKEN
updater = Updater(token, use_context=True)


def start(update, context):
    print('star_update', update)
    print('star_context', context)
    keyboard = []
    reply_markup = InlineKeyboardMarkup(keyboard)
    category = Category.objects.all()
    for cat in category:
        with open(cat.image.path, 'rb') as file:
            update.message.reply_photo(photo=file.read())
        update.message.reply_text(text=cat.description)
        update.message.reply_text(text=cat.name)
        update.message.reply_text(text=cat.id)
        keyboard.append([InlineKeyboardButton(cat.name, callback_data=f'{cat.name}')])
    update.message.reply_text('Виберіть категорію:', reply_markup=reply_markup)


def produkt(update, context):
    keyboard = []

    reply_markup = InlineKeyboardMarkup(keyboard)
    prod = Product.objects.filter(category__name=context)
    print('prod', prod.values())
    print('prod_update', update)
    print('prod_context', context)
    for p in prod:
        with open(p.image.path, 'rb') as file:
            update.callback_query.message.reply_photo(photo=file.read())
        update.callback_query.message.reply_text(text=p.description)
        update.callback_query.message.reply_text(text=p.name)
        keyboard.append([InlineKeyboardButton(p.name, callback_data=f'{p.name}')])
    update.callback_query.message.reply_text('Please choose:', reply_markup=reply_markup)


def menu_actions(update, _: CallbackContext):
    print('actions_update', update)
    print('actions_context', _)
    category = Category.objects.all()
    query = update.callback_query
    # query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")
    for c in category:
        if query.data == c.name:
            produkt(update, c.name)
            print(c.name)


def do_echo(update, context):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Property.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(text=reply_text)


updater.dispatcher.add_handler(CommandHandler('start', start))
message_handler = MessageHandler(Filters.text, do_echo)
updater.dispatcher.add_handler(message_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(menu_actions))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
updater.idle()


