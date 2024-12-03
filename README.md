# cleaning-robot-service

Service will simulate a robot moving in an office space and will be cleaning the places this robot visits. The path of the robot's movement is
described by the starting coordinates and move commands. After the cleaning has been done, the robot reports the number of unique places cleaned.
The service will store the results into the database and return the created record in JSON format.


Request Example:
````json
{
    "start": 
    {
        "x": 10,
        "y": 22
    },
    "commmands": 
    [
      {
        "direction": "east",
        "steps": 2
      },
      {
        "direction": "north",
        "steps": 1
      } 
    ]
}
````
Stored record example:

| Id    | Timestamp | Commands | Result |Duration |
| -------- |-----------|----------|--------|-------|
| 1234  | $2018-05-12 12:45:10.851596      | 2        | 4      |0.000123      |

## Pre requisites

Install `docker` and `docker compose` on your local machine.

Run 
````bash
make init
````
**Note**: Please make sure this is done right after cloning the repository.

If you are using Window machine, follow these steps:
- create venv
- activate the venv
- install dev-requirements `pip install -r requirements-dev.txt`
- install pre-commit `pre-commit install`

## Project structure



## How to run locally

```bash
docker compose up
````

Open `http://127.0.0.1:5000/docs` to see OpenAPI spec of the service.

## How to run tests

### Running all tests

````bash
make test
````

### Running specific test

Run 
````
pytest _part_to_the_test_file_
````

**Note:** Make sure to run `docker compose -f docker-compose-local-db.yml up -d` in case test needs DB access.

## How does this project manage dependencies

For local development the project relies on environmental. This is isolated env were your project dependents live. 
If you completed steps from [Pre requisites](#Pre requisites) you only need to activate it:
Run 
````
source .venv/bin/activate
````

## How to add dependencies

Add the dependency to `requirements.in` or `requirement-dev.in` depending on the type of the dependency. 
Next step is to run:
````bash
make compile-dependencies
````