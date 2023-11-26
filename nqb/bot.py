import requests
from . import go_cqhttp

class Bot(object):
    def __init__(self, host="http://localhost", port=5700) -> None:
        self.url = f"{host}:{port}"
        # print(go_cqhttp.get_status(self.url))
        if not go_cqhttp.get_status(self.url)["online"]:
            raise Exception("go-cqhttp不在线")
    
    def get_login_info(self):
        return requests.get(url=f"{self.url}/get_login_info").json()["data"]
    
    def set_qq_profile(self):
        return requests.get(url=f"{self.url}/set_qq_profile").json()["data"]
    
    def get_stranger_info(self, user_id: int, no_cache: bool=False):
        return requests.get(url=f"{self.url}/get_stranger_info", params={
                "user_id": user_id,
                "no_cache": no_cache
            }).json()["data"]
    
    def get_friend_list(self):
        return requests.get(url=f"{self.url}/get_friend_list").json()["data"]
    
    def get_unidirectional_friend_list(self):
        return requests.get(url=f"{self.url}/get_unidirectional_friend_list").json()["data"]
    
    def delete_friend(self, user_id: int):
        return requests.get(url=f"{self.url}/delete_friend", params={
                "user_id": user_id
            })
    
    def delete_unidirectional_friend(self, user_id: int):
        return requests.get(url=f"{self.url}/delete_unidirectional_friend", params={
                "user_id": user_id
            })
    
    def send_private_msg(self, user_id: int, message: str, group_id: int=-1, auto_escape: bool=False):
        # https://docs.go-cqhttp.org/cqcode/#%E5%9B%BE%E7%89%87
        params={
            "user_id": user_id,
            "message": message,
            "auto_escape": auto_escape
        }
        if group_id != -1:
            data["group_id"] = group_id
        return requests.get(url=f"{self.url}/send_private_msg", params=params).json()
    
    def send_group_msg(self, message: str, group_id: int, auto_escape: bool=False):
        # https://docs.go-cqhttp.org/cqcode/#%E5%9B%BE%E7%89%87
        return requests.get(url=f"{self.url}/send_group_msg", params={
                "message": message,
                "auto_escape": auto_escape,
                "group_id": group_id
            }).json()

    # def send_msg(self, user_id: int, message: str, auto_escape: bool=False):
    #     # https://docs.go-cqhttp.org/cqcode/#%E5%9B%BE%E7%89%87
    #     return requests.get(url=f"{self.url}/send_msg", params={
    #         "message": message,
    #         "auto_escape": auto_escape,
    #         "user_id": user_id,
    #         "message_type": "private"
    #     }).json()
    
    def get_msg(self, message_id: int):
        return requests.get(url=f"{self.url}/get_msg", params={
                "message_id": message_id
            }).json()["data"]
    
    def delete_msg(self, message_id: int):
        return requests.get(url=f"{self.url}/delete_msg", params={
                "message_id": message_id
            })
    
    def mark_msg_as_read(self, message_id: int):
        return requests.get(url=f"{self.url}/mark_msg_as_read", params={
                "message_id": message_id
            })
    
    def get_group_msg_history(self, message_seq: int, group_id: int):
        return requests.get(url=f"{self.url}/get_group_msg_history", params={
                "message_seq": message_seq,
                "group_id": group_id
            }).json()
    
    def can_send_image(self):
        return requests.get(url=f"{self.url}/can_send_image").json()["data"]["yes"]
