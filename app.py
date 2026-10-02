from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Synapse", version="0.1.0")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <body style="background:#0f172a;color:white;display:flex;justify-content:center;align-items:center;height:100vh;font-family:system-ui">
        <div style="text-align:center">
            <h1>🧠 Synapse</h1>
            <p>Your AI Second Brain is online.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)