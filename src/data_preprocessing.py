import pandas as pd


def load_data(file_path):
    data = pd.read_excel(file_path)
    return data


def clean_data(data):
    data = data.dropna()
    return data


if __name__ == "__main__":
    print("Data preprocessing module is ready.")