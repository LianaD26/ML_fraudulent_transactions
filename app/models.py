import pickle

def load_model(path: str):
    with open(path, "rb") as file:
        model = pickle.load(file)
    return model

# cargar el modelo al inicio
model = load_model("app/model/modelo.pkl")