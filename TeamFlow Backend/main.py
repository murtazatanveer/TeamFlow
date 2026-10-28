from fastapi import FastAPI
from contextlib import asynccontextmanager
from Configuration.supabaseClient import getDatabaseEngine, closeDatabaseConnections
 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🗄️  Initializing Supabase PostgreSQL Engine...")
    try:
        engine = getDatabaseEngine() 
        print("   ✅ PostgreSQL Engine ready (Async)")
    except Exception as e:
        print(f"   ❌ PostgreSQL init failed: {type(e).__name__}: {e}")
        raise

    yield

    print("👋 Shutting down...")
    try:
        await closeDatabaseConnections()
        print("   ✅ PostgreSQL connections closed.")
    except Exception as e:
        print(f"   ❌ Error closing PostgreSQL: {e}")

app = FastAPI(lifespan=lifespan)