from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class Event:
    content: Dict[str, Any]
    base64Img: Optional[str] = None
    data: Optional[Any] = None
    createTime: int = 0
    displayFullContent: str = ''
    fromUser: str = ''
    msgId: int = 0
    msgSequence: int = 0
    pid: int = 0
    signature: Dict[str, Any] = field(default_factory=dict)
    toUser: str = ''
    type: int = 0

    def __post_init__(self):
        # 可以在这里添加初始化后需要执行的逻辑
        print(f"Event created with msgId: {self.msgId}")


# 示例
event_instance = Event(
    content={'msg': {'op': {'@id': '1', 'username': 'wxid_tmiew55xuxb522', 'name': 'lastMessage', 'arg': '{"messageSvrId":"8762582284657574818","MsgCreateTime":"1733209917"}'}}},
    base64Img=None,
    data=None,
    createTime=1733209917,
    displayFullContent='',
    fromUser='wxid_v8c1b7o6h1k622',
    msgId=5813549787807551598,
    msgSequence=735880830,
    pid=10716,
    signature={'msgsource': {'signature': 'v1_pqFMIKvs', 'tmp_node': {'publisher-id': None}}},
    toUser='wxid_tmiew55xuxb522',
    type=51
)

print(event_instance)