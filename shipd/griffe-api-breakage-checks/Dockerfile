FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Isolate the challenge from unrelated package conflicts in the base image.
RUN python -m venv /opt/griffe-venv
ENV PATH="/opt/griffe-venv/bin:$PATH"
# Install pinned distributions and their runtime and test dependencies.
RUN python -m pip install --no-cache-dir \
      pytest==9.0.3 \
      pytest-gitconfig==0.8.0 \
      pytest-cov==7.0.0 \
      colorama==0.4.6 \
      jsonschema==4.26.0 \
      build==1.3.0 \
      hatchling==1.28.0 \
      setuptools==83.0.0 \
      editables==0.5 \
      pdm-backend==2.4.5 \
      uv-dynamic-versioning==0.11.1 \
      mkdocstrings==1.0.1 \
      griffe==2.2.0 griffelib==2.2.0 griffecli==2.2.0 \
      griffe-inherited-docstrings==1.1.1
# Restore the upstream release tag omitted by shallow platform checkouts.
# Commit a345344b40f50f8556ee5d08665880ff9251485f is the 2.2.0 release.
# Git-free exports use the same version from the repository changelog.
RUN if [ -d .git ]; then \
      test "$(git rev-parse HEAD)" = a345344b40f50f8556ee5d08665880ff9251485f || exit 1; \
      git show-ref --verify --quiet refs/tags/2.2.0 || \
        git tag 2.2.0 a345344b40f50f8556ee5d08665880ff9251485f; \
      test "$(git rev-parse '2.2.0^{commit}')" = a345344b40f50f8556ee5d08665880ff9251485f; \
    fi
# Use the repository's workspace configuration to keep edited source live.
# Preserve the pinned test dependencies, excluding optional development groups.
RUN UV_DYNAMIC_VERSIONING_BYPASS=2.2.0 UV_PROJECT_ENVIRONMENT=/opt/griffe-venv \
    uv sync --all-packages --no-default-groups --inexact \
      --no-build-isolation --no-python-downloads \
      --upgrade-package griffe==2.2.0 --upgrade-package griffelib==2.2.0 \
      --upgrade-package griffecli==2.2.0 --upgrade-package colorama==0.4.6
RUN python -c 'from importlib.metadata import version; assert all(version(name) == "2.2.0" for name in ("griffe", "griffelib", "griffecli"))'
RUN python -m pip check
# Library tests: python -m pytest packages/griffelib/tests from /app.
CMD ["/bin/bash"]
