from typing import Awaitable
from typing import Callable

from fastapi import FastAPI
from fastapi import Request
from punq import Container

from domain.company.controller.rest.base import company_router
from domain.company.controller.rest.base import tag as company_tag
from domain.module import DomainModule
from domain.order.controller.rest.base import order_router
from domain.order.controller.rest.base import tag as order_tag
from settings.config import ApplicationSettings
from settings.module import SettingsModule
from shared.exception.base import BaseAppException
from shared.fastapi_.exception.factory import exception_factory
from shared.module import SharedModule
from shared.module_setup.bootstrap import ModulesConfig


def create_app() -> FastAPI:
    """
    Creates an application and configures DI-container.

    @return:
        The initialized FastAPI application.
    """

    modules_config = ModulesConfig(
        container=Container(),
        modules=(
            SettingsModule(),
            SharedModule(),
            DomainModule(),
        ),
    )
    modules_config.setup()

    app = FastAPI(
        debug=modules_config.container.resolve(ApplicationSettings).DEBUG,
        description="The backend application for automation business-process of the delivery company.",
        version="1.0.0",
        openapi_tags=[
            {
                "name": order_tag,
                "description": "Operations with orders. This section has basic CRUD operations for orders.",
            },
            {
                "name": company_tag,
                "description": "Operations with orders. This section has basic CRUD operations for companies.",
            },
        ],
    )
    app.include_router(order_router)
    app.include_router(company_router)

    @app.middleware('http')
    async def set_registry[T](
        request: Request,
        call_next: Callable[[Request], Awaitable[T]],
    ) -> T:
        request.state.registry = modules_config.container
        return await call_next(request)

    @app.exception_handler(BaseAppException)
    def base_app_exception_handler(
        request: Request,
        exc: BaseAppException,
    ) -> None:
        raise exception_factory(exc=exc)

    return app
