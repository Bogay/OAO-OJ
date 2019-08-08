# OAO-OJ Backend

## Requirements

- Python3.6
- Flask
- gunicorn (Optional)
- flask-cors

## Run

### Linux/Mac

`gunicorn -b 0.0.0.0:8000 server:app`

or

`python3 -c "__import__('server').app.run(host='0.0.0.0', port='8000')"`

### Windows

`python -c "__import__('server').app.run(host='0.0.0.0', port='8000')"`
