import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# تكوين متغير التوكن الخاص بالبوت على تليجرام
TELEGRAM_BOT_TOKEN = '6658939432:AAFAO3xXHDq_ecjJ_L65-CGlNojAeMsLi-4'

# تكوين متغير التوكن الخاص بOpenAI API
OPENAI_API_KEY = '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'

# تكوين عميل OpenAI
openai.api_key = OPENAI_API_KEY

# تكوين مستوى السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# تعريف الأمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت الذكاء الاصطناعي. أرسل لي أي شيء تريده.')

# تعريف معالج الرسائل
def echo(update: Update, context: CallbackContext) -> None:
    # استخراج النص من الرسالة المستلمة
    user_input = update.message.text
    # استدعاء خدمة OpenAI للحصول على الرد
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50
    )
    # استخراج الرد من الاستجابة
    bot_response = response.choices[0].text.strip()
    # إرسال الرد إلى المستخدم
    update.message.reply_text(bot_response)

def main() -> None:
    # إنشاء تحديث لربط البوت بتليجرام
    updater = Updater(TELEGRAM_BOT_TOKEN)
    # الحصول على المعالج الخاص بالتحديثات
    dispatcher = updater.dispatcher
    # تعريف معالجات الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    # تعريف معالج الرسائل
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    # بدء البوت
    updater.start_polling()
    # تشغيل البوت حتى يتم إيقافه
    updater.idle()

if __name__ == '__main__':
    main()
