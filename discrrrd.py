from discord_webhook import DiscordWebhook
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1115389607593394186/oDV94MoByLXxoAcuZM9TcMUTkaoMOpgtHoSWZrZbULMzrKOgXZ4arag1MArq6ugldXXD', content='Test from python')
response = webhook.execute()
print(response)
print()