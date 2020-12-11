FROM python:alpine
COPY . /app/veamer_search
WORKDIR /app/veamer_search
RUN pip install -r requirements.txt 
 
ENV OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider

EXPOSE 5001

CMD opentelemetry-instrument python3 tracer.py