import requests
from bs4 import BeautifulSoup
def kino(k,i,j):
    if (j != 'кино'):
        url = 'http://afisha.ngs.ru/afisha/1/'
        r = requests.get(url)
        with open('test.html', 'w') as f:
            f.write(r.text)
            j = 'кино'
    with open('test.html', 'r') as f:
        soup = BeautifulSoup(f,'lxml')
        text = soup.find_all('a', {'class': 'poster-title'})
    requests.post('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/sendMessage?chat_id='+str(k)+'&text=Как насчёт этого?')
    requests.post('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/sendMessage?chat_id='+str(k)+'&text='+text[i].text)
    with open('test.html', 'r') as f:
        soup = BeautifulSoup(f,'lxml')
        text = soup.find_all('a',{'class':'desc_text'})
    requests.post('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/sendMessage?chat_id='+str(k)+'&text='+text[i].text)
    requests.post('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/sendMessage?chat_id='+str(k)+'&text=Если вам не понравился фильм, то повторите команду /cinema ещё раз')

old_message_id = 0
i = 0
old_chat_id = 0
while (1 == 1):
    chat_id = ''
    chat_text = ''
    message_id = ''
    text1 = requests.get('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/getUpdates')
    #message_id
    r = text1.text.rfind('message_id')
    r = r + 12
    while (text1.text[r] != ','):
        message_id = message_id + text1.text[r]
        r = r + 1
    print(message_id)
    #chat_id
    r = text1.text.rfind('id')
    r = r + 4
    while (text1.text[r] != ','):
        chat_id = chat_id + text1.text[r]
        r = r + 1
    if (old_chat_id != chat_id):
        i = 0
    old_chat_id = chat_id
    print(chat_id)

    #text
    r = text1.text.rfind('text')
    r = r + 7
    while (text1.text[r] != '"'):
        chat_text = chat_text + text1.text[r]
        r = r + 1

    #message
    if (chat_text == '/start')and(old_message_id != message_id):
        requests.post('https://api.telegram.org/bot534921788:AAF1aUYd5S62PQY9pKDKK4y7j4SSFbXm9Es/sendMessage?chat_id='+str(chat_id)+'&text=Команды: /cinema')
    if (chat_text == '/cinema')and(old_message_id != message_id): 
        kino(chat_id,i,'')
        i = i+1
    old_message_id = message_id

