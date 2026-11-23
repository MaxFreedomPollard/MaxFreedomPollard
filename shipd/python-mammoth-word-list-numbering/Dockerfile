FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Install pinned runtime and test dependencies only; link /app via a .pth file instead of running pip install -e . during docker build.
RUN pip install --no-cache-dir cobble==0.1.4 Funk==0.5.0 iniconfig==2.3.1 packaging==26.3 pluggy==1.7.0 precisely==0.1.3 pyflakes==2.4.0 Pygments==2.21.0 pytest==9.2.0 setuptools==84.0.0 spur.local==0.3.19 tempman==0.1.3 wheel==0.48.0
RUN python3 -c "import site, pathlib; pathlib.Path(site.getsitepackages()[0], 'mammoth.pth').write_text('/app\n')" && printf '#!/usr/bin/env python3\nimport sys\nfrom mammoth.cli import main\nsys.exit(main())\n' > /usr/local/bin/mammoth && chmod 755 /usr/local/bin/mammoth
CMD ["/bin/bash"]
