FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest

WORKDIR /app

COPY . .

RUN pip install pytest==9.0.3 pytz==2026.3.post1 pandas==3.0.5 python-dateutil==2.9.0.post0 duckdb==1.5.5

RUN pip install -e .

CMD ["/bin/bash"]
