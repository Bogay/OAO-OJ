# OAO-OJ Backend

## Requirements

- Python3.6
- Flask
- flask-cors
- gunicorn (optional)

## run with gunicorn

`gunicorn server:app`

## run server without gunicorn

### Linux/Mac
`python3 -c "__import__('server').app.run(port='8000')"`

### Windows
`python -c "__import__('server').app.run(port='8000')"`