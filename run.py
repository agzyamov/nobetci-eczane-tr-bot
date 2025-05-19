import os
import uvicorn

if __name__ == "__main__":
    # Get port from environment variable for Railway compatibility
    port = int(os.environ.get("PORT", 8000))
    
    # Run the FastAPI application
    uvicorn.run(
        "bot.main:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
