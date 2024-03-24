import requests
import yaml

# YAMLファイルから設定を読み込む
with open('config.yaml', 'r', encoding='utf-8') as config_file:
    config_str = config_file.read()
config = yaml.safe_load(config_str)

# Discord Webhook URL
WEBHOOK_URL = config['WebhookURL']

def send_embedded_message_via_webhook(embed):
    data = {
        'embeds': [embed]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("正常にメッセージが送信されました。")
    else:
        print("正常にメッセージが送信されませんでした。stats code:", response.status_code)

# コマンドの説明
embed = {
    'title': config['title'],
    'description': config['description'],
    'color': int(config['color'], 0)
}

# Embeddedメッセージを送信
send_embedded_message_via_webhook(embed)