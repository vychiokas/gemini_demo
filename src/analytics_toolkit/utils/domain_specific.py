"""
SCENARIO 5: Tasks where AI agents struggle.

This module demonstrates scenarios where AI coding agents have limitations:

1. DOMAIN-SPECIFIC BUSINESS LOGIC
   - Agents don't know your company's business rules
   - They may generate technically correct but business-incorrect code

2. CREATIVE/SUBJECTIVE DECISIONS
   - UI/UX design choices
   - Code architecture preferences
   - Naming conventions beyond common patterns

3. EXTERNAL DEPENDENCIES
   - Integration with specific company systems
   - Proprietary APIs without public documentation
   - Environment-specific configurations

4. HIGHLY SPECIALIZED ALGORITHMS
   - Domain-specific mathematical models
   - Industry-specific calculations
   - Regulatory compliance logic

DEMO: Ask the agent to implement these - observe where it struggles or asks for clarification.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


# === Scenario 5.1: Domain-Specific Business Logic ===
# Agent doesn't know: company pricing rules, customer tier definitions, etc.

@dataclass
class Customer:
    id: str
    name: str
    tier: str  # What tiers exist? What privileges?
    account_balance: Decimal
    signup_date: datetime


def calculate_customer_discount(customer: Customer, base_price: Decimal) -> Decimal:
    """
    Calculate discount for customer based on company's pricing rules.

    TODO: Implement company-specific discount logic
    - What are the customer tiers and their discounts?
    - Are there special promotions running?
    - How does account balance affect pricing?
    - Are there loyalty discounts based on signup_date?

    The agent CANNOT know these business rules without being told.
    """
    # Agent will likely generate generic discount logic
    # but won't know YOUR company's specific rules
    raise NotImplementedError("Business rules not specified")


def calculate_commission(
    sale_amount: Decimal,
    salesperson_id: str,
    product_category: str,
) -> Decimal:
    """
    Calculate sales commission based on company policy.

    Questions only a human can answer:
    - What is the base commission rate?
    - Do different product categories have different rates?
    - Are there sales targets that affect commission?
    - How do team vs individual sales work?
    - Are there caps on commission?
    """
    raise NotImplementedError("Company commission policy not specified")


# === Scenario 5.2: External System Integration ===
# Agent doesn't have access to: internal APIs, database schemas, etc.

def sync_with_legacy_erp(data: dict) -> bool:
    """
    Sync data with company's legacy ERP system.

    Challenges for AI agents:
    - No documentation for internal ERP API
    - Unknown authentication mechanism
    - Proprietary data formats
    - Network configuration requirements

    This requires institutional knowledge the agent doesn't have.
    """
    raise NotImplementedError("Internal system details required")


def process_compliance_report(transactions: list[dict]) -> dict:
    """
    Generate compliance report per regulatory requirements.

    Challenges:
    - Agent doesn't know which regulations apply (GDPR? SOX? HIPAA?)
    - Specific reporting formats required by regulators
    - Audit trail requirements
    - Data retention policies
    """
    raise NotImplementedError("Regulatory requirements not specified")


# === Scenario 5.3: Subjective Design Decisions ===

def design_dashboard_layout(metrics: list[dict]) -> dict:
    """
    Design the layout for a metrics dashboard.

    Subjective questions:
    - How should metrics be grouped?
    - What visualizations are most appropriate?
    - What color scheme matches company branding?
    - What is the priority/importance of each metric?
    - How should mobile layout differ from desktop?

    Agent can generate A layout, but not YOUR preferred layout.
    """
    raise NotImplementedError("Design preferences not specified")


# === Scenario 5.4: Specialized Algorithms ===

def calculate_insurance_premium(
    customer_age: int,
    risk_factors: list[str],
    coverage_amount: Decimal,
    policy_type: str,
) -> Decimal:
    """
    Calculate insurance premium using actuarial models.

    Challenges:
    - Requires actuarial tables (proprietary data)
    - Company-specific risk models
    - Regulatory requirements for pricing
    - Historical loss data

    Generic algorithm won't match your actuarial models.
    """
    raise NotImplementedError("Actuarial models required")


def optimize_supply_chain(
    inventory: dict[str, int],
    demand_forecast: dict[str, list[int]],
    supplier_contracts: list[dict],
) -> dict[str, int]:
    """
    Optimize inventory ordering based on supply chain constraints.

    Domain-specific challenges:
    - Supplier contract terms
    - Warehouse capacity limits
    - Shipping cost structures
    - Lead time variability
    - Safety stock policies

    Each company's supply chain is unique.
    """
    raise NotImplementedError("Supply chain parameters required")


# === Scenario 5.5: Ambiguous Requirements ===

def process_user_feedback(feedback: str) -> dict:
    """
    Process and categorize user feedback.

    Ambiguous aspects:
    - What categories exist?
    - What is the priority scale?
    - How to handle mixed sentiment?
    - What triggers escalation?
    - What languages are supported?

    Requirements are unclear - agent will make assumptions.
    """
    raise NotImplementedError("Feedback processing rules not defined")


# === Summary of when NOT to use AI agents ===

AGENT_LIMITATIONS = """
When to AVOID relying on AI coding agents:

1. BUSINESS LOGIC
   - Company-specific rules and policies
   - Pricing/discount calculations
   - Compliance and regulatory requirements
   - Commission/bonus calculations

2. INTEGRATION
   - Internal/proprietary APIs
   - Legacy systems without documentation
   - Environment-specific configurations
   - Authentication with internal systems

3. SUBJECTIVE DECISIONS
   - UI/UX design choices
   - Architecture preferences
   - Code style beyond standard conventions
   - Feature prioritization

4. SPECIALIZED DOMAINS
   - Actuarial calculations
   - Financial models
   - Industry-specific algorithms
   - Regulatory compliance logic

5. AMBIGUOUS REQUIREMENTS
   - Vague user stories
   - Conflicting requirements
   - Missing edge cases
   - Undefined error handling

BEST PRACTICE: Use agents for well-defined technical tasks.
Provide clear specifications for business logic.
Review agent output critically for domain correctness.
"""
