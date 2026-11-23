FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Isolate the pinned toolchain from the base image's independent package managers.
RUN python3 -m venv /opt/pokerkit-env
ENV PATH="/opt/pokerkit-env/bin:$PATH" VIRTUAL_ENV=/opt/pokerkit-env
# Upstream requirements.txt uses version ranges; this committed Dockerfile records
# the complete dependency lock for this submission, including all transitive pins.
# Keep the installer on one line for the offline wheelhouse vendor to rewrite.
RUN pip install --no-cache-dir setuptools==82.0.1 wheel==0.45.1 packaging==26.3 typing-extensions==4.16.0 mypy-extensions==1.1.0 pycparser==3.12 types-psutil==7.2.2.20260906 types-setuptools==84.0.0.20261006 alabaster==1.0.0 attrs==26.1.0 babel==2.18.0 build==1.2.2post1 certifi==2026.10.23 cffi==2.1.1 charset-normalizer==3.5.2 click==8.5.0 colorama==0.4.6 coverage==7.6.12 cryptography==50.0.2 docutils==0.21.2 flake8==7.1.2 idna==3.20 imagesize==2.0.1 iniconfig==2.3.1 interrogate==1.7.0 jaraco-classes==3.4.0 jaraco-context==6.1.2 jaraco-functools==4.6.0 jeepney==0.9.0 jinja2==3.1.6 keyring==24.3.1 markdown-it-py==4.2.0 markupsafe==3.0.4 mccabe==0.7.0 mdurl==0.1.2 more-itertools==11.2.1 mypy==1.13.0 nh3==0.3.7 pkginfo==1.12.1.2 pluggy==1.7.0 py==1.11.0 pycodestyle==2.12.1 pyflakes==3.2.0 pygments==2.21.0 pyproject-hooks==1.3.3 pytest==8.3.5 readme-renderer==46.0 requests==2.34.2 requests-toolbelt==1.0.0 rfc3986==2.0.0 rich==15.0.0 secretstorage==3.5.0 snowballstemmer==3.1.1 sphinx==8.1.3 sphinx-rtd-theme==3.0.2 sphinxcontrib-applehelp==2.0.0 sphinxcontrib-devhelp==2.0.0 sphinxcontrib-htmlhelp==2.1.0 sphinxcontrib-jquery==4.1 sphinxcontrib-jsmath==2.0.0 sphinxcontrib-qthelp==2.0.0 sphinxcontrib-serializinghtml==2.0.0 tabulate==0.10.0 twine==6.0.1 urllib3==2.8.0
# setup.py names the pure-Python library pokerkit, located at /app/pokerkit.
# Register that checkout in site-packages so edits are visible from any directory,
# including Python -I. Root writes the registration at build time; runtime only reads it.
# Editable source import installation, equivalent to pip install -e . for source lookup.
ENV PYTHONPATH=/app
RUN python3 -c "import site; from pathlib import Path; Path(site.getsitepackages()[0], 'pokerkit.pth').write_text('/app\n')"
CMD ["/bin/bash"]
