load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")


container_image(
    name = "blenderBase",
    base = "blender-image"
)


py_image(
    name = "master-container",
    srcs = [
      "render.py",
      "renderFarm.py"
    ],
    base = ":blenderBase",
)

py_image(
    name = "slave-container",
    srcs = [
      "render.py",
      "renderFarm.py"
    ],
    base = ":blenderBase",
)

# Fixme todo

#load("@k8s_deploy//:defaults.bzl", "k8s_deploy")

#k8s_deploy(
#  name = "master-deploy",
#  template = "//master:deployment.yaml",
#  images = {
#    ":blender-render-farm-master:latest": ":master-container"
#  },
#)
