import httpx
from app.core.config import settings
import os
from supabase import create_client, Client
# SUPABASE_URL = settings.SUPABASE_URL
# SUPABASE_SERVICE_KEY = settings.SUPABASE_SERVICE_KEY
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_KEY: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
async def supabase_signup(email, password):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{SUPABASE_URL}/auth/v1/signup",
            headers={"apikey": SUPABASE_SERVICE_KEY},
            json={"email": email, "password": password}
        )
        r.raise_for_status()
        return r.json()

async def supabase_login(email, password):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
            headers={"apikey": SUPABASE_SERVICE_KEY},
            json={"email": email, "password": password}
        )
        r.raise_for_status()
        return r.json()

async def supabase_get_user(jwt):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{SUPABASE_URL}/auth/v1/user",
            headers={"Authorization": f"Bearer {jwt}"}
        )
        r.raise_for_status()
        return r.json()
