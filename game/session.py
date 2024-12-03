import http.client
import json


# requestBody = json.dumps({
#    "game_id": "GN7MZCKCJ",
#    "session_id": "1sOjgGg7AGtHPGmRlZxyI1"
# })
def start_game(game_id, session_id, payload_encoded):
    """
        启动游戏会话的函数。

        :param game_id: 游戏ID
        :param session_id: 会话ID
        :param payload_encoded: Base64编码的payload字符串
        :return: 服务器响应的内容
        """
    conn = http.client.HTTPSConnection("backend-pro-qavdnvfe5a-uc.a.run.app")

    # 创建请求体的payload
    request_body = json.dumps({
        "game_id": game_id,
        "session_id": session_id
    })

    # 创建请求头
    headers = {
        'Authorization': 'Bearer 8BD6476DAD6668CC9F5AE65435D54D2515723F3858F9BE8BBC2EDA89714C64A2',
        'payload': payload_encoded,
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'backend-pro-qavdnvfe5a-uc.a.run.app',
        'Connection': 'keep-alive'
    }

    # 发送POST请求
    conn.request("POST", "/open/game/startgame", request_body, headers)

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


# # 示例用法
# json_response = """
# {
#     "code": 0,
#     "msg": "ok",
#     "data": {
#         "chapter": {
#             "name": "🏚️Chapter I Enter the Domain🕸️",
#             "chapter_id": "EH3Hi-X8k",
#             "background": "```\\nIt's Halloween night 🎃, You are Julia Morrison, and ...\\n```"
#         }
#     }
# }
# """
#
# # 将JSON字符串解析为Python字典
# response_object = json.loads(json_response)
#
# # 提取章节信息
# chapter_data = response_object.get('data', {}).get('chapter', {})
#
# # 使用函数格式化章节信息
# formatted_chapter_info = format_chapter_info(chapter_data)
# print(formatted_chapter_info)

import json


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


# # 示例用法
# json_response = """
# {
#     "code": 0,
#     "msg": "ok",
#     "data": {
#         "chapter": {
#             "init_dialog": [
#                 {
#                     "character_id": "C5ET0HPXJ",
#                     "message": "Welcome to our haunted house!",
#                     "name": "The Manor Incarnate"
#                 },
#                 {
#                     "character_id": "CC51FWYKS",
#                     "message": "*Max \"Ghostbuster\" Thompson steps up.*",
#                     "name": "Max \"Ghostbuster\" Thompson"
#                 },
#                 {
#                     "character_id": "CPWQ5EFQB",
#                     "message": "*Olivia \"Witchling\" Alvarez draws herself up with all the poise.*",
#                     "name": "Olivia \"Witchling\" Alvarez"
#                 }
#             ]
#         }
#     }
# }
# """
#
# response_object = json.loads(json_response)
#
# # 提取初始对话信息
# init_dialogs = response_object.get('data', {}).get('chapter', {}).get('init_dialog', [])
#
# formatted_init_dialogs = format_init_dialog(init_dialogs)
# print(formatted_init_dialogs)