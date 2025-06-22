from fastapi import Header, HTTPException
import httpx
from app.core.config import Settings

settings = Settings()

print(f"✅ Loaded SUPABASE_URL: {settings.SUPABASE_URL}")
print(f"✅ Loaded SUPABASE_SERVICE_KEY: {settings.SUPABASE_SERVICE_KEY[:10]}...")
print(f"✅ Loaded SUPABASE_JWT_SECRET: {settings.SUPABASE_JWT_SECRET[:10]}...")

async def get_current_user(authorization: str = Header(...)):
    try:
        print("🔐 Authorization header received:", authorization)
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            print("❌ Invalid auth scheme:", scheme)
            raise HTTPException(status_code=401, detail="Invalid auth scheme")

        print("🔑 Extracted token:", token[:10], "...")

        async with httpx.AsyncClient() as client:
            supabase_url = f"{settings.SUPABASE_URL}/auth/v1/user"
            print(f"🌐 Calling Supabase URL: {supabase_url}")
            r = await client.get(
                supabase_url,
                headers={
            "Authorization": f"Bearer {token}",
            "apikey": settings.SUPABASE_SERVICE_KEY  # or your anon/public key
        }
            )

        print("🌐 Supabase response status:", r.status_code)
        print("🌐 Supabase response body:", r.text)

        if r.status_code != 200:
            # Return Supabase's error details if available
            try:
                error_detail = r.json()
            except Exception:
                error_detail = r.text
            print("❌ Supabase error detail:", error_detail)
            raise HTTPException(status_code=401, detail=f"Invalid or expired token: {error_detail}")

        user_data = r.json()
        print("✅ Supabase user data loaded:", user_data)
        return user_data

    except httpx.RequestError as re:
        print("❌ HTTPX Request error:", str(re))
        raise HTTPException(status_code=502, detail=f"Supabase connection error: {str(re)}")
    except HTTPException as he:
        # Already formatted error — re-raise
        raise he
    except Exception as e:
        print("❌ Unexpected auth error:", str(e))
        raise HTTPException(status_code=500, detail=f"Unexpected internal error: {str(e)}")
