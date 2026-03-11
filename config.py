# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv
load_dotenv()

# ════════════════════════════════════════════════════════════════════════════════
# ░ CONFIGURATION SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# ─── BOT / DATABASE CONFIG ──────────────────────────────────────────────────────
API_ID       = os.getenv("API_ID", "29057526")
API_HASH     = os.getenv("API_HASH", "92cb1f82af717e97a2ad7e1670c35b21")
BOT_TOKEN    = os.getenv("BOT_TOKEN", "")
MONGO_DB     = os.getenv("MONGO_DB", "mongodb+srv://rupakaryanaryan_db_user:Ty55JMgP55isDNW9@cluster0.05xkjx2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
")
DB_NAME      = os.getenv("DB_NAME", "rupakaryanaryan_db_user")

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_ID     = list(map(int, os.getenv("OWNER_ID", "7338678521").split()))  # space-separated list
STRING       = os.getenv("BQG7YfYAdzOGJzQqHSZEN8d0C66WtzL--r0FVoIf4ZIr5sJUexX5ekEcSBw5WdbqntOqRJf6d5b1SdCuaajLv2CRU5Dv49W56eI-_2lG8uxHW82TC1PE9_IKAjXK16NbR7ToculkDU6KwIrpCqUuLOIvWxYteZWmzHCXXjj0HHk1a33XQ00mx92Ajh0sG03xmpI9bLejjfX3CdFpjpzYNAFbSDXfSMAuujZABiwTtDy9TE_yOeK0mMnQW2PorSJmoeFLtSkC0B3xIKzMfy3UYMMpt7Sd2oJ6rJMh23MQYxXRdhdhCTnPSkge_BaGkgjVUeGuv1HahGIbO9QU-jZrhTtrqQcofgAAAAG1a1j5AA", None)  # optional session string
LOG_GROUP    = int(os.getenv("LOG_GROUP", "0"))
FORCE_SUB    = int(os.getenv("FORCE_SUB", "0"))

# ─── SECURITY KEYS ──────────────────────────────────────────────────────────────
MASTER_KEY   = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")  # session encryption
IV_KEY       = os.getenv("IV_KEY", "s7Yx5CpVmE3F")  # decryption key

# ─── COOKIES HANDLING ───────────────────────────────────────────────────────────
YT_COOKIES   = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# ─── USAGE LIMITS ───────────────────────────────────────────────────────────────
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "9999999"))
PREMIUM_LIMIT  = int(os.getenv("PREMIUM_LIMIT", "9999999"))

# ─── UI / LINKS ─────────────────────────────────────────────────────────────────
JOIN_LINK     = os.getenv("JOIN_LINK", "")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "@Extrac_txt_bot")

# ════════════════════════════════════════════════════════════════════════════════
# ░ PREMIUM PLANS CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

P0 = {
    "d": {
        "s": int(os.getenv("PLAN_D_S", 1)),
        "du": int(os.getenv("PLAN_D_DU", 1)),
        "u": os.getenv("PLAN_D_U", "days"),
        "l": os.getenv("PLAN_D_L", "Daily"),
    },
    "w": {
        "s": int(os.getenv("PLAN_W_S", 3)),
        "du": int(os.getenv("PLAN_W_DU", 1)),
        "u": os.getenv("PLAN_W_U", "weeks"),
        "l": os.getenv("PLAN_W_L", "Weekly"),
    },
    "m": {
        "s": int(os.getenv("PLAN_M_S", 5)),
        "du": int(os.getenv("PLAN_M_DU", 1)),
        "u": os.getenv("PLAN_M_U", "month"),
        "l": os.getenv("PLAN_M_L", "Monthly"),
    },
}

# ════════════════════════════════════════════════════════════════════════════════
# ░ DEVGAGAN
# ════════════════════════════════════════════════════════════════════════════════










