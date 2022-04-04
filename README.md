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

### Prerequisites

- Python 3.8 or higher
- Django
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/rakibulislam01/omni-obj-generator.git

# move to the project folder
$ cd omni-obj-generator
```
## Running the Docker Container

We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the omni-obj-generator app and then start the omni-obj-generator app container.


```sh
$ docker-compose up --build

```

## Functional test
```sh
$ docker container exec -it omni-obj-generator_app_1 sh
$ python -m pytest

```
### Home page
Here you will find the UI of the object generator application.

    http://127.0.0.1/

## API End Point

To Generate random object please run following api endpoint in any api client.

```sh
GET /api/generate-obj/
```

**Sample output:**

    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "file_link": "http://127.0.0.1/media/data/objects.txt"
    }

To get the report of random object please run following api endpoint in any api client.

```sh
 GET /api/report/
```
**Sample output:**
    
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