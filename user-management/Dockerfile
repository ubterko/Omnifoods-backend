FROM python:latest 

COPY . /usr-mgt/ 

WORKDIR /usr-mgt
 
RUN pip install -r requirements.txt 
RUN rm Dockerfile

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]