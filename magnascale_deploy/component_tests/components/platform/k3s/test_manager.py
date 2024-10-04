# 使用示例
from magnascale_deploy.components.platform.k3s.manager import create_k3s_manager

dsm_k3s = create_k3s_manager("dsm")
dsm_k3s.install()
dsm_k3s.upgrade()

smartiq_k3s = create_k3s_manager("smartiq")
smartiq_k3s.install()
smartiq_k3s.upgrade()

cockpit_k3s = create_k3s_manager("cockpit")
cockpit_k3s.install()
cockpit_k3s.upgrade()
