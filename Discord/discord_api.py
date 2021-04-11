import os
from discord_webhook import DiscordWebhook, DiscordEmbed

class Discord:

    def __init__(self):
        DISCORD_WEBHOOK_URL = os.environ['DISCORD_WEBHOOK_URL']
        self.webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)

    def send_embedded_message(self, title='', description='', color='03b2f8'):

        embed = DiscordEmbed(title=title, description=description, color=color)

        # add embed object to webhook
        self.webhook.add_embed(embed)

        response=""
        try:
            response = self.webhook.execute()
        except Exception as e:
            return False, e, response

        return True

    def send_message(self, message=""):

        self.webhook.set_content(message)

        response = ""
        try:
            response = self.webhook.execute()
        except Exception as e:
            return False, e, response

        return True
