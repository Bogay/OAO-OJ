# OAO-OJ Backend

## Requirements

- Python3.6
- Flask
- gunicorn (Optional)
- flask-cors
- pymongo
- mongodb

## Run

### MongoDB

`mongod -f mongod.conf`

### Linux/Mac

`gunicorn -b 0.0.0.0:8000 server:app`

or

`python3 -c "__import__('server').app.run(host='0.0.0.0', port='8000')"`

### Windows

`python -c "__import__('server').app.run(host='0.0.0.0', port='8000')"`

## DB Preset

`use OAO-OJ`
`db.createCollection('problems')`
`db.problems.insertOne({'pid': '0000', 'title': 'Hello, OAO-OJ'})`

## TODO

- [ ] account system
- [ ] support multi-testcase
