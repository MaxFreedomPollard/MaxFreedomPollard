FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# SCons scripts import the installed package. Install this checkout editably
# so agent edits in /app take effect in the shell and test runner. The project
# has no runtime dependencies, and pytest is pinned for its existing suite.
RUN python3 -m pip install --no-cache-dir pytest==8.3.5 -e .
CMD ["/bin/bash"]
