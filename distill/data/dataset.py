"""
what all is to be added in here 
1. loading the HF dataset as set in the capture.yaml
2. format each example - plain data uses text_field.
3. tokenize using the tokenizer - (BOS/EOS?)
4. build a loss mask - "mask_prompt_tokens" should be off
5. max_seq_len function - fitting the length
6. sample_id - assigns each sample "sample_id".
"""
import hashlib
import json
from pathlib import Path
import typing
import torch 
from torch.utils.data import Dataset
from datasets import load_dataset, HFDataset, load_from_disk
import transformers
from transformers import AutoTokenizer
from distill.capture.storage import ManifestReader, ShardReader

def load_raw_dataset(cfg: DatasetCfg) -> HFDataset:
  

class DatasetLoader(Dataset):
  def __init__(self, dataset_name="HuggingFaceH4/ultrachat_200k", split = "train_sft"):
    self.dataset = load_dataset(dataset_name, split=split)

  def __len__(self):
    return len(self.dataset)

  def __getitem__(self, idx):
    item = self.dataset[idx]

    messages = item["messages"]
    return {
      "messages" : messages
    }

if __name__ == "__main__":
    loader = DatasetLoader()
    print("Dataset loaded successfully!")
    print("Running test : ", loader[0])
