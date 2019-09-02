load(
  "@rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

load("@my_deps//:requirements.bzl", "requirement")

py_binary(
    name = "master",
    srcs = [
      "client.py",
      "render.py",
      "master.py"
    ],
    deps = [
        requirement("flask"),
        requirement("flask-jsonpify"),
        requirement("flask-sqlalchemy"),
        requirement("flask-restful"),
        requirement("Werkzeug"),
        requirement("jinja2"),
        requirement("MarkupSafe"),
        requirement("click"),
        requirement("itsdangerous")
    ],
    # FIXME, flask requires html to be a templates folder...
    data = glob(["client/dist/client/**"]),
)
