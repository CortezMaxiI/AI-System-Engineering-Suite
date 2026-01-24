from dataclasses import dataclass, field
from typing import Dict, Optional, List

@dataclass
class Anomaly:
    """Represents a detected issue in the system."""
    id: str
    description: str
    timestamp: str
    severity: str  # critical, warning, info
    context: Dict[str, str] = field(default_factory=dict)

@dataclass
class MitigatedPlan:
    """A proposed action to resolve an anomaly."""
    action_id: str
    description: str
    target_service: str
    command: str
    reasoning: str
    risk_level: str # low, medium, high

@dataclass
class SimulationResult:
    """Result of running a plan in the sandbox."""
    passed: bool
    details: str
    logs: List[str]
