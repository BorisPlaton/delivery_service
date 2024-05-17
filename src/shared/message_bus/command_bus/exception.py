from shared.message_bus.interface.exception import MessageBusException


class NoCommandHandlersFound(MessageBusException):

    def __init__(
        self,
        message: str = "No handlers found for the command",
    ) -> None:
        super().__init__(message)
