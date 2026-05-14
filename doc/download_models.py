import argparse
import os
import shutil
from pathlib import Path


DEFAULT_MODELSCOPE_REPO_ID = "supersong/onnxocr_model"
DEFAULT_HUGGINGFACE_REPO_ID = "jingsongliu/onnxocr_model"
DEFAULT_MODEL_SUBDIR = "models"