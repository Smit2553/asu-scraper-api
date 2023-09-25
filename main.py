from fastapi import FastAPI
import src.schedule_scraper as schedule_scraper
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/schedule")
async def get_schedule(subject: str, course_number: int, term: int):
    schedule = await schedule_scraper.parse_classes(subject, course_number, term)
    if not schedule:
        return {"error": "No classes found"}
    return schedule


if __name__ == "__main__":
    uvicorn.run(
        "test:app",
        host="0.0.0.0",
        reload=False,
        port=8002
    )
