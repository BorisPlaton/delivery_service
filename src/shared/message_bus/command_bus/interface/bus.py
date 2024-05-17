from abc import ABC

from shared.message_bus.interface.bus import IMessageBus


class ICommandBus(
    IMessageBus,
    ABC,
):
    pass
