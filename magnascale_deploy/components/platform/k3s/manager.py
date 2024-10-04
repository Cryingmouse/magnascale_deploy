from typing import List

from typing_extensions import Literal

from magnascale_deploy.components.platform.k3s.config import CockpitConfig
from magnascale_deploy.components.platform.k3s.config import DSMConfig
from magnascale_deploy.components.platform.k3s.config import K3sConfig
from magnascale_deploy.components.platform.k3s.config import SmartIQConfig


class K3sManager:
    def __init__(self, config: K3sConfig):
        self.config = config

    def install(self):
        print(f"Installing K3s service with the current version {self.config.current_config}")

    def upgrade(self):
        print(f"Upgrading K3s service with the current version {self.config.current_config}")


def create_k3s_manager(code_name: Literal["dsm", "smartiq", "cockpit"]) -> K3sManager:
    configs = {
        "dsm": DSMConfig(),
        "smartiq": SmartIQConfig(),
        "cockpit": CockpitConfig(),
    }
    if code_name not in configs:
        raise ValueError(f"Unknown code name: {code_name} when deploying k3s service.")

    return K3sManager(configs[code_name])
