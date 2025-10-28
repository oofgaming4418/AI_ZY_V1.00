def train_model(model, dataset, epochs=10):
    for epoch in range(epochs):
        print(f"Starting epoch {epoch + 1}/{epochs}")
        model.train(dataset)
        print(f"Epoch {epoch + 1} completed.")

def run_training_pipeline():
    from src.models.model import Model
    from src.data.dataset import Dataset

    dataset = Dataset()
    dataset.load_data()
    dataset.preprocess()

    model = Model()
    train_model(model, dataset)

if __name__ == "__main__":
    run_training_pipeline()