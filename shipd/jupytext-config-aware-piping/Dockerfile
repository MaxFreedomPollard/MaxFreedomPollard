FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Install pinned runtime and test dependencies only; this repository is the jupytext project itself and provides the 'jupytext' package (including jupytext.cli) under /app/src/jupytext, so the 'jupytext' module is satisfied from /app/src rather than by pip via an editable install (equivalent to pip install -e .) using jupytext.pth.
RUN pip install --no-cache-dir autopep8==2.3.2 black==24.10.0 coverage==7.17.1 flake8==7.3.0 gitdb==4.0.12 GitPython==3.1.50 ipykernel==7.4.0 isort==8.0.1 jupyter_client==8.10.0 jupyter_server==2.21.1 markdown-it-py==4.2.0 mccabe==0.7.0 mdit-py-plugins==0.6.1 nbconvert==7.17.2 nbformat==5.11.1 packaging==26.3 pycodestyle==2.14.0 pyflakes==3.4.0 pytest==9.2.0 pytest-asyncio==1.4.1.post1 PyYAML==6.0.3 ruff==0.17.3 smmap==5.0.3 traitlets==5.16.1
RUN python3 -c "import site, pathlib; pathlib.Path(site.getsitepackages()[0], 'jupytext.pth').write_text('/app/src\n')" && printf '#!/usr/bin/env python3\nimport sys\nfrom jupytext.cli import jupytext\nsys.exit(jupytext())\n' > /usr/local/bin/jupytext && printf '#!/usr/bin/env python3\nimport sys\nfrom jupytext_config.__main__ import main\nsys.exit(main())\n' > /usr/local/bin/jupytext-config && chmod 755 /usr/local/bin/jupytext /usr/local/bin/jupytext-config
CMD ["/bin/bash"]
