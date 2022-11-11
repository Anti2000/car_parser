from typing import NamedTuple
import requests
#
# class Ad(NamedTuple):
#     id: int
#     signer_id: int
#     owner_id: int
#     text: str
#     comments: str
#
#
# class VKAPI:
#
#     def get_an_ad_from_a_group_in_vk(self, domain: str, count: int = 1) -> Ad:
#         BASE_URL = 'https://api.vk.com/method/wall.get'
#         TOKEN = "572477c6572477c6572477c67b5434c57c55724572477c63405f601773f64afdbf3668b"
#         VERSION = 5.131
#         FIRST_AD = 0
#
#         params = {
#             'access_token': TOKEN,
#             'v': VERSION,
#             'domain': domain,
#             'count': count,
#         }
#
#         try:
#             response = self._send_request(BASE_URL, params)
#             #print(response)
#             ad = response['response']['items'][FIRST_AD]
#
#             return Ad(
#                 id=ad['id'],
#                 signer_id=ad.get('signer_id', 0),
#                 owner_id=ad['owner_id'],
#                 text=ad['text'],
#                 comments=ad['comments']
#
#             )
#
#         except requests.exceptions.RequestException:
#             pass
#
#   #      https://api.vk.com/method/wall.getComments({"owner_id": owner_id, "post_id": post_id, "offset": offset+100*i, "count": cur_count, "need_likes":1})["items"]
#         # API.wall.getComments({"owner_id": owner_id, "post_id": post_id, "offset": offset+100*i, "count": cur_count, "need_likes":1})["items"];
#
# def main() -> None:
#     # bezdenegavtonet
#     groups = ['orenkoruto', 'tapki_56', 'avto_orenburg56']
#
#     vk_api = VKAPI()
#
#     for group in groups:
#         posts = vk_api.get_an_ad_from_a_group_in_vk(group)
#         print(posts)
#
#
#
# if __name__ == '__main__':
#     main()


# def average():
#     count = 0
#     summ = 0
#     average = 0
#
#     while True:
#         try:
#             x = yield average
#         except StopIteration:
#             print('Done')
#         else:
#             count += 1
#             summ += x
#             average = round(summ / count, 2)
#
#
# a = average()
# print(a.send(None))
# print(a.send(5))
# print(a.send(7))
# print(a.send(13))


def get_an_ad_from_a_group_in_vk():
    BASE_URL = 'https://api.vk.com/method/wall.getComments'
    TOKEN = "572477c6572477c6572477c67b5434c57c55724572477c63405f601773f64afdbf3668b"
    VERSION = 5.131
    FIRST_AD = 0

    #      https://api.vk.com/method/wall.getComments({"owner_id": owner_id, "post_id": post_id, "offset": offset+100*i, "count": cur_count, "need_likes":1})["items"]
    # API.wall.getComments({"owner_id": owner_id, "post_id": post_id, "offset": offset+100*i, "count": cur_count, "need_likes":1})["items"];

    params = {
        'access_token': TOKEN,
        "owner_id": 678033511,
        "post_id": 215302,
        # "offset": 1,
        # "count": 1,
        # "need_likes": 1
        # 'access_token': TOKEN,
        # 'v': VERSION,
        # 'domain': domain,
        # 'count': count,
    }

    response = requests.get(BASE_URL,params)

    for i in response:
        print(i)

    print(response)





get_an_ad_from_a_group_in_vk()
print(1)