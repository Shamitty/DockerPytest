# Python-MachineBook

## Prerequisites

1. Install a code editor of your choice VSCode or Pycharm

```
https://code.visualstudio.com/download
```

2. Next we need to download Python and Pip

```
Python download: https://www.python.org/downloads/ 
py -m ensurepip --upgrade
```

## Steps to Run your First Test

Step 1. Clone the MachineBook Selenium Repository.

```
git clone https://github.com/Shamitty/DockerPytest.git
```

Step 2. Install required packages.

```
pip install -r requirements.txt
```

Step 4. Running tests via docker, docker-compose, or command line

##### Running with docker-compose

```
docker-compose -f docker-compose.test.yml run --rm machinebook_regression
```