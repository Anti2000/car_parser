import time
import requests

import datetime
import telebot

#
# def send_telegram(text: str):
#     token = "5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM"
#     url = "https://api.telegram.org/bot"
#     channel_id = "@vk_parser2"
#     url += token
#     method = url + "/sendMessage"
#
#     r = requests.post(method, data={
#          "chat_id": channel_id,
#          "text": text
#           })
#
#     if r.status_code != 200:
#         raise Exception("post_text error")
#
#
#
# # def telegram_bot(message):
# #     token = '5614491014:AAGefYbZMqEdZi1_EiRc5cxico9e36jNnIM'
# #     bot = telebot.TeleBot(token)
# #     chat_id = '597890895'
# #     # text = 'Hello python'
# #     bot.send_message(chat_id, message)
# #    # 1001599781941
#
#
#
#
#
# def checking_new_posts(posts, post_ids, oldpost_id: int = 0):
#     for post in posts:
#         post_id = post['id']
#         print('Post_id', post_id)
#         latest_post_id = post_id
#
#     print("checking vk", latest_post_id, "post id", oldpost_id)
#
#     if latest_post_id > oldpost_id:
#         print("output info about new post")
#         outputing_posts(posts)
#         oldpost_id = latest_post_id
#
#     time.sleep(5)
#     print("checking vk2", latest_post_id, "post id", oldpost_id)
#
#     return oldpost_id
#
#
# def outputing_posts(posts):
#     post_ids = []
#     for post in posts:
#         try:
#             timestamp = post['date']
#             value = datetime.datetime.fromtimestamp(timestamp)
#             post_id = post['id']
#             print('Post_id', post_id)
#             print(value.strftime('%Y-%m-%d %H:%M:%S'))
#             # print(post['url'])
#             print(post['signer_id'])
#             print(post['owner_id'])
#             print(post['text'])
#
#             for count, pic in enumerate(post['attachments']):
#                 try:
#                     print(pic['photo']['sizes'][-1]['url'])
#                 except:
#                     pass
#
#
#         except:
#             pass
#
#     # text = post['text']
#     text = "https://vk.com/bezdenegavtonet?w=wall-75492648_" + str(post_id)
#     #text = post['text'] + str(post_id)
#
#   #  https: // vk.com / bezdenegavtonet?w = wall - 75492648_1146377
#
#     send_telegram(text)
#     send_telegram(post['text'])
#
#     # telegram_bot(text)
#     # telegram_bot(post['text'])
#     post_ids.append(post_id)
#
#     print('\n\n')
#
#     return post_ids
#
#
# def taking_posts(count: int = 10):
#     token = "572477c6572477c6572477c67b5434c57c55724572477c63405f601773f64afdbf3668b"
#     version = 5.131
#     domain = "bezdenegavtonet"
#     posts = []
#
#     other_domain = ("bezdenegavtonet",
#                     "orenkoruto",
#                     "tapki_56"
#                     )
#     response = requests.get("https://api.vk.com/method/wall.get",
#                             params={
#                                 'access_token': token,
#                                 'v': version,
#                                 'domain': domain,
#                                 'count': count,
#                             }
#                             )
#
#     data = response.json()['response']['items']
#     posts.extend(data)
#
#     return posts
#
#
# def main():
#     post_ids = outputing_posts(taking_posts())
#     oldpost_id = checking_new_posts(taking_posts(1), post_ids)
#     while True:
#         oldpost_id = checking_new_posts(taking_posts(1), post_ids, oldpost_id)
#
#
# if __name__ == '__main__':
#     main()

GROUPS_LIST = ("bezdenegavtonet",
                    "orenkoruto",
                    "tapki_56"
                    )

class Vk_parser:
    def __int__(self):
        self.name = 'qw'

def main():
    for i in GROUPS_LIST:
        parser = i
    Parser(GROUPS_LIST)
    while True:
        sleep(3)


if __name__ == '__main__':
    main()
