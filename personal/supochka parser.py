# https://betterprogramming.pub/how-to-get-data-from-telegram-82af55268a4b
# https://stackoverflow.com/questions/50975793/telegram-get-chat-messages-posts-python-telethon
import pymorphy2
from telethon.sync import TelegramClient
# ЧАСТИ РЕЧИ
TAGS =['NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB', 'INFN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ']
my_tags = ['NOUN', 'ADJF', 'ADJS','PRTF', 'PRTS']
analyzer = pymorphy2.MorphAnalyzer(lang='ru')

def get_words(text):
    symbols = ',.<>/?""();:«»-–_•!%+`~\n'
    for symbol in symbols:
        text = text.replace(symbol, ' ')
    return text.lower().split()

def method_filter(word):
    results = analyzer.parse(word)
    for result in results:
        if str(result.methods_stack[0][0]) =='FakeDictionary()':
            return result.word
    return False

def word_filter(word):
    if word.isdigit():
        return False
    results = analyzer.parse(word)
    for result in results:
        if not(set(my_tags) & set(list(result.tag.grammemes))):
            return False
        if 'Abbr' in result.tag:
            return False
    return True

api_id = 28412408
api_hash = 'd3e8d796ea7e08e4ece84f1139736f94'
phone = '79611221841'
client = TelegramClient(phone, api_id, api_hash)
client.start()
messages = client.get_messages(1562086721, limit=100)
may_be_uniq = []

for message in messages:
    words = get_words(message.message)
    filtered_words = list(filter(word_filter, words))
    for word in words:
        word = method_filter(word)
        if word:
            may_be_uniq.append(word)

may_be_uniq.sort()
i = 0
while i < len(may_be_uniq):
    print(*may_be_uniq[i: i + 3], sep='\t\t')
    i += 3

