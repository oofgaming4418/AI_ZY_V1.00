# File: /python-ai-app/python-ai-app/src/main.py

import sys
from src.models.model import Model
from src.data.dataset import Dataset
from src.pipelines.train import run_training

def main():
    # Initialize the dataset
    dataset = Dataset()
    data = dataset.load_data()
    preprocessed_data = dataset.preprocess(data)

    # Initialize the model
    model = Model()

    # Run the training process
    run_training(model, preprocessed_data)

if __name__ == "__main__":
    main()