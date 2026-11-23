FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# This repository (pyfakefs) has no runtime dependencies; install pinned test runner dependencies only and expose /app via PYTHONPATH for editable development without running explicit Python build commands such as pip install -e .
RUN pip install --no-cache-dir iniconfig==2.3.1 packaging==26.3 pluggy==1.7.0 Pygments==2.21.0 pytest==9.1.1
ENV PYTHONPATH=/app
CMD ["/bin/bash"]
