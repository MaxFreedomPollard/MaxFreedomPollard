FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app
RUN uv pip install --system gitdb==4.0.12 smmap==5.0.3 pytest==8.3.5 pytest-cov==6.0.0 typing-extensions==4.12.2 ddt==1.7.2 pytest-mock==3.14.0
CMD ["/bin/bash"]
