from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Tuple
from typing import Union


class K3sConfig(ABC):
    def __init__(
        self, history_configs: Dict[Tuple[str, Union[str, None]], Dict[str, str]], current_config: Dict[str, str]
    ):
        self.history_configs = history_configs
        self.current_config = current_config

    @abstractmethod
    def apply(self):
        pass


class DSMConfig(K3sConfig):
    def __init__(self):
        history_configs = {
            ("4.0.0", "4.1.0"): {"setting1": "dsm_value1", "setting2": "dsm_value2"},
        }
        current_config = {"setting1": "dsm_value1", "setting2": "dsm_value2"}
        super().__init__(history_configs, current_config)

    def apply(self):
        # Implementation for DSM apply method
        pass


class CockpitConfig(K3sConfig):
    def __init__(self):
        history_configs = {("1.0.0", None): {"setting1": "cockpit_value1", "setting2": "cockpit_value2"}}
        current_config = {"setting1": "cockpit_value1", "setting2": "cockpit_value2"}
        super().__init__(history_configs, current_config)

    def apply(self):
        # Implementation for Cockpit apply method
        pass


class SmartIQConfig(K3sConfig):
    def __init__(self):
        history_configs = {("1.0.0", None): {"setting1": "smartiq_value1", "setting2": "smartiq_value2"}}
        current_config = {"setting1": "smartiq_value1", "setting2": "smartiq_value2"}
        super().__init__(history_configs, current_config)

    def apply(self):
        # Implementation for SmartIQ apply method
        pass
