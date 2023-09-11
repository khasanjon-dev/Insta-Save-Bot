from sqlalchemy import select, update, func

from utils.db_api.db.session import get_session
from utils.db_api.models import Users


class DataBase:
    @staticmethod
    async def create_or_update(data: dict):
        async with get_session() as session:
            telegram_id = data['telegram_id']
            query = select(Users).where(Users.telegram_id == telegram_id)
            user = await session.scalar(query)
            if user:
                query = update(Users).where(Users.telegram_id == telegram_id).values(data)
                await session.execute(query)
            else:
                user = Users(**data)
                session.add(user)
            return user

    @staticmethod
    async def count_users():
        async with get_session() as session:
            query = select(func.count()).select_from(Users)
            count = await session.scalar(query)
            return count

    @staticmethod
    async def update_language(data: dict):
        async with get_session() as session:
            telegram_id = data['telegram_id']
            query = update(Users).where(Users.telegram_id == telegram_id).values(data).execution_options(
                synchronize_session="fetch")
            await session.execute(query)


db = DataBase()
