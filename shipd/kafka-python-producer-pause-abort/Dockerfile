FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Install pinned runtime, codec, lint, and test dependencies only without running explicit Python build commands such as pip install -e .; ENV PYTHONPATH=/app exposes the live /app source checkout directly for editable development.
RUN pip install --no-cache-dir astroid==4.3.4 coverage==7.17.3 cramjam==2.14.0 crc32c==2.9.post0 dill==0.4.1 flake8==7.5.0 iniconfig==2.3.1 isort==9.0.2 lz4==4.4.5 mccabe==0.7.0 mypy-extensions==1.2.0 packaging==26.3 platformdirs==4.14.6 pluggy==1.7.0 psutil==7.2.2 py==1.11.0 pycodestyle==2.15.0 pyflakes==4.1.0 pygments==2.21.0 pylint==4.1.4 pyperf==2.11.0 pytest==9.2.0 pytest-cov==7.1.0 pytest-mock==3.17.0 pytest-timeout==2.4.0 python-snappy==0.7.3 tomlkit==0.15.2 xxhash==4.1.0 zstandard==0.25.0
ENV PYTHONPATH=/app
# Verify package import from /app without running a build command.
RUN python -c "import kafka; assert kafka.__version__"
CMD ["/bin/bash"]
