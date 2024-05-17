from punq import Container

from settings.config import ApplicationSettings
from settings.config import DatabaseSettings
from shared.module_setup.module import IModule


class SettingsModule(IModule):

    def configure(
        self,
        container: Container,
    ) -> None:
        container.register(
            DatabaseSettings,
            instance=DatabaseSettings(),
        )
        container.register(
            ApplicationSettings,
            instance=ApplicationSettings(),
        )
