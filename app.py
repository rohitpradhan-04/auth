from fastapi import FastAPI

from common.routes.service import route as service_route
from common.routes.user import route as user_route

app = FastAPI()


@app.get('/health')
def health():
    return {'status': 'ok'}


app.include_router(user_route)
app.include_router(service_route)
