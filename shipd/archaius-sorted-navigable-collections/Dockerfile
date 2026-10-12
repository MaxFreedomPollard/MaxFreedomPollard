FROM public.ecr.aws/d3j8x8q7/olympus-base-jvm:latest
WORKDIR /app

# This checkout compiles and launches tests with Java 8. Install the same
# Temurin 8u504-b01 release through Adoptium's signed Debian repository.
# Vendor the public signing key below so rebuilds never fetch a mutable key URL.
# Restrict its trust to this source and verify the expected fingerprint.
RUN printf '%s\n' '-----BEGIN PGP PUBLIC KEY BLOCK-----' \
    '' \
    mQENBGGTvTQBCAC6ey144n7CG8foafF6mwgIBN1fIm1ILZDuGS4tMr0/XI8pgJnT \
    QvsPxZWEvtSm7bEMObzEoZJcXwjBcJl1B0ui8k5kHMTI75gCmZPsoKLFWIEpuRBQ \
    PBocusw80apDmLnNDQLVQvDFtEua5gaNa/fRw9YsmBoXBqvgrjFUIdGyWoQvH5+a \
    9OYlWD9n5VV0gnVMb+aclwVzB/zJw3kHGSgzuMtlAHeQiah7Y8yomQn/UIX8yqDf \
    +11sP3+c87YcjkRqImRTtmKEDcEtGPAIXC6SYA+uEEkbYE0Fy0chkvtnVWJ597fa \
    Epai4rnICU8zoJ6X5z3v1aM2WerhX9oq9X8PABEBAAG0QEFkb3B0aXVtIEdQRyBL \
    ZXkgKERFQi9SUE0gU2lnbmluZyBLZXkpIDx0ZW11cmluLWRldkBlY2xpcHNlLm9y \
    Zz6JAVIEEwEIADwWIQQ7BNdTyQUNml00PzmEPEilZfjwSwUCYZO9NAIbAwULCQgH \
    AgMiAgEGFQoJCAsCBBYCAwECHgcCF4AACgkQhDxIpWX48Et4AggAjjJzYWuKV3nG \
    7ngInngl8G/m9JoHr7BmwgcQXYhdy5hVkMcUx5JLeXz2LMBUH/F2nD595hgjMabk \
    kVib20X8lq9RsNbdfc2hBcWU6qyHKxsIqT4boI2/XDyEzzMyyZWWNGo/27Ci7Xmj \
    pWu31nh0pDdPqdyWDIKojbVVnxlCRY8as8Sm+1ufi709KCi4MuwHNsUlCSwb/fju \
    NKeHkrHbLcHKUUIEcmTSKRWrpMYBzm1HYOGBz4xPuELwUfUp71ehfoyBZlp6RDRf \
    l5TYI1FmCyHuvjNhrJgWv7bOTcf8yObGY+TEUhzc4xQqCrF4ur9d3opvsuPBQsv+ \
    Klqi5KSZgrkBDQRhk700AQgAq14okly8cFrpYVenEQPiB75AUZfKRpMduiR6IxAj \
    SKcH7aSoFZ9AubUEBVpZsyT5svxoEPe1i4TdbF+m9FGy42EcOlLa3ArLTj5H8FRl \
    UdGZB9I5mk4GptOzPM+aHMMu92vW/ZwjuS8DvOiQSp+cUmG1EqOMJSM7e/4BM71z \
    E+OKaVJCj79pEzhG3SK/IC/OlxxyETT66NSfYJd7Sw5R6Vr19am/uNU690W0CJ+q \
    VQeFpmDMr7LnfdFRIh+lJe05+PvWXeidkGjox5cbG52wf8aRIR/FgkfcFvqRMN1f \
    B+dVOWueloUeVAnzcUznOKmUEs7LP9ObJhYHHgup4IAU2wARAQABiQE2BBgBCAAg \
    FiEEOwTXU8kFDZpdND85hDxIpWX48EsFAmGTvTQCGwwACgkQhDxIpWX48EvXHQf/ \
    Q0nZsGDXnZHiBoojeSdpkO7WBjMIP3w1GdLvRpPQrS8TfOPbZuoevzCNh38Y3gwF \
    yelJspvzDQrBXhgkzAGlucYg8Y7KHa5Ebm7iDgMzc37L1hYSZTYCqwd7aowfgy34 \
    hOk3B67LffkJpIh738Oa9CtlwxQ9xcytmBmQ1fBBOwm/9IhAwHPQuydYIs4DxWbj \
    0MGSP4fDntU7e4UjsHNmhudDcYol0FaqdHHIIB9C/G4CzetRwHFOn3b4JwXMU7YU \
    6aJA3mXhi3hggMC3wkT2HHZ/TquuOdNc02fypWOCDOHz0alBBJNqoVUNFNqU3tfJ \
    wI4qF/KKq9BfyfucAs0ykA== \
    =szki \
    '-----END PGP PUBLIC KEY BLOCK-----' > /tmp/adoptium.asc
RUN set -eux; \
    test "$(gpg --batch --show-keys --with-colons /tmp/adoptium.asc | awk -F: '$1 == "fpr" {print $10; exit}')" = 3B04D753C9050D9A5D343F39843C48A565F8F04B; \
    gpg --batch --dearmor -o /usr/share/keyrings/adoptium.gpg /tmp/adoptium.asc; \
    . /etc/os-release; \
    printf 'deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb %s main\n' "$VERSION_CODENAME" > /etc/apt/sources.list.d/adoptium.list; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends temurin-8-jdk=8.0.504.0.0+1-0; \
    ln -s "/usr/lib/jvm/temurin-8-jdk-$(dpkg --print-architecture)" /opt/jdk8; \
    rm -f /tmp/adoptium.asc; \
    rm -rf /var/lib/apt/lists/*; \
    /opt/jdk8/bin/java -version

# The base image ships /etc/profile.d/gradle.sh, which exports
# GRADLE_USER_HOME=/opt/gradle-cache. A login shell applies that after this
# ENV, so setting any other value here would be silently overridden and the
# properties file below would never be read. Naming the same directory makes a
# login shell and a plain shell agree.
ENV GRADLE_USER_HOME=/opt/gradle-cache
RUN mkdir -p /opt/gradle-cache \
 && printf 'org.gradle.java.installations.paths=/opt/jdk8\n' >> /opt/gradle-cache/gradle.properties

# Gradle reads the git metadata of the checkout during configuration; without
# this it refuses the directory as owned by another user and reports it as an
# unrelated failure.
RUN git config --global --add safe.directory '*'

# Match the system command to the repository wrapper. The base image's default
# gradle command selects 9.5.0, which cannot configure this pinned checkout.
RUN printf '#!/usr/bin/env bash\nexport GRADLE_USER_HOME="${GRADLE_USER_HOME:-/opt/gradle-cache}"\nexec /opt/gradle-8.14.2/bin/gradle "$@"\n' > /usr/local/bin/gradle \
 && chmod 755 /usr/local/bin/gradle

COPY . .

# The Gradle version is pinned by the repository's own wrapper
# (gradle/wrapper/gradle-wrapper.properties names 8.14.2 and its distribution
# URL). Dependencies are resolved here, while the network still exists, into
# GRADLE_USER_HOME above.
#
# NO TEST IS RUN DURING THIS BUILD. testClasses compiles the main and test
# sources without executing anything, and the init script below resolves every
# resolvable configuration in every module, which is what pulls the test RUNTIME
# artefacts (the JUnit platform launcher and engines) into the cache. Without
# that second step the first offline test run would try to reach the network.
# Tests are run only by ./test.sh, which takes a mode argument of base or new
# and writes JUnit XML to --output_path.
RUN printf 'allprojects {\n  tasks.register("resolveEveryConfiguration") {\n    doLast { configurations.findAll { it.canBeResolved }.each { it.resolve() } }\n  }\n}\n' > /opt/resolve-all.gradle
RUN ./gradlew --no-daemon --console=plain --init-script /opt/resolve-all.gradle testClasses resolveEveryConfiguration

# Keep a dependency seed separate from mutable daemon and native-process state.
# test.sh copies it into a fresh writable Gradle home for each invocation.
RUN mkdir -p /opt/archaius-gradle-seed/caches \
 && cp -a /opt/gradle-cache/caches/modules-2 /opt/archaius-gradle-seed/caches/ \
 && cp -a /opt/gradle-cache/wrapper /opt/gradle-cache/gradle.properties /opt/archaius-gradle-seed/ \
 && find /opt/archaius-gradle-seed -type f \( -name '*.lock' -o -name gc.properties \) -delete \
 && chmod -R a+rX /opt/archaius-gradle-seed \
 && chown -R 1000:1000 /opt/gradle-cache

CMD ["/bin/bash"]
