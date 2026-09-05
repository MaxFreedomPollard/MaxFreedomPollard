FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest

WORKDIR /app

COPY . .

RUN pip install pytest==9.0.3

RUN pip install -e .

CMD ["/bin/bash"]
