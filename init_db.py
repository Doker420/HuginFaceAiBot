import asyncio
from database import engine, Base
from app.models import User, Flyer
from config import ADMIN_IDS

async def init_database():
    """Initialize database with sample data"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create sample flyers
    sample_flyers = [
        {
            "title": "Бесплатный гид по DeepSeek",
            "description": "Полное руководство по использованию ИИ DeepSeek для решения различных задач. Узнайте все возможности и секреты эффективной работы с AI.",
            "category": "Образование",
            "flyer_type": "regular",
            "price": 0,
            "created_by": int(ADMIN_IDS[0]) if ADMIN_IDS else 123456789
        },
        {
            "title": "Премиум консультация",
            "description": "Персональная консультация по настройке и оптимизации использования DeepSeek API. Профессиональные рекомендации от эксперта.",
            "category": "Консультации",
            "flyer_type": "admin_config",
            "price": 50,
            "created_by": int(ADMIN_IDS[0]) if ADMIN_IDS else 123456789
        },
        {
            "title": "Шаблоны промптов",
            "description": "Коллекция проверенных шаблонов промптов для различных задач: написание текстов, анализ данных, генерация идей и многое другое.",
            "category": "Инструменты",
            "flyer_type": "regular",
            "price": 25,
            "created_by": int(ADMIN_IDS[0]) if ADMIN_IDS else 123456789
        },
        {
            "title": "VIP поддержка",
            "description": "Приоритетная техническая поддержка и доступ к эксклюзивным функциям бота. Быстрое решение любых вопросов 24/7.",
            "category": "Поддержка",
            "flyer_type": "admin_config",
            "price": 100,
            "created_by": int(ADMIN_IDS[0]) if ADMIN_IDS else 123456789
        }
    ]

    async with engine.begin() as conn:
        for flyer_data in sample_flyers:
            flyer = Flyer(**flyer_data)
            await conn.execute(
                flyer.__table__.insert().values(**flyer_data)
            )

    print("✅ База данных инициализирована с примерными данными!")
    print("📄 Создано флаеров:", len(sample_flyers))
    print("   - Обычные флаеры:", len([f for f in sample_flyers if f["flyer_type"] == "regular"]))
    print("   - Настраиваемые флаеры:", len([f for f in sample_flyers if f["flyer_type"] == "admin_config"]))

if __name__ == "__main__":
    asyncio.run(init_database())