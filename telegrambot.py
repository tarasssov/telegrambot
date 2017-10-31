import misc
import requests
import json

token = misc.token

URL = misc.URL

def get_updates():
    url = URL + 'getUpdates'
    print(url)
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    base = data['result'][-1]['message']

    person_or_chat = base['chat']['type']
    id_superchat = base['chat']['id']
    chat_person_id = base['chat']['id']
    message_text = base['text']

    print(chat_person_id, message_text)


    def person_or_chat_func():
        if person_or_chat != 'private':
            chat_person_id = id_superchat


    person_or_chat_func()
    print(chat_person_id)

    return

def main():
    # d = get_updates()
    # with open('text.json','w') as f:
    #     json.dump(d, f, indent=2, ensure_ascii=False)
    get_message()


if __name__ == '__main__':
    main()
