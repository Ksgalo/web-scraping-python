FROM python:3.9-alpine
ADD main.py .
COPY prod.txt qa.txt prodlog.txt qalog.txt /var/
VOLUME v1/:/var/
RUN pip3 install requests beautifulsoup4
CMD [ "python", "./main.py" ]
