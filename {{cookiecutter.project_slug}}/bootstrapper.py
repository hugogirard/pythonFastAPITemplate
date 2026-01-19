from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan_event(app: FastAPI):

    # Add all dependencies here the be injected
    # app.state.service = Service() for example

    yield

class Bootstrapper:

    def run(self) -> FastAPI:

        app = FastAPI(lifespan=lifespan_event)

        self._configure_monitoring(app)

        return app        

    def _configure_monitoring(self, app: FastAPI):
        pass        