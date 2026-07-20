from fastapi import FastAPI
from common.routes.user import route as UserRoute
from common.routes.service import route as ServiceRoute

app = FastAPI()


@app.get("/health")
def Health():
    return {"status": "ok"}


app.include_router(UserRoute)
app.include_router(ServiceRoute)
