from app.database.models import async_session, User, Admin
from sqlalchemy import select



async def get_admins():
    async with async_session() as session:
        return await session.execute(select(Admin))


async def add_new_user(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User.tg_id).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id = tg_id, username = username))
            await session.commit()


async def get_usernames():
    async with async_session() as session:
        result = await session.execute(select(User.username))
        usernames = result.scalars().all()

        beautiful_answer = ''
        beautiful_answer = '\n'.join(usernames)

        return beautiful_answer
