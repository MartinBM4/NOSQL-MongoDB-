# MongoDB dataset:
- Restaurants dataset:
https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json save to a file named primer-dataset.json

- Spatial restaurants dataset:
https://raw.githubusercontent.com/mongodb/docs-assets/geospatial/restaurants.json

- Spatial neighborhoods dataset:
https://raw.githubusercontent.com/mongodb/docs-assets/geospatial/neighborhoods.json

- Import data into the collection (Terminal).
```diff
  mongoimport --db test --collection restaurants --drop --file primer-dataset.json
```
