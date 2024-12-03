import http.client
import json

from config import constans


def start_game(game_id, session_id, request_header_payload):
    """
        启动游戏会话的函数。

        :param game_id: 游戏ID
        :param session_id: 会话ID
        :param request_header_payload: Base64编码的payload字符串
        :return: 服务器响应的内容
        """
    conn = http.client.HTTPSConnection(constans.RPG_GO_BACKEND_URL)

    # 创建请求体的payload
    request_body = json.dumps({
        "game_id": game_id,
        "session_id": session_id
    })

    # 创建请求头
    headers = {
        'Authorization': constans.RPG_GO_BACKEND_AUTH_TOKEN,
        'payload': request_header_payload,
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': constans.RPG_GO_BACKEND_URL,
        'Connection': 'keep-alive'
    }

    # 发送POST请求
    conn.request("POST", constans.RPG_GO_START_GAME_URI, request_body, headers)

    # 获取响应
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def format_game_data(response):
    data = response.get('data', {})

    # 提取需要的字段
    name = data.get('name', 'N/A')
    game_id = data.get('game_id', 'N/A')
    background = data.get('background', 'N/A')
    intro = data.get('intro', 'N/A')

    # 格式化输出
    formatted_output = (
        f"游戏名称：{name}\n"
        f"游戏ID：{game_id}\n"
        f"游戏背景：{background}\n"  # Assuming background might be a multiline string
        f"游戏介绍：{intro}\n"
    )

    return formatted_output


def format_chapter_info(chapter_data):
    """
    格式化章节信息，包括章节名称、章节ID和背景。

    :param chapter_data: 'chapter' 字典数据
    :return: 格式化的字符串
    """
    if not chapter_data:
        return "章节信息不可用\n"

    # 尝试获取字段
    name = chapter_data.get('name')
    chapter_id = chapter_data.get('chapter_id')
    background = chapter_data.get('background')

    # 初始化格式化结果的列表
    formatted_lines = []

    # 逐个检查和添加每个字段
    if name is not None:
        formatted_lines.append(f"章节名称：{name}")

    if chapter_id is not None:
        formatted_lines.append(f"章节ID：{chapter_id}")

    if background is not None:
        formatted_lines.append(f"章节背景：\n{background}")

    # 将列表中的所有字符串用换行符连接
    return '\n'.join(formatted_lines) + '\n'


def format_init_dialog(dialogs):
    """
    格式化初始对话信息。

    :param dialogs: 包含对话信息的列表
    :return: 格式化后的对话字符串
    """
    if not dialogs:
        return "初始对话不可用\n"

    formatted_dialogs = []

    for dialog in dialogs:
        character_id = dialog.get('character_id', '未知ID')
        message = dialog.get('message', '')
        name = dialog.get('name', '未知角色')
        formatted_dialog = f"{name}({character_id}) 说: {message}"
        formatted_dialogs.append(formatted_dialog)

    return '\n'.join(formatted_dialogs) + '\n'


def format_for_wechat(dialogs):
    """
    格式化对话文本为微信聊天卡片风格。实际也一般

    :param dialogs: 列表，每个元素是一个包含character_id, message和name的字典
    :return: 格式化后的字符串
    """
    formatted_texts = []

    for dialog in dialogs:
        character_id = dialog.get('character_id', '未知ID')
        message = dialog.get('message', '')
        name = dialog.get('name', '未知角色')
        if name == '':
            name = '未知角色'
        # 将Markdown中的强调符号替换成全角符或其他符号来增强显著性
        formatted_message = message.replace('*', '').replace('`', '')

        # 格式化成聊天卡片样式
        formatted_text = f"【{name}】({character_id}) 说:\n{formatted_message}"
        formatted_texts.append(formatted_text)

    return '\n\n'.join(formatted_texts)
