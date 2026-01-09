import os
from typing import List

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Admin IDs (comma-separated)
ADMIN_IDS = [int(id.strip()) for id in os.getenv("ADMIN_IDS", "").split(",") if id.strip()]

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bot.db")

# Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# DeepSeek API
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com"
DEEPSEEK_MODELS = ["deepseek-chat", "deepseek-coder"]
MAX_TOKENS_PER_USER = int(os.getenv("MAX_TOKENS_PER_USER", "10000"))
MAX_REQUESTS_PER_DAY = int(os.getenv("MAX_REQUESTS_PER_DAY", "100"))

# Flyer API
FLYER_API_KEY = os.getenv("FLYER_API_KEY")

# Image Generation API (Hugging Face)
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
IMAGE_MODEL = os.getenv("IMAGE_MODEL", "Qwen/Qwen-Image-2512")

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Bot settings
BOT_USERNAME = os.getenv("BOT_USERNAME", "")

# Rate limiting
RATE_LIMIT = 5  # messages per second