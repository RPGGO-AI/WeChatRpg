import random
import string

# 全局字典，用于存储键值对
global_hash_map = {}


def get_random_string(length=32):
    """生成一个以 wechat_ 开头的随机字符串，长度为32."""
    # 生成一个指定长度的随机字符串（减去'wechat_'的长度）
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length - 7))
    return "wechat_" + random_string


def get_or_create_value(key):
    """根据给定的key获取value，如果不存在则创建新value."""
    global global_hash_map  # 声明使用全局变量
    # 如果key不存在于字典中，添加新的key-value对
    if key not in global_hash_map:
        global_hash_map[key] = get_random_string()
    return global_hash_map[key]


def del_value(key):
    global_hash_map[key] = None
