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
BOT_TOKEN    = os.getenv("BOT_TOKEN", "8241696754:AAFK_xH_EqkIY7C2nfoY1W44XzDbCSRlIK4")
MONGO_DB     = os.getenv("MONGO_DB", "mongodb+srv://rupak:yHjYzKG7q_E@cluster0.cbyim0l.mongodb.net/rupak?retryWrites=true&w=majority")
DB_NAME      = os.getenv("DB_NAME", "rupak")

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_ID     = list(map(int, os.getenv("OWNER_ID", "7338678521").split()))  # space-separated list
STRING       = os.getenv("BQG7YfYACkrE88St9oy7bnddUX9Z_jLRjspZONab4N1yyQZ3iYslZ0MXOZgj5vWg4wF0Cbg5vrSffh_WaN-1iclzAWZmlyQf72DeLgVQNidOXblBzE-b-OuIRcUUbmJlsU-8HWdUu7octkAVOZgF0V8mYzu3ulGBI5Gsdn2C-RrToumVm78lvYR9cTpRovUO2DiyBFPAJj6p-6jT2jvGwSC3pZbgXkBKa_ZpitLlXszQWZqvM8dFKycjV3v8jwFk0Lu35BgLHSI6Za3kxvSUf57AG5ZczHV1I5EisO3qYb3JiL52ud-bfFUdHJIyZikUfFaeNtSMqNhyi840swtmoC8HljallwAAAAG1a1j5AA", None)  # optional session string
LOG_GROUP    = int(os.getenv("LOG_GROUP", "-5112419856"))
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




















