from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


class Var:
    API_HASH = getenv("API_HASH", "4599e8f16f52517e608b719fa4665467")
    API_ID = int(getenv("API_ID", "16436100"))
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/9f8e73d387f25b7f27ce5.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Saya AyiinUbot Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "5680740751:AAEyL7-IFs2xpemSNL6Y7-WWHzumibmKOns")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    LOG_CHAT = int(getenv("LOG_CHAT", "-1001811634958")
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://userby:userby@cluster0.e6t8egn.mongodb.net/?retryWrites=true&w=majority")
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "BQAhIHQALBbP8f56NDXoJZNjOd1S4p0MAg3hwSf6O4QyQQWnlsxVLqgPZRQsbmahlD1vgsNMMzYu-moLdIKCDQWLkBHStxsdvMn7ZmTZcjhv0p4ATo-mmDN_89fJR0ipNYp5-wTFazMB-NcWWFlNukjgSWIuRXQ7gTI5AlDcyjIMq1bc05iyfu6dUfW1MKNXkPuPeBEYVTdCarfVBrpSgNFYI7vLIbLVc2Ha-ui-Fv3WZVTWKnWw3hGsyGHTMRruWeSPwmLh21ieKQo12zAh8OOLgy1XXz2iJv5xAJXb0nuGQwJosVhsaTZRob6si53x5mCOAXIzi4icb-5JuRYnwRJVfdLQ8AAAAAAwSxg3AA")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
