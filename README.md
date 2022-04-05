# Random Object Generator

A Web app to generate four (4) types of printable random objects and store
them in a single file, each object will be separated by a ",". These are the 4 objects:
alphabetical strings, real numbers, integers, alphanumerics.
```
hisadfnnasd, 126263, assfdgsga12348fas, 13123.123,
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122,
nmarcysfa900jkifh, 3.781, 2.11, ....
```

The output should be 2MB in size. And show the total count of generated objects.

## Getting Started

### Setup Process
> ❗Make sure You have python3 and pip installed on your machine.
- Python 3.8 or higher
- Django
- Docker  -> [Docker install process](https://docs.docker.com/engine/install/ubuntu/)

### Project setup

```sh
# clone the repo
$ git clone https://github.com/rakibulislam01/omni-obj-generator.git

# move to the project folder
$ cd omni-obj-generator
```
## Running the Docker Container

We set up Docker to run this project. Now we will run Protest with Docker.
Build and run docker image using docker compose.

```sh
$ docker-compose up --build
```

## Running Test
```sh
$ docker container exec -it omni-obj-generator_app_1 sh
$ python -m pytest

```
### Home page
Here you will find the UI of the object generator application in this URL.

    http://127.0.0.1/

## API End Points

### To Generate random object:

```sh
GET /api/generate-obj/
```

**Sample output:**

```json
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "file_link": "http://127.0.0.1/media/data/objects.txt"
    }
```

### To generate report:

```sh
 GET /api/report/
```
**Sample output:**
    
```json
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    {
        "integers": 0,
        "alphanumerics": 0,
        "string": 0,
        "real_number": 0
    }
```