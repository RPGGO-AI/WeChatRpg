import base64
import json

DEFAULT_SOURCE = 'creator'


def make_payload(user_id):
    """与RPGGO生成payload规则一致，使用微信ID作为每个用户对于RPG-GO中的ID"""
    payload = {
        'user_id': user_id,
        'source': DEFAULT_SOURCE,
        'user_type': 1
    }

    # 将payload字典序列化为JSON字符串，并编码为base64
    json_bytes = json.dumps(payload).encode('utf-8')
    base64_bytes = base64.b64encode(json_bytes)

    return base64_bytes.decode('utf-8')
