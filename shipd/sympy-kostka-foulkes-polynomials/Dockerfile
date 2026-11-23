FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app
RUN python3 -m pip install --no-cache-dir mpmath==1.3.0 pytest==8.3.5 hypothesis==6.168.1
CMD ["/bin/bash"]
