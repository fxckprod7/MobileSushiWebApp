import os

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

            return result
        
    async def menu_item(self, name: str) -> list:
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT * FROM menu WHERE item_name =?", (name,))
            result = await cursor.fetchone()
            
            return result
    