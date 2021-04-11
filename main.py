import src.news_alert as newsAlert
import Discord.discord_api as discord

discord = discord.Discord()
# res = discord.send_embedded_message(title="Hello World",
#  description="The first message")
# print(res)
newsAlert.startNewsALert("./data/keywords.json")
