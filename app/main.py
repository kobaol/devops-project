from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>DevOps Project</title>
        </head>
        <body>
            <h1>DevOps Project</h1>
            <p>Application is running.</p>
            <ul>
                <li>Docker</li>
                <li>Docker Compose</li>
                <li>GitHub Actions</li>
                <li>PostgreSQL</li>
            </ul>
        </body>
    </html>
    """

