import yaml 
from Typing import Optional, List
from pathlib import Path
from dataclasses import dataclass, field
"""
I have to make all of these functions
"""
@dataclass 
class Config:
  def load_capture_config(path) -> CaptureConfig:



  def load_train_config(path) -> TrainConfig:



  def validate_compat(cap: CaptureConfig, train: TrainConfig) -> None:



  def _build(cls, d: dict):


    




