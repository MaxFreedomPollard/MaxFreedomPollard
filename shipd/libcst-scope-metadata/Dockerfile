FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Project runtime dependencies, pinned (see pyproject.toml [project] dependencies).
RUN pip install --no-cache-dir pyyaml==6.0.2 pytest==9.1.1
# LibCST's parser needs its compiled native extension. Take the prebuilt
# extension from the matching published wheel so the image build does not
# require a Rust toolchain, then remove the wheel again.
RUN pip install --no-cache-dir libcst==1.9.0 \
 && SITE_PACKAGES="$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')" \
 && mkdir -p /app/libcst \
 && cp "$SITE_PACKAGES"/libcst/native*.so /app/libcst/ \
 && pip uninstall -y libcst
# Editable install of the checkout. The native extension is already present
# above, so the Rust build step is skipped for the install and setup.py is
# restored unchanged afterwards.
RUN cp setup.py /tmp/setup.py.orig \
 && python -c "import pathlib; p = pathlib.Path('setup.py'); p.write_text(p.read_text().replace('rust_extensions=[', 'rust_extensions=[] and [', 1))" \
 && SETUPTOOLS_SCM_PRETEND_VERSION=1.9.0 pip install --no-cache-dir -e . \
 && mv /tmp/setup.py.orig setup.py
CMD ["/bin/bash"]
