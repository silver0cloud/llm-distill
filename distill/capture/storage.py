import json
from pathlib import Path
import collections
from collections import OrderedDict
import dataclasses
import torch
import numpy as np
import safetensors
from safetensors.torch import save_file, load_file
from safetensors import safe_open

"""
One of the most important modules.
"""

def topk_from_logits(logits, k, temperature) -> (idx, logprobs):


class ShardWriter(

