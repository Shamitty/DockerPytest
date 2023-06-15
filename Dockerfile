FROM python:3
MAINTAINER schmiedtbrian@johndeere.com

COPY . /MachineBookTesting
WORKDIR /MachineBookTesting

RUN pip install --no-cache-dir -r requirements.txt

ENV TAG_NAME tagname

COPY . .

CMD pytest -k ${TAG_NAME}
