def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_config(config_file):
    """Loads configuration from a given file."""
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def save_model(model, filepath):
    """Saves the trained model to a specified filepath."""
    import joblib
    joblib.dump(model, filepath)

def load_model(filepath):
    """Loads a model from a specified filepath."""
    import joblib
    return joblib.load(filepath)