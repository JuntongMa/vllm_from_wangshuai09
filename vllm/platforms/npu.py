from typing import Tuple

import torch

from .interface import Platform, PlatformEnum


class NpuPlatform(Platform):
    _enum = PlatformEnum.NPU

    @staticmethod
    def get_device_capability(device_id: int = 0) -> Tuple[int, int]:
        raise RuntimeError("NPU does not have device capability.")

    @staticmethod
    def inference_mode():
        return torch.no_grad()