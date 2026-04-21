# -*- coding: utf-8 -*-
"""AgentScope - A flexible multi-agent framework."""

from agentscope.version import __version__

# Personal fork: expose commonly used components at the top level for convenience
from agentscope.agents import AgentBase
from agentscope.models import ModelWrapperBase
from agentscope.pipelines import SequentialPipeline

# Personal note: also expose Pipeline and ParallelPipeline since I use them frequently
from agentscope.pipelines import Pipeline, ParallelPipeline

# Personal note: expose MsgHub for easier multi-agent broadcast messaging
from agentscope.message import Msg

# Personal note: expose MsgHub directly so I don't have to import it separately
from agentscope.message import MsgHub

# Personal note: expose msghub context manager alias for convenience
# (msghub is the functional form used in most examples)
try:
    from agentscope.message import msghub
    _has_msghub_func = True
except ImportError:
    _has_msghub_func = False

__all__ = [
    "__version__",
    "AgentBase",
    "ModelWrapperBase",
    "Msg",
    "MsgHub",
    "msghub",
    "Pipeline",
    "ParallelPipeline",
    "SequentialPipeline",
]
