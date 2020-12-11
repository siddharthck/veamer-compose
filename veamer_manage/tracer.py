from opentelemetry import trace
from opentelemetry.exporter.jaeger import JaegerSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor
import opentelemetry.instrumentation.requests
#from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware

from opentelemetry.sdk.trace.propagation.b3_format import B3Format

from opentelemetry import propagators

#setting propagators
#propagators.set_global_textmap(B3Format())

# SpanExporter receives the spans and send them to the target location.
exporter = JaegerSpanExporter(
    service_name="Veamer-manage",
    agent_host_name="jaeger",
    agent_port=6831,
)
span_processor = BatchExportSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

#exec(open("./manage.py").read())

import manage
#manage.app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
manage.main()