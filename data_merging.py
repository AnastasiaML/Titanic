import pandas as pd

dataset_paths = ['dataset\original\train.csv', 'dataset\original\test.csv']

datasets = []
for path in dataset_paths:
  datasets.append(pd.read_csv(path))

merged_dataset = pd.concat(datasets)
merged_dataset.reset_index(inplace = True, drop = True)

merged_dataset.to_csv('dataset\merged\merged.csv', index=False)