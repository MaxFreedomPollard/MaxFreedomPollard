FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# The checkout in /app is the library under development, so an editable install (equivalent to pip install -e .) is intentional: every
# edit to it must take effect for the tests. Install pinned runtime, test, linter, and build dependencies.
RUN pip install --no-cache-dir apispec==6.10.0 asgiref==3.12.1 blinker==1.9.0 click==8.5.0 coverage==7.16.2 Flask==3.1.3 flit_core==4.1.0 iniconfig==2.3.1 itsdangerous==2.2.0 Jinja2==3.1.6 MarkupSafe==3.0.4 marshmallow==4.3.1 packaging==26.3 pluggy==1.7.0 Pygments==2.21.0 pytest==9.1.1 pytest-cov==7.1.0 PyYAML==6.0.3 ruff==0.17.1 setuptools==84.0.0 webargs==8.7.1 Werkzeug==3.1.9 wheel==0.48.0
RUN python3 -c "import os, site, zipfile, flit_core.buildapi as b; sp = site.getsitepackages()[0]; w = b.build_editable('/tmp'); zipfile.ZipFile('/tmp/' + w).extractall(sp); os.remove('/tmp/' + w)"
CMD ["/bin/bash"]
