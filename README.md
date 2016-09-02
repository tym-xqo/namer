# namer
Another random adjective-noun name generator; seeks names with punk poetry (<http://namer.ty-m.xyz> to see it in action)

`namer-svc.py` is a Flask app; Dockerfile provides a container to set this up in a gunicorn service running on port 8880.

## API
- `GET` request to `/` returns 1 name as plain text
- There are no other methods or endpoints
