package TelegramBot

import TelegramBotApplication
import org.jvnet.hk2.annotations.Service
import org.telegram.telegrambots.bots.TelegramLongPollingBot
import org.telegram.telegrambots.meta.api.methods.send.SendMessage
import org.telegram.telegrambots.meta.api.objects.Update

@Service
class telegramBot: TelegramBotApplication() {

    private val AMyTelegramLongPollingBot = MyTelegramLongPollingBot()

    fun bot() {
        MyTelegramLongPollingBot()
    }

    class MyTelegramLongPollingBot: TelegramLongPollingBot() {
        override fun getBotUsername() = "MavenTelegramBot"
        override fun getBotToken() = "6068520146:AAHjPyQgkOmkS-SIbA6X4Ze-jf3PQkC0DfA"
        override fun onUpdateReceived(update: Update) {
            println("hello")
            val message = update.message
            val chatId = message.chatId
            val userName = update.message.from.userName
            val responseText = if (message.hasText()) {
                val messageText = message.text
                when {
                    messageText == "/start" -> "$userName привіт, я бот написанний на мові *kotlin*, у збірці *maven*"
                    else -> "Ти написав: *$messageText*"
                }
            } else {
                "Вибачте, але я розумію лише текст"
            }
            sendNotification(chatId, responseText)
        }
        private fun sendNotification(chatId: Long, responseText: String) {
            val responseMessage = SendMessage(chatId.toString(), responseText)
            responseMessage.enableMarkdownV2(true)
            execute(responseMessage)
        }
    }
}