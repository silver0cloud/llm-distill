import torch
import torch.nn.utils.rnn.pad_sequence
import typing 
import dataclasses 
from dataclasses import Dataset
"""
Function / class	Purpose
pad_to_multiple(length: int, m: int = 8) -> int	Round up the batch length for GPU efficiency.
_pad_1d(seqs, pad_value, length) -> Tensor	Right-pad a list of 1-D tensors to [B, T].
_pad_topk(tensors, length, K, pad_value) -> Tensor	Right-pad a list of [t_i, K] tensors to [B, T, K].
class CaptureCollator	__call__(batch) -> {"input_ids", "attention_mask", "sample_ids"}.
class DistillCollator	__call__(batch) -> {"input_ids", "attention_mask", "labels", "teacher_indices",
"teacher_logprobs", "distill_mask"}. labels is -100 at padding and prompt-masked positions. distill_mask is False at padding, 
masked prompt tokens, and the last real position of each sample.

"""
def pad_to_multiple(length: int, m: int = 8) -> int:


def _pad_1d(seqs, pad_value, length) -> Tensor:


def _pad_topk(tensors, length, K, pad_value) -> Tensor:


class CaptureCollator(Dataset):
  def __call__(batch):

class DistillCollator(Dataset):
  def __call__(batch):
    
