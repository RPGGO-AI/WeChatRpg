from enum import Enum, unique


# 取自\wxhook\events.py
@unique
class EventType(Enum):
    NOTICE_MESSAGE = 10000  # 通知消息事件
    SYSTEM_MESSAGE = 10002  # 系统消息事件
    ALL_MESSAGE = 99999  # 全部消息事件
    TEXT_MESSAGE = 1  # 文本消息事件
    IMAGE_MESSAGE = 3  # 图片消息事件
    VOICE_MESSAGE = 34  # 语音消息事件
    FRIEND_VERIFY_MESSAGE = 37  # 好友验证请求消息事件
    CARD_MESSAGE = 42  # 卡片消息事件
    VIDEO_MESSAGE = 43  # 视频消息事件
    EMOJI_MESSAGE = 47  # 表情消息事件
    LOCATION_MESSAGE = 48  # 位置消息事件
    XML_MESSAGE = 49  # XML消息事件
    VOIP_MESSAGE = 50  # 视频/语音通话消息事件
    PHONE_MESSAGE = 51  # 手机端同步消息事件

    @classmethod
    def from_value(cls, v):
        # 提供一个方法来从值获取枚举成员
        for member in cls:
            if member.value == v:
                return member
        raise ValueError(f"No matching EventType for value: {v}")


# 示例：如何从值获取事件类型
# value = 1
# try:
#     event_type = EventType.from_value(value)
#     print(f"匹配的事件是：{event_type.name}")
# except ValueError as e:
#     print(e)
