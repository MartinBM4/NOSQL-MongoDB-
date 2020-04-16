# MongoDB dataset:
- Retrieve the dataset from:
https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json save to a file named primer-dataset.json

- Import data into the collection (Terminal).
```diff
  mongoimport --db test --collection restaurants --drop --file primer-dataset.json
```
