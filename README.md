# emoji-in-the-haystack

Make sure you meet the following prerequisites before running this project:

* Pipenv- version 2018.11.26 (run `pipenv --version` to confirm)
* Elasticsearch - version 5.5.3 (https://www.elastic.co/downloads/past-releases/elasticsearch-5-5-3)

## Run Elasticsearch instance
```
elasticsearch
```

## Start the virtual environmnt
```bash
pipenv shell
```

## Run migrations
```bash
python manage.py migrate
```

## Retrieve emoji data
```bash
python manage.py initemojidata
```

## Index emoji data
```bash
python manage.py rebuild_index
```

## Run the app
```bash
python manage.py runserver
```

<p align="center">
  <img src="https://phaven-prod.s3.amazonaws.com/files/image_part/asset/2471693/51WXfddo30CV6ghSNqXV-7pWnrY/medium_Screen_Shot_2020-06-22_at_11.12.58_PM.png">
</p>
