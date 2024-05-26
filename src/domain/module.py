from punq import Container

from domain.company.command.delete_company.command import DeleteCompanyCommand
from domain.company.command.delete_company.handler import DeleteCompanyCommandHandler
from domain.company.command.save_company.command import SaveCompanyCommand
from domain.company.command.save_company.handler import SaveCompanyCommandHandler
from domain.company.repository.interface import ICompanyRepository
from domain.company.repository.repository import CompanyRepository
from domain.order.command.delete_order.command import DeleteOrderCommand
from domain.order.command.delete_order.handler import DeleteOrderCommandHandler
from domain.order.command.save_order.command import SaveOrderCommand
from domain.order.command.save_order.handler import SaveOrderCommandHandler
from domain.order.repository.interface import IOrderRepository
from domain.order.repository.repository import OrderRepository
from shared.database.sqlalchemy.connection.interface import IAsyncSQLAlchemyConnection
from shared.message_bus.command_bus.interface.bus import ICommandBus
from shared.module_setup.module import IModule


class DomainModule(IModule):

    def configure(
        self,
        container: Container,
    ) -> None:
        self._configure_dependencies(
            container=container,
        )
        self._register_commands(
            container=container,
        )

    @staticmethod
    def _configure_dependencies(container: Container) -> None:
        container.register(
            IOrderRepository,
            instance=OrderRepository(
                async_connection=container.resolve(IAsyncSQLAlchemyConnection)
            )
        )
        container.register(
            ICompanyRepository,
            instance=CompanyRepository(
                async_connection=container.resolve(IAsyncSQLAlchemyConnection)
            ),
        )

    @staticmethod
    def _register_commands(container: Container) -> None:
        command_bus: ICommandBus = container.resolve(ICommandBus)

        command_bus.register(
            message=DeleteOrderCommand,
            handler=DeleteOrderCommandHandler(
                order_repository=container.resolve(IOrderRepository),
            ),
        )
        command_bus.register(
            message=SaveOrderCommand,
            handler=SaveOrderCommandHandler(
                order_repository=container.resolve(IOrderRepository),
                company_repository=container.resolve(ICompanyRepository),
            ),
        )
        command_bus.register(
            message=DeleteCompanyCommand,
            handler=DeleteCompanyCommandHandler(
                company_repository=container.resolve(ICompanyRepository),
            ),
        )
        command_bus.register(
            message=SaveCompanyCommand,
            handler=SaveCompanyCommandHandler(
                company_repository=container.resolve(ICompanyRepository),
            ),
        )

