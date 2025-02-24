load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "test_math_utils",
    srcs = ["test_math_utils.py"],
    deps = [
        "//:math_utils",
        "@pip//:pytest",
    ],
)

py_test(
    name = "test_string_utils",
    srcs = ["test_string_utils.py"],
    deps = [
        "//:string_utils",
        "@pip//:pytest",
    ],
)
