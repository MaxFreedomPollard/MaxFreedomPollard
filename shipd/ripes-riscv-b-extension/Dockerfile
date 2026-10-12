FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest
WORKDIR /app

COPY . .

# Every download happens during this build; the finished image builds and runs
# the tests offline.

# OpenGL, EGL and xkbcommon libraries that Qt's GUI module links against, and
# Debian's Python with its venv module for the Qt installer below.
RUN apt-get update -q \
 && DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends \
      libgl-dev=1.6.0-1 libegl-dev=1.6.0-1 libopengl-dev=1.6.0-1 libxkbcommon0=1.5.0-1 \
      python3=3.11.2-1+b1 python3-venv=3.11.2-1+b1 \
 && rm -rf /var/lib/apt/lists/*

# Qt 6.9.3 with Charts, the version the repository's CI uses. The apt sources
# have only Qt 6.4 and no Qt Charts, so aqtinstall fetches it from a temporary
# virtual environment on that Python. aqt checks each archive against the
# SHA-256 published on download.qt.io.
RUN /usr/bin/python3 -m venv /tmp/aqt \
 && /tmp/aqt/bin/pip install --no-cache-dir aqtinstall==3.3.0 \
 && /tmp/aqt/bin/aqt install-qt linux desktop 6.9.3 linux_gcc_64 -m qtcharts -O /opt/Qt \
 && rm -rf /tmp/aqt aqtinstall.log

# The base image's clang; GCC 12 rejects the constrained template
# specializations in src/binutils.h.
ENV CC=clang \
    CXX=clang++ \
    CMAKE_PREFIX_PATH=/opt/Qt/6.9.3/gcc_64 \
    LD_LIBRARY_PATH=/opt/Qt/6.9.3/gcc_64/lib \
    QT_QPA_PLATFORM=offscreen

# The VSRTL submodule at the commit the repository pins, always from that
# commit's archive, checked against its SHA-256, so the result is the same
# whether or not the build context carries .git or submodule contents.
RUN curl -fsSL -o /tmp/vsrtl.tar.gz \
      https://github.com/mortbopet/VSRTL/archive/8497dd14fe80e57efcff4c424a9a3b6363d93eb7.tar.gz \
 && echo "44258800cf9a6ae75fa71ca140c59a695400f8ebb4b00d305d45d15b3684dc03  /tmp/vsrtl.tar.gz" \
    | sha256sum -c - \
 && rm -rf external/VSRTL \
 && mkdir -p external/VSRTL \
 && tar -xzf /tmp/vsrtl.tar.gz --strip-components=1 -C external/VSRTL \
 && rm -f /tmp/vsrtl.tar.gz

# Configure and compile once, test binaries included, so test runs rebuild only
# what a change touches; then make later reconfigures offline. Tests may run as
# a non-root user, so every uid can edit and rebuild the tree. No tests run here.
RUN cmake -S . -B build -G Ninja -Wno-dev -DCMAKE_BUILD_TYPE=Release \
      -DRIPES_BUILD_TESTS=ON -DVSRTL_BUILD_TESTS=OFF \
 && cmake --build build \
 && cmake -S . -B build -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
 && chmod -R a+rwX /app

CMD ["/bin/bash"]
