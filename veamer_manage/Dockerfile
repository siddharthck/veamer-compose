FROM python:alpine
COPY . /app/veamer_manage
WORKDIR /app/veamer_manage
RUN pip install -r requirements.txt 
 
ENV OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider

EXPOSE 5000

CMD opentelemetry-instrument python3 tracer.py