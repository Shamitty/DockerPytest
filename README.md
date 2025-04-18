# Python-DockerPytest

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

Step 1. Clone the DockerPytest Selenium Repository.

```
git clone https://github.com/Shamitty/DockerPytest.git
```

Step 2. Install required packages.

```
pip install -r requirements.txt
```

Step 4. Running tests via docker, docker-compose, or command line

#### Running with local vs code 
```
pytest step_defs/test_fglife_landing_page_steps.py --disable-warnings --html=reports/dockerpytest.html -k Regression

Add -v -f for it to run automatically after a change



```

##### Running with docker-compose

```
docker-compose -f docker-compose.test.yml run -e TAGNAME=Regression --rm dockerpytest_regression && docker-compose rm -fsv

TAGNAME="@Regression or @Smoke" docker-compose --no-cache -f docker-compose.yml run --rm dockerpytest_regression && docker-compose rm -fsv
TAGNAME="@Regression or @Smoke" docker-compose --no-cache -f docker-compose.yml run --rm dockerpytest_regression
```