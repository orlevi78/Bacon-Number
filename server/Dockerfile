FROM python:alpine
WORKDIR /server
COPY bacon_number ./bacon_number
COPY server.py .
# Feels a bit smelly to run pip install here, but fine for now.
RUN pip install pandas
RUN pip install flask
RUN pip install flask_cors
# RUN pip install -e bacon_number
CMD python -m bacon_number && python server.py