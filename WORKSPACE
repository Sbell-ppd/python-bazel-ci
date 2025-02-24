load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    urls = [
        "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
    ],
    sha256 = "your_sha256_checksum_here",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    requirements = "//:requirements.txt",
)
