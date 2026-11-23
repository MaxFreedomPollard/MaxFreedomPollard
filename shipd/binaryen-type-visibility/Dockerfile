FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest
WORKDIR /app
COPY . .

# Populate the uninitialized third_party/googletest git submodule at its exact pinned commit
# (e2239ee6043f73722e7aa812a459f54a28552929) only when absent, without replacing checked-out files.
RUN if [ ! -f third_party/googletest/googletest/src/gtest-all.cc ]; then \
      if [ -d .git ]; then \
        git config --global --add safe.directory /app \
        && git submodule update --init --depth 1 third_party/googletest; \
      else \
        curl -fsSL -o /tmp/googletest.tar.gz \
          https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.tar.gz \
        && echo "2765fbfaa978e90d1c8477bc2f2b9705be65b1b562bb215dbfaa76567d508fe1  /tmp/googletest.tar.gz" \
           | sha256sum -c - \
        && mkdir -p third_party/googletest \
        && tar -xzf /tmp/googletest.tar.gz --strip-components=1 -C third_party/googletest \
        && rm -f /tmp/googletest.tar.gz; \
      fi; \
    fi

# Pre-build libbinaryen, wasm-opt, and binaryen-unittests into /opt/binaryen-build outside /app
# so /app stays clean and incremental rebuilds take seconds without running any tests here.
ENV CC=clang \
    CXX=clang++
RUN cmake -S /app -B /opt/binaryen-build -G Ninja -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_TESTS=ON -DBUILD_TOOLS=ON -DENABLE_WERROR=OFF \
 && ninja -C /opt/binaryen-build wasm-opt binaryen-unittests \
 && chmod -R a+rwX /opt/binaryen-build

CMD ["/bin/bash"]
