import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","29481920"))
API_HASH = getenv("API_HASH","f700ddb0930acfab095b00911a2e6f3a")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN",)

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "CardioMuzicBot")

# Get Your repo
REPO_LINK = getenv("REPO_LINK" , "https://github.com/Nobi-123/NISHA")

# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "Cardio")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://IVANxNISHA:IVANxNISHA@cluster0.pq52raw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002681848382"))

# Get this value from @CrewMusic_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","7694170809"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Nobu-123/NISHA",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botXjarvis")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/JarvisXsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/4ft3kh.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/tbra0o.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/0zhu1b.jpg"
STATS_IMG_URL = "https://files.catbox.moe/fd6a5x.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/kobtju.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ksuz0m.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/futwz1.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/ksuz0m.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/futwz1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/futwz1.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/fd6a5x.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/fd6a5x.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
