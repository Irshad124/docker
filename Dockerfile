FROM ubuntu 

RUN apt update -y &&\
    apt install -y python3 python3-pip

COPY . .

RUN pip3 install -r requirements.txt --break-system-packages

ENTRYPOINT [ "uvicorn","main:app","--reload" ]