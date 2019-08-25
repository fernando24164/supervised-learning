from argparse import Namespace
import numpy as np
import pandas as pd

args = Namespace(
    seed=1234,
    data_file="../data/sample_data.csv",
    num_samples=100,
)

np.random.seed(args.seed)


def generate_data(num_samples):
    X = np.array(range(num_samples))
    random_noise = np.random.uniform(-10, 11, num_samples)
    y = 3.65*X + 10 + random_noise
    return X, y


def save_data():
    X, y = generate_data(args.num_samples)
    data = np.vstack([X, y]).T
    df = pd.DataFrame(data, columns=["X", "y"])
    df.to_csv(args.data_file, index=None, header=True)


save_data()
