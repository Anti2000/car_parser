import time
import requests

import datetime
import telebot

other_domain = ("bezdenegavtonet",
                "orenkoruto",
                "tapki_56"
                )


class group1:


    def send_telegram(text: str):
        token = "5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM"
        url = "https://api.telegram.org/bot"
        channel_id = "@vk_parser2"
        url += token
        method = url + "/sendMessage"

        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })

        if r.status_code != 200:
            raise Exception("post_text error")

    # def telegram_bot(message):
    #     token = '5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM'
    #     bot = telebot.TeleBot(token)
    #     chat_id = '597890895'
    #     # text = 'Hello python'
    #     bot.send_message(chat_id, message)
    #    # 1001599781941

    def checking_new_posts(posts, post_ids, oldpost_id: int = 0):
        for post in posts:
            post_id = post['id']
            print('Post_id', post_id)
            latest_post_id = post_id

        print("checking vk", latest_post_id, "post id", oldpost_id)

        if latest_post_id > oldpost_id:
            print("output info about new post")
            group1.outputing_posts(posts)
            oldpost_id = latest_post_id

        time.sleep(5)
        print("checking vk2", latest_post_id, "post id", oldpost_id)

        return oldpost_id

    def outputing_posts(posts):
        post_ids = []
        for post in posts:
            try:
                timestamp = post['date']
                value = datetime.datetime.fromtimestamp(timestamp)
                post_id = post['id']
                print('Post_id', post_id)
                print(value.strftime('%Y-%m-%d %H:%M:%S'))
                # print(post['url'])
                print(post['signer_id'])
                print(post['owner_id'])
                print(post['text'])

                for count, pic in enumerate(post['attachments']):
                    try:
                        print(pic['photo']['sizes'][-1]['url'])
                    except:
                        pass


            except:
                pass
        text = "https://vk.com/bezdenegavtonet?w=wall-75492648_" + str(post_id)
        # text = post['text'] + str(post_id)

        #  https: // vk.com / bezdenegavtonet?w = wall - 75492648_1146377

        group1.send_telegram(text)
        group1.send_telegram(post['text'])

        # telegram_bot(text)
        # telegram_bot(post['text'])
        post_ids.append(post_id)

        print('\n\n')

        return post_ids

    def taking_posts(count: int = 10):
        token = "572477c6572477c6572477c67b5434c57c55724572477c63405f601773f64afdbf3668b"
        version = 5.131
        domain = "bezdenegavtonet"
        posts = []

        other_domain = ("bezdenegavtonet",
                        "orenkoruto",
                        "tapki_56"
                        )
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                }
                                )

        data = response.json()['response']['items']
        posts.extend(data)

        print(posts)
        return posts

    def main(oldpost_id):
        group1.checking_new_posts(group1.taking_posts(1), group1.outputing_posts(group1.taking_posts(1)))


class group2:
    def send_telegram(text: str):
        token = "5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM"
        url = "https://api.telegram.org/bot"
        channel_id = "@vk_parser2"
        url += token
        method = url + "/sendMessage"

        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })

        if r.status_code != 200:
            raise Exception("post_text error")

    # def telegram_bot(message):
    #     token = '5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM'
    #     bot = telebot.TeleBot(token)
    #     chat_id = '597890895'
    #     # text = 'Hello python'
    #     bot.send_message(chat_id, message)
    #    # 1001599781941

    def checking_new_posts(posts, post_ids, oldpost_id1: int = 0):
        for post in posts:
            post_id = post['id']
            print('Post_id', post_id)
            latest_post_id = post_id

        print("checking vk", latest_post_id, "post id", oldpost_id1)

        if latest_post_id > oldpost_id1:
            print("output info about new post")
            group1.outputing_posts(posts)
            oldpost_id1 = latest_post_id

        time.sleep(5)
        print("checking vk2", latest_post_id, "post id", oldpost_id1)

        return oldpost_id1

    def outputing_posts(posts):
        post_ids = []
        for post in posts:
            try:
                timestamp = post['date']
                value = datetime.datetime.fromtimestamp(timestamp)
                post_id = post['id']
                print('Post_id', post_id)
                print(value.strftime('%Y-%m-%d %H:%M:%S'))
                # print(post['url'])
                print(post['signer_id'])
                print(post['owner_id'])
                print(post['text'])

                for count, pic in enumerate(post['attachments']):
                    try:
                        print(pic['photo']['sizes'][-1]['url'])
                    except:
                        pass


            except:
                pass
        text = "https://vk.com/orenkoruto?w=wall-107167070_" + str(post_id)
        # text = post['text'] + str(post_id)

        #  https: // vk.com / bezdenegavtonet?w = wall - 75492648_1146377

        group2.send_telegram(text)
        group2.send_telegram(post['text'])

        # telegram_bot(text)
        # telegram_bot(post['text'])
        post_ids.append(post_id)

        print('\n\n')

        return post_ids

    def taking_posts(count: int = 10):
        token = "572477c6572477c6572477c67b5434c57c55724572477c63405f601773f64afdbf3668b"
        version = 5.131
        domain = "orenkoruto"
        posts = []

        other_domain = ("bezdenegavtonet",
                        "orenkoruto",
                        "tapki_56"
                        )
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                }
                                )

        data = response.json()['response']['items']
        posts.extend(data)

        print(posts)
        return posts

    def main(oldpost_id1):
        group2.checking_new_posts(group2.taking_posts(1), group2.outputing_posts(group2.taking_posts(1)), oldpost_id1)



if __name__ == '__main__':
    oldpost_id = 0
    oldpost_id1 = 0
    while True:
        oldpost_id = group1.main(oldpost_id)
        oldpost_id1 = group2.main(oldpost_id1)
