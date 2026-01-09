import asyncio
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN, LOG_LEVEL, ADMIN_IDS
from database import engine, Base
from app.handlers import user, admin, admin_users, deepseek, referral, balance, flyers, image_generation, huggingface
from app.middlewares import throttling, acl, subscription
from app.utils.states import AdminStates, UserStates

# Configure logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper()))
logger = logging.getLogger(__name__)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    logger.info(f"BOT_TOKEN loaded: {'Yes' if BOT_TOKEN else 'No'}")
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN is not set")
        return

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Create database tables
    await create_tables()

    # Register middlewares
    dp.message.middleware.register(throttling.ThrottlingMiddleware())
    dp.callback_query.middleware.register(throttling.ThrottlingMiddleware())
    dp.message.middleware.register(acl.ACLMiddleware())
    dp.message.middleware.register(subscription.FlyerAPIMiddleware())
    dp.callback_query.middleware.register(subscription.FlyerAPIMiddleware())

    # Register handlers
    dp.include_router(user.router)
    dp.include_router(admin.router)
    dp.include_router(admin_users.router)
    dp.include_router(deepseek.router)
    dp.include_router(huggingface.router)
    dp.include_router(image_generation.router)
    dp.include_router(referral.router)
    dp.include_router(balance.router)
    dp.include_router(flyers.router)

    # Start polling
    logger.info("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())