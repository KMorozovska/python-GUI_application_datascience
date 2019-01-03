import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "sources")

DATA_PATH = os.path.join(data_dir, "paragony_ms.csv")
