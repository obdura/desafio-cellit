# Running our app in a docker container

## Build the docker image

```bash
docker build -t desafio-cellit . 
```
This looks for the `Dockerfile` and it builds our app into a docker image.

## Run the docker image

```bash
docker run -dp 8000:80 desafio-cellit
```
This runs the image into a container. And it binds our Fast-API app running on the port 80 on the container, into the host's port 8000.

## Access the API documentation

In a web browser you can access to the api documentation going to [localhost:8000/docs](localhost:8000/docs).

## Accessing the API
The api contains two entry points:

### `/id/{plate}`

You can get the unique id for a given plate of the form `aaaa000` that ranges to `zzzz999`. It is accessible through the address `localhost:8000/id/{plate}` on a web browser. It can accept lower and upper case written plates, and a combination of both.

### `/plate/{id}`

You can get the unique plate given an id. It maps from the id `1` corresponding to the plate `aaaa000` to the id `456_976_000` corresponding to the plate `zzzz999`. It is accessible through the web address `localhost:8000/plate/{id}`.

# Running local tests

You can run locally the included tests for this app. For that, you have to build a virtual environment. The requirement is that you use **Python 3.10.5** on windows.

On command bash run the following commands to create the virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

This installs the libraries required to run locally the app under the environment. It includes the library `pytest`.

And to run the tests, run the following command:

```bash
pytest app/tests.py
```
