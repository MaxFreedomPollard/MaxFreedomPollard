FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# The checkout in /app is the library under development, so the editable install is intentional: every
# edit to it must take effect for the tests. Install pinned runtime, test, linter, and build dependencies.
RUN python3 -m pip install --no-cache-dir \
    babel==2.18.0 \
    coverage==7.16.2 \
    dnspython==2.9.0 \
    editables==0.6 \
    email-validator==2.3.0 \
    hatchling==1.32.4 \
    idna==3.20 \
    iniconfig==2.3.1 \
    MarkupSafe==3.0.4 \
    packaging==26.3 \
    pathspec==1.1.1 \
    pluggy==1.7.0 \
    Pygments==2.21.0 \
    pytest==9.1.1 \
    ruff==0.17.1 \
    setuptools==84.0.0 \
    tomlkit==0.15.2 \
    trove-classifiers==2026.9.21.13 \
    wheel==0.48.0
RUN python3 -m pip install --no-cache-dir --no-build-isolation --no-deps -e .
CMD ["/bin/bash"]
