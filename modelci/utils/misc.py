import collections
import logging
import re


def json_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = json_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def remove_dict_null(d: dict):
    """Remove `None` value in dictionary."""
    return {k: v for k, v in d.items() if v is not None}


def get_device(device: str):
    """Get device (cuda and device order) from device name string.

    Args:
        device: Device name string.

    Returns:
        Tuple[bool, Optional[int]]: A tuple containing flag for CUDA device and CUDA device order. If the CUDA device
            flag is `False`, the CUDA device order is `None`.
    """
    # obtain device
    device_num = None
    if device == 'cpu':
        cuda = False
    else:
        # match something like cuda, cuda:0, cuda:1
        matched = re.match(r'^cuda(?::([0-9]+))?$', device)
        if matched is None:  # load with CPU
            logging.warning('Wrong device specification, using `cpu`.')
            cuda = False
        else:  # load with CUDA
            cuda = True
            device_num = int(matched.groups()[0])
            if device_num is None:
                device_num = 0

    return cuda, device_num
