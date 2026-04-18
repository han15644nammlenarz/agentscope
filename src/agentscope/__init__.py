# -*- coding: utf-8 -*-
"""AgentScope - A flexible multi-agent framework."""

from agentscope.version import __version__

# Personal fork: expose commonly used components at the top level for convenience
from agentscope.agents import AgentBase
from agentscope.models import ModelWrapperBase

__all__ = ["__version__", "AgentBase", "ModelWrapperBase"]
