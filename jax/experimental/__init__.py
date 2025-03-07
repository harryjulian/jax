# Copyright 2018 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO(https://github.com/google/jax/issues/13487): Remove PartitionSpec in
# 3 months from `jax.experimental.PartitionSpec`.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/google/jax/issues/7570

from jax.interpreters.pxla import PartitionSpec as PartitionSpec
from jax.experimental.x64_context import (
  enable_x64 as enable_x64,
  disable_x64 as disable_x64,
)
