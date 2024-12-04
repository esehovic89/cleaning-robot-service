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

## Code structure

- **src** - Application source code.
  - **api** - Contains communication with outside world. This layer does not have any business logic and entrypoint to the service.
  - **application** - Contains different services that are needed for orchestration of business logic.
  - **common** - Contains code that will be share in the service. For example Logger 
  - **domain** - Contains business logic and models. For examples use case to orchestration business logic by interacting with different domain models, application services and infrastructure. 
  - **infrastructure** - Contains communication with internal services for this service. For example DB repositories.
- **tests** - All tests related to application source code.

## Pre requisites

Install `docker` and `docker compose` on your local machine.

Virtualenv

You can install venv to your host Python by running this command in your terminal:

````
pip install virtualenv
````

Create Virtualenv

To use venv in your project, in your terminal, cd to the project folder in your terminal, and run the following command:
`python<version> -m venv <virtual-environment-name>`

For example:
````
 cd cleaning-robot-service
 python3.10 -m venv .venv
````

Activate Virtualenv

On a mac, to activate your virtual environment, run the code below:
````
source .venv/bin/activate
````
On Widows, to activate your virtual environment, run the code below:
````
 .venv/Scripts/activate.bat //In CMD
 .venv/Scripts/Activate.ps1 //In Powershel
````

Install dev-requirements `pip install -r requirements-dev.txt`
Install pre-commit `pre-commit install`

**Note**: Please make sure this is done right after cloning the repository. The project was build using python 3.10

## How to run locally

```bash
docker compose up
````

Open `http://127.0.0.1:5000/docs` to see OpenAPI spec of the service.

To generate test data:
- Open python inside of project 
- Import `from tests.factory.clean_command_factory import CleanCommandFactory`
- Generate test data by running and copy the output to OpenAPI spec:
  - `CleanCommandFactory().build().model_dump_json()`

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

If you are having issues with the command try running these steps:
- Make sure the `venv` is activated
- `pip-compile --allow-unsafe --no-emit-index-url requirements.in`
- `pip-compile --allow-unsafe --no-emit-index-url requirements-dev.in`