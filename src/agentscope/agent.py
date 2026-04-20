# -*- coding: utf-8 -*-
"""Base agent module for AgentScope.

This module defines the foundational Agent class that all agents in
AgentScope should inherit from.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence


class AgentBase(ABC):
    """Abstract base class for all agents in AgentScope.

    All agents must implement the `reply` method, which defines how
    the agent responds to incoming messages.

    Attributes:
        name (str): The name of the agent.
        sys_prompt (str): The system prompt used to configure agent behavior.
    """

    def __init__(
        self,
        name: str,
        sys_prompt: Optional[str] = None,
    ) -> None:
        """Initialize an AgentBase instance.

        Args:
            name (str): The name of the agent.
            sys_prompt (Optional[str]): An optional system prompt to configure
                the agent's behavior. Defaults to None.
        """
        self.name = name
        self.sys_prompt = sys_prompt or ""
        self._memory: list = []

    @abstractmethod
    def reply(self, x: Optional[Any] = None) -> Any:
        """Generate a reply based on the input message.

        Subclasses must implement this method to define agent behavior.

        Args:
            x (Optional[Any]): The input message or data to respond to.
                Defaults to None.

        Returns:
            Any: The agent's response.
        """

    def observe(self, x: Any) -> None:
        """Observe a message without generating a reply.

        Useful for updating the agent's memory or state based on
        messages from other agents.

        Args:
            x (Any): The message or data to observe.
        """
        if isinstance(x, list):
            self._memory.extend(x)
        else:
            self._memory.append(x)

    def clear_memory(self) -> None:
        """Clear the agent's memory."""
        self._memory.clear()

    @property
    def memory(self) -> list:
        """Return a copy of the agent's current memory.

        Returns:
            list: A copy of the agent's memory list.
        """
        return list(self._memory)

    def __call__(self, x: Optional[Any] = None) -> Any:
        """Make the agent callable, delegating to the `reply` method.

        Args:
            x (Optional[Any]): The input message or data.

        Returns:
            Any: The agent's response.
        """
        return self.reply(x)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"

    def __str__(self) -> str:
        return self.__repr__()
