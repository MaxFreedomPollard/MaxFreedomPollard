FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# This is a development container for prompt_toolkit itself, so the editable
# install is intentional: the checkout in /app is the code being developed and
# tested, and edits to it must take effect for every import. The package uses a
# src/ layout, so it is not importable without this install. Its only runtime
# dependency, wcwidth, is pinned in the same install, so pip resolves the
# package against that exact version.
RUN python3 -m pip install --no-cache-dir wcwidth==0.9.1 pytest==8.3.5 -e .
CMD ["/bin/bash"]
