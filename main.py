import json

from wxhook import Bot, events
from wxhook.model import Event

from config import constans
from rpg_game import game_util, game_session, rpg_payload

MAPLE_WX_ID = constans.ADMIN_WE_CHAT_ID


# 提取了环境变量设置的功能为一个函数，方便复用和以后进行扩展
def configure_environment():
    import os
    os.environ["WXHOOK_LOG_LEVEL"] = "INFO"  # 修改日志输出级别
    os.environ["WXHOOK_LOG_FORMAT"] = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>"  # 修改日志输出格式


configure_environment()


def on_login(wx_bot: Bot, event: Event):
    wx_bot.send_text(MAPLE_WX_ID, "我已登陆，感觉良好")
    print("登录成功")


def on_start(wx_bot: Bot):
    wx_bot.send_text(MAPLE_WX_ID, "我已打开客户端，感觉一般")
    print("微信客户端打开了")


def on_stop(wx_bot: Bot):
    wx_bot.send_text(MAPLE_WX_ID, "客户端被关闭了")
    print("关闭了微信客户端")


def on_before_message(wx_bot: Bot, event: Event):
    print("消息事件处理之前")


def on_after_message(wx_bot: Bot, event: Event):
    pass
    # wx_msg_handler = event_handlers.get(wx_event.type)
    # if wx_msg_handler:
    #     wx_msg_handler(wx_bot, wx_event)
    # else:
    #     print(f"No wx_msg_handler for wx_event type: {wx_event.type}")
    # wx_bot.send_text(MAPLE_WX_ID, wx_event.content)
    # print(f"消息事件发送到 {MAPLE_WX_ID} 之后")


# 使用Bot配置参数时为了提高可读性，可以按键值对的形式书写
bot = Bot(
    faked_version="3.9.12.17",  # 解除微信低版本限制
    on_login=on_login,
    on_start=on_start,
    on_stop=on_stop,
    on_before_message=on_before_message,
    on_after_message=on_after_message
)


# 消息回调函数的注解改为更加明确的路径表示
@bot.handle(events.TEXT_MESSAGE)
def on_message(wx_bot: Bot, event: Event):
    if event.content == '开始游戏':
        wechat_user_id = event.toUser
        user_session_id = game_session.get_user_session_id(wechat_user_id)
        # 这里也可以做成全局缓存，由于to base64的结果一致性，能用就行
        payload = rpg_payload.generate_rpg_payload(wechat_user_id)
        result = game_util.start_game('GN7MZCKCJ', user_session_id, payload)
        response_object = json.loads(result)

        wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, game_util.format_game_data(response_object))
        wx_bot.send_text(constans.ADMIN_WE_CHAT_ID,
                         game_util.format_chapter_info(response_object.get('data', {}).get('chapter', {})))
        wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, game_util.format_for_wechat(
            response_object.get('data', {}).get('chapter', {}).get('init_dialog', [])))
    elif event.content == '结束游戏':
        wechat_user_id = event.toUser
        game_session.remove_user_session_id(wechat_user_id)

    wx_bot.send_text(constans.ADMIN_WE_CHAT_ID, event.content)


# 启动Bot
if __name__ == "__main__":
    bot.run()
