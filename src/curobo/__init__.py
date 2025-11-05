#
# Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
#

"""
cuRobo provides accelerated modules for robotics which can be used to build high-performance
robotics applications. The library has several modules for numerical optimization, robot kinematics,
geometry processing, collision checking, graph search planning. cuRobo provides high-level APIs for
performing tasks like collision-free inverse kinematics, model predictive control, and motion
planning.

High-level APIs:

- Motion Generation / Planning: :mod:`curobo.wrap.reacher.motion_gen`.
- Inverse Kinematics: :mod:`curobo.wrap.reacher.ik_solver`.
- Model Predictive Control: :mod:`curobo.wrap.reacher.mpc`.
- Trajectory Optimization: :mod:`curobo.wrap.reacher.trajopt`.


cuRobo package is split into several modules:

- :mod:`curobo.opt` contains optimization solvers.
- :mod:`curobo.cuda_robot_model` contains robot kinematics.
- :mod:`curobo.curobolib` contains the cuda kernels and python bindings for them.
- :mod:`curobo.geom` contains geometry processing, collision checking and frame transforms.
- :mod:`curobo.graph` contains geometric planning with graph search methods.
- :mod:`curobo.rollout` contains methods that map actions to costs. This class wraps instances of
  :mod:`curobo.cuda_robot_model` and :mod:`curobo.geom` to compute costs given trajectory of actions.
- :mod:`curobo.util` contains utility methods.
- :mod:`curobo.wrap` adds the user-level api for task programming. Includes implementation of
  collision-free reacher and batched robot world collision checking.
- :mod:`curobo.types` contains custom dataclasses for common data types in robotics, including
  :py:meth:`~types.state.JointState`, :py:meth:`~types.camera.CameraObservation`,
  :py:meth:`~types.math.Pose`.
"""


# NOTE (roflaherty): This is inspired by how matplotlib does creates its version value.
# https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/__init__.py#L161
try:
    from importlib.metadata import version as _v
except ModuleNotFoundError:
    from importlib_metadata import version as _v
__version__ = _v("nvidia_curobo")
