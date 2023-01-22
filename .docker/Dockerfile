FROM python=3.8.6
WORKDIR /app
COPY Pipfile Pipfile.lock ./

RUN pip install requirements.txt
RUN pipenv install --system

COPY . .

EXPOSE 8000

CMD = ['python', 'manage.py', 'runserver', "0.0.0.0:8000"]