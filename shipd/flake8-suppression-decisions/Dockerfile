FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest

WORKDIR /app
COPY . /app

# The checkout at efe6750405be77b661f64e60002c4ef8e922daf5 supplies Flake8 7.3.0.
# uv uses the frozen dependency graph and editable source dependency below.
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON=/usr/local/bin/python
RUN mkdir -p /opt/dev-env \
    && printf '%s\n' \
    '[project]' \
    'name = "flake8-development"' \
    'version = "0.0.0"' \
    'requires-python = ">=3.12,<3.13"' \
    'dependencies = [' \
    '  "flake8==7.3.0",' \
    '  "pytest==8.4.2",' \
    '  "iniconfig==2.3.0",' \
    '  "packaging==26.2",' \
    '  "pluggy==1.6.0",' \
    '  "Pygments==2.20.0",' \
    '  "mccabe==0.7.0",' \
    '  "pycodestyle==2.14.0",' \
    '  "pyflakes==3.4.0",' \
    '  "setuptools==80.9.0",' \
    '  "wheel==0.45.1",' \
    ']' \
    '[tool.uv]' \
    'package = false' \
    'build-constraint-dependencies = ["setuptools==80.9.0", "wheel==0.45.1", "packaging==26.2"]' \
    '[tool.uv.sources]' \
    'flake8 = { path = "/app", editable = true }' \
    > /opt/dev-env/pyproject.toml \
    && printf '%s\n' \
    'version = 1' \
    'revision = 3' \
    'requires-python = "==3.12.*"' \
    '' \
    '[manifest]' \
    'build-constraints = [' \
    '    { name = "packaging", specifier = "==26.2" },' \
    '    { name = "setuptools", specifier = "==80.9.0" },' \
    '    { name = "wheel", specifier = "==0.45.1" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "colorama"' \
    'version = "0.4.6"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "flake8"' \
    'version = "7.3.0"' \
    'source = { editable = "/app" }' \
    'dependencies = [' \
    '    { name = "mccabe" },' \
    '    { name = "pycodestyle" },' \
    '    { name = "pyflakes" },' \
    ']' \
    '' \
    '[package.metadata]' \
    'requires-dist = [' \
    '    { name = "mccabe", specifier = ">=0.7.0,<0.8.0" },' \
    '    { name = "pycodestyle", specifier = ">=2.14.0,<2.15.0" },' \
    '    { name = "pyflakes", specifier = ">=3.4.0,<3.5.0" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "flake8-development"' \
    'version = "0.0.0"' \
    'source = { virtual = "." }' \
    'dependencies = [' \
    '    { name = "flake8" },' \
    '    { name = "iniconfig" },' \
    '    { name = "mccabe" },' \
    '    { name = "packaging" },' \
    '    { name = "pluggy" },' \
    '    { name = "pycodestyle" },' \
    '    { name = "pyflakes" },' \
    '    { name = "pygments" },' \
    '    { name = "pytest" },' \
    '    { name = "setuptools" },' \
    '    { name = "wheel" },' \
    ']' \
    '' \
    '[package.metadata]' \
    'requires-dist = [' \
    '    { name = "flake8", editable = "/app" },' \
    '    { name = "iniconfig", specifier = "==2.3.0" },' \
    '    { name = "mccabe", specifier = "==0.7.0" },' \
    '    { name = "packaging", specifier = "==26.2" },' \
    '    { name = "pluggy", specifier = "==1.6.0" },' \
    '    { name = "pycodestyle", specifier = "==2.14.0" },' \
    '    { name = "pyflakes", specifier = "==3.4.0" },' \
    '    { name = "pygments", specifier = "==2.20.0" },' \
    '    { name = "pytest", specifier = "==8.4.2" },' \
    '    { name = "setuptools", specifier = "==80.9.0" },' \
    '    { name = "wheel", specifier = "==0.45.1" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "iniconfig"' \
    'version = "2.3.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "mccabe"' \
    'version = "0.7.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/e7/ff/0ffefdcac38932a54d2b5eed4e0ba8a408f215002cd178ad1df0f2806ff8/mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325", size = 9658, upload-time = "2022-01-24T01:14:51.113Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/27/1a/1f68f9ba0c207934b35b86a8ca3aad8395a3d6dd7921c0686e23853ff5a9/mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e", size = 7350, upload-time = "2022-01-24T01:14:49.62Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "packaging"' \
    'version = "26.2"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/d7/f1/e7a6dd94a8d4a5626c03e4e99c87f241ba9e350cd9e6d75123f992427270/packaging-26.2.tar.gz", hash = "sha256:ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661", size = 228134, upload-time = "2026-04-24T20:15:23.917Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/df/b2/87e62e8c3e2f4b32e5fe99e0b86d576da1312593b39f47d8ceef365e95ed/packaging-26.2-py3-none-any.whl", hash = "sha256:5fc45236b9446107ff2415ce77c807cee2862cb6fac22b8a73826d0693b0980e", size = 100195, upload-time = "2026-04-24T20:15:22.081Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "pluggy"' \
    'version = "1.6.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "pycodestyle"' \
    'version = "2.14.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/11/e0/abfd2a0d2efe47670df87f3e3a0e2edda42f055053c85361f19c0e2c1ca8/pycodestyle-2.14.0.tar.gz", hash = "sha256:c4b5b517d278089ff9d0abdec919cd97262a3367449ea1c8b49b91529167b783", size = 39472, upload-time = "2025-06-20T18:49:48.75Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/d7/27/a58ddaf8c588a3ef080db9d0b7e0b97215cee3a45df74f3a94dbbf5c893a/pycodestyle-2.14.0-py2.py3-none-any.whl", hash = "sha256:dd6bf7cb4ee77f8e016f9c8e74a35ddd9f67e1d5fd4184d86c3b98e07099f42d", size = 31594, upload-time = "2025-06-20T18:49:47.491Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "pyflakes"' \
    'version = "3.4.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/45/dc/fd034dc20b4b264b3d015808458391acbf9df40b1e54750ef175d39180b1/pyflakes-3.4.0.tar.gz", hash = "sha256:b24f96fafb7d2ab0ec5075b7350b3d2d2218eab42003821c06344973d3ea2f58", size = 64669, upload-time = "2025-06-20T18:45:27.834Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/c2/2f/81d580a0fb83baeb066698975cb14a618bdbed7720678566f1b046a95fe8/pyflakes-3.4.0-py2.py3-none-any.whl", hash = "sha256:f742a7dbd0d9cb9ea41e9a24a918996e8170c799fa528688d40dd582c8265f4f", size = 63551, upload-time = "2025-06-20T18:45:26.937Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "pygments"' \
    'version = "2.20.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/c3/b2/bc9c9196916376152d655522fdcebac55e66de6603a76a02bca1b6414f6c/pygments-2.20.0.tar.gz", hash = "sha256:6757cd03768053ff99f3039c1a36d6c0aa0b263438fcab17520b30a303a82b5f", size = 4955991, upload-time = "2026-03-29T13:29:33.898Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/f4/7e/a72dd26f3b0f4f2bf1dd8923c85f7ceb43172af56d63c7383eb62b332364/pygments-2.20.0-py3-none-any.whl", hash = "sha256:81a9e26dd42fd28a23a2d169d86d7ac03b46e2f8b59ed4698fb4785f946d0176", size = 1231151, upload-time = "2026-03-29T13:29:30.038Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "pytest"' \
    'version = "8.4.2"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'dependencies = [' \
    '    { name = "colorama", marker = "sys_platform == '"'"'win32'"'"'" },' \
    '    { name = "iniconfig" },' \
    '    { name = "packaging" },' \
    '    { name = "pluggy" },' \
    '    { name = "pygments" },' \
    ']' \
    'sdist = { url = "https://files.pythonhosted.org/packages/a3/5c/00a0e072241553e1a7496d638deababa67c5058571567b92a7eaa258397c/pytest-8.4.2.tar.gz", hash = "sha256:86c0d0b93306b961d58d62a4db4879f27fe25513d4b969df351abdddb3c30e01", size = 1519618, upload-time = "2025-09-04T14:34:22.711Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/a8/a4/20da314d277121d6534b3a980b29035dcd51e6744bd79075a6ce8fa4eb8d/pytest-8.4.2-py3-none-any.whl", hash = "sha256:872f880de3fc3a5bdc88a11b39c9710c3497a547cfa9320bc3c5e62fbf272e79", size = 365750, upload-time = "2025-09-04T14:34:20.226Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "setuptools"' \
    'version = "80.9.0"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/18/5d/3bf57dcd21979b887f014ea83c24ae194cfcd12b9e0fda66b957c69d1fca/setuptools-80.9.0.tar.gz", hash = "sha256:f36b47402ecde768dbfafc46e8e4207b4360c654f1f3bb84475f0a28628fb19c", size = 1319958, upload-time = "2025-05-27T00:56:51.443Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/a3/dc/17031897dae0efacfea57dfd3a82fdd2a2aeb58e0ff71b77b87e44edc772/setuptools-80.9.0-py3-none-any.whl", hash = "sha256:062d34222ad13e0cc312a4c02d73f059e86a4acbfbdea8f8f76b28c99f306922", size = 1201486, upload-time = "2025-05-27T00:56:49.664Z" },' \
    ']' \
    '' \
    '[[package]]' \
    'name = "wheel"' \
    'version = "0.45.1"' \
    'source = { registry = "https://pypi.org/simple" }' \
    'sdist = { url = "https://files.pythonhosted.org/packages/8a/98/2d9906746cdc6a6ef809ae6338005b3f21bb568bea3165cfc6a243fdc25c/wheel-0.45.1.tar.gz", hash = "sha256:661e1abd9198507b1409a20c02106d9670b2576e916d58f520316666abca6729", size = 107545, upload-time = "2024-11-23T00:18:23.513Z" }' \
    'wheels = [' \
    '    { url = "https://files.pythonhosted.org/packages/0b/2c/87f3254fd8ffd29e4c02732eee68a83a1d3c346ae39bc6822dcbcb697f2b/wheel-0.45.1-py3-none-any.whl", hash = "sha256:708e7481cc80179af0e556bbf0cc00b8444c7321e2700b8d8580231d13017248", size = 72494, upload-time = "2024-11-23T00:18:21.207Z" },' \
    ']' \
    > /opt/dev-env/uv.lock \
    && uv sync --frozen --project /opt/dev-env

ENV PATH=/opt/dev-env/.venv/bin:$PATH

RUN mkdir -p /opt/basetests \
    && cp -a /app/tests /opt/basetests/tests \
    && cp /app/pytest.ini /opt/basetests/pytest.ini \
    && ln -s /app/docs /opt/basetests/docs \
    && ln -s /app/src /opt/basetests/src \
    && ln -s /app/bin /opt/basetests/bin \
    && chmod -R a+rX /opt/basetests/tests \
    && chown -R 1000:1000 /app

# Upstream tests append to these logs; arbitrary runtime UIDs need write access.
RUN flake8_test_log="$(python -c 'import sys; print("test-logs-%s.%s.log" % sys.version_info[:2])')" \
    && touch "/app/$flake8_test_log" "/opt/basetests/$flake8_test_log" \
    && chmod a+rw "/app/$flake8_test_log" "/opt/basetests/$flake8_test_log"


CMD ["/bin/bash"]
