# -*- coding: utf-8 -*-
"""AgentScope - A flexible multi-agent framework."""

from agentscope.version import __version__

# Personal fork: expose commonly used components at the top level for convenience
from agentscope.agents import AgentBase
from agentscope.models import ModelWrapperBase
from agentscope.pipelines import SequentialPipeline

# Personal note: also expose Pipeline and ParallelPipeline since I use them frequently
from agentscope.pipelines import Pipeline, ParallelPipeline

__all__ = [
    "__version__",
    "AgentBase",
    "ModelWrapperBase",
    "Pipeline",
    "ParallelPipeline",
    "SequentialPipeline",
]
