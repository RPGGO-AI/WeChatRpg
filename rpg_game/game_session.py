import random
import string

# 全局字典，用于存储键值对
RPG_USER_SESSION_DICT = {}


def generate_rpg_session_id(length=32):
    """生成一个以 wechat_ 开头的随机字符串，长度为32."""
    # 生成一个指定长度的随机字符串（减去'wechat_'的长度）
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length - 7))
    return "wechat_" + random_string


def get_user_session_id(key):
    """根据给定的key获取value，如果不存在则创建新value."""
    global RPG_USER_SESSION_DICT  # 声明使用全局变量
    # 如果key不存在于字典中，添加新的key-value对
    if key not in RPG_USER_SESSION_DICT:
        RPG_USER_SESSION_DICT[key] = generate_rpg_session_id()
    return RPG_USER_SESSION_DICT[key]


def remove_user_session_id(key):
    RPG_USER_SESSION_DICT[key] = None
