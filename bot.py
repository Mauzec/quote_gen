from lib import Quote
from lib.packages.origamibot import OrigamiBot as Bot
from lib.packages.origamibot.listener import Listener
from lib.packages.origamibot.core.teletypes.message import Message

quote = Quote()

def log(message: Message=None, logs='', out=False):
    if message:
        print(f'{message.chat.username}: {message.text}'.replace('\n', ' '))
    if out:
        print('\t\t\tSent:', end=' ')
    if logs:
        print(logs.replace('\n', ' [] '))


class BotCommands:
    def __init__(self, bot: Bot):
        self.bot = bot
    
    def inspiration(self, message: Message):
        text = quote('inspiration')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def motivation(self, message: Message):
        text = quote('motivation')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def love(self, message: Message):
        text = quote('love')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def life(self, message: Message):
        text = quote('life')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def friendship(self, message: Message):
        text = quote('friendship')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)

    def sad(self, message: Message):
        text = quote('sad')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)

    def philosophy(self, message: Message):
        text = quote('philosophy')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def happiness(self, message: Message):
        text = quote('happiness')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def humor(self, message: Message):
        text = quote('humor')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def relationship(self, message: Message):
        text = quote('relationship')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def truth(self, message: Message):
        text = quote('truth')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def funny(self, message: Message):
        text = quote('funny')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def death(self, message: Message):
        text = quote('death')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def god(self, message: Message):
        text = quote('god')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def romance(self, message: Message):
        text = quote('romance')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def hope(self, message: Message):
        text = quote('hope')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def writing(self, message: Message):
        text = quote('writing')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def religion(self, message: Message):
        text = quote('religion')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def success(self, message: Message):
        text = quote('success')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def knowledge(self, message: Message):
        text = quote('knowledge')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def education(self, message: Message):
        text = quote('education')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    
    def music(self, message: Message):
        text = quote('music')
        self.bot.send_message(message.chat.id, text)
        log(None, text, True)
    

class BotListener(Listener):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    def on_new_chat_members(self, message):
        self.bot.send_message(message.chat.id, 'Hi there!')
    
    def on_command_failure(self, message: Message, err=None):
        if err:
            log(None, f'Fatal error on server [{err}]', True)
            self.bot.send_message(message.chat.id, 'Fatal error on server!')
        else:
            log(None, 'Wrong command!', True)
            self.bot.send_message(message.chat.id, 'Wrong command!')
            
    def on_message(self, message):
          log(message)
          
    
from sys import argv
from time import sleep


token = (argv[1] if len(argv) > 1 else input('Enter bot token: '))
bot = Bot(token)
bot.add_commands(BotCommands(bot))
bot.add_listener(BotListener(bot))
bot.start()

while 1:
    sleep(1)