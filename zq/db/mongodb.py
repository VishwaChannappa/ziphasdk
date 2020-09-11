from motor.motor_asyncio import AsyncIOMotorClient

''' 
file to initiate the db client from motor package for the db connections
'''


class DataBase:
    client: AsyncIOMotorClient = None
db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client