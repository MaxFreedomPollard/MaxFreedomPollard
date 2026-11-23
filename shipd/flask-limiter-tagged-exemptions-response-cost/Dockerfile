FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest
WORKDIR /app
COPY . .
# Install pinned runtime, typecheck/lint, and test dependencies only without running explicit Python build commands such as pip install -e .; ENV PYTHONPATH=/app exposes the live /app source checkout directly for editable development.
RUN pip install --no-cache-dir aniso8601==10.0.1 asgiref==3.13.0 attrs==26.1.0 blinker==1.9.0 click==8.5.0 coverage==7.17.2 Deprecated==3.0.1 dnspython==2.9.2 Flask==3.1.3 Flask-RESTful==0.3.10 flask-restx==1.3.2 hiro==1.1.1 importlib_resources==7.1.0 iniconfig==2.3.1 itsdangerous==2.2.0 Jinja2==3.1.6 jsonschema==4.26.0 jsonschema-specifications==2025.9.1 librt==0.7.2 limits==5.8.0 markdown-it-py==4.2.0 MarkupSafe==3.0.4 mdurl==0.1.2 mypy==1.19.0 mypy-extensions==1.1.0 ordered-set==4.1.0 packaging==26.3 pathspec==0.12.1 pluggy==1.7.0 Pygments==2.21.0 pymemcache==4.0.0 pymongo==4.19.0 pytest==9.2.0 pytest-check==3.0.3 pytest-cov==7.1.0 pytest-mock==3.17.0 pytz==2026.6 redis==8.1.0 referencing==0.37.0 rich==14.3.4 rpds-py==2026.9.1 ruff==0.14.8 six==1.17.0 typing_extensions==4.16.0 Werkzeug==3.1.9 wrapt==2.5.2
ENV PYTHONPATH=/app
# Materialize the gitignored hatch-vcs version-file declared in pyproject.toml ([tool.hatch.build.hooks.vcs] version-file = "flask_limiter/_version.py") from the checked-out HISTORY.rst release header when absent, failing the build if the extracted version is empty, and verify package import without running a build command.
RUN if [ ! -f /app/flask_limiter/_version.py ]; then ver="$(sed -n 's/^v\([0-9][0-9.]*\)$/\1/p' /app/HISTORY.rst | head -n 1)" && [ -n "$ver" ] && printf '__version__ = "%s"\n' "$ver" > /app/flask_limiter/_version.py; fi && python -c "import flask_limiter; assert flask_limiter.__version__"
CMD ["/bin/bash"]
