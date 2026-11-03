import torch 
import numpy as np
import os 
import logging 
import random

def set_seed(seed: int) -> None:
  random.seed(seed)
  np.random.seed(seed)

  torch.manual_seed(seed)
  torch.cuda.manual_seed(seed)
  torch.cuda.manual_seed_all(seed)

  torch.backends.cudnn.deterministic = True
  torch.backends.cudnn.benchmark = False

def get_logger(name: str) -> logging.Logger:
  logger = logging.getLogging(name)
  logger.setLevel(level)


def get_dtype(name: str) -> torch.dtype:


def ensure_dir(path) -> Path:

  

