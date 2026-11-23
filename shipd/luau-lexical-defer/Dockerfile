FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest
WORKDIR /app
COPY . .
# Luau has zero external third-party dependencies (doctest and isocline are vendored in extern/, and g++/make/libpthread are preinstalled in olympus-base-cpp).
# Pre-compile object files and $(TESTS_TARGET) ($(BUILD)/luau-tests) into /opt/luau-build to warm the incremental build cache outside /app without running any tests.
RUN mkdir -p /opt/luau-build && make -j4 BUILD=/opt/luau-build /opt/luau-build/luau-tests
CMD ["/bin/bash"]
