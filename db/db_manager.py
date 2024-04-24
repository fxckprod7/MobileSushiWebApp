import os, asyncio

import aiosqlite


class Database:
    def __init__(self, path: list):
        self.path = str(os.path.join(*path))
        
    async def connection_check(self) -> None:
        async with aiosqlite.connect(self.path) as db:
            print("[INFO] Connection check successful")
    
    async def menu_items(self) -> list:
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT * FROM menu")
            result = await cursor.fetchall()

            await db.close()
            return result
        
    async def menu_item(self, name: str) -> list:
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT * FROM menu WHERE item_name =?", (name,))
            result = await cursor.fetchone()
            
            return result
    
    
async def main():
    db = Database(["database.db"])
    await db.connection_check()
    print(await db.menu_items())
    
if __name__ == "__main__":
    asyncio.run(main())