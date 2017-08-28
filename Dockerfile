FROM python:3.6
WORKDIR /ablator
COPY ./ablator/requirements.txt /ablator/
RUN pip install -r requirements.txt
COPY ./ablator/ /ablator/

ENV PORT=8000
EXPOSE 8000
RUN python manage.py collectstatic --noinput --clear
CMD python manage.py migrate && gunicorn -w 4 ablator.wsgi --access-logfile - --error-logfile -
