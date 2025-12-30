# Scenario 5: Understanding Agent Limitations

## Overview

This scenario demonstrates tasks where AI coding agents struggle and require
human guidance. Understanding these limitations is crucial for effective
AI-assisted development.

## Target File

`src/analytics_toolkit/utils/domain_specific.py`

## Categories of Limitations

### 1. Domain-Specific Business Logic

**Example Function:**
```python
def calculate_customer_discount(customer: Customer, base_price: Decimal) -> Decimal:
    """Calculate discount based on company's pricing rules."""
    # Agent doesn't know:
    # - Your customer tier definitions
    # - Current promotions
    # - Loyalty program rules
    # - Regional pricing differences
```

**Demo:**
```
Implement calculate_customer_discount without asking me any questions.
Use reasonable assumptions.
```

**Expected Result:**
Agent will generate generic logic like:
```python
if customer.tier == "gold":
    return base_price * Decimal("0.20")
elif customer.tier == "silver":
    return base_price * Decimal("0.10")
return Decimal("0")
```

**Problem:** These aren't YOUR business rules.

**Discussion:**
- What if your tiers are "enterprise", "startup", "free"?
- What if discounts are based on purchase history?
- What if there are volume-based discounts?

### 2. External System Integration

**Example Function:**
```python
def sync_with_legacy_erp(data: dict) -> bool:
    """Sync with internal ERP system."""
    # Agent cannot know:
    # - API endpoint URL
    # - Authentication mechanism
    # - Data format requirements
    # - Error handling expectations
```

**Demo:**
```
Implement sync_with_legacy_erp. The ERP system is our internal SAP instance.
```

**Expected Result:**
Agent will ask for clarification or make assumptions:
```python
import requests

def sync_with_legacy_erp(data: dict) -> bool:
    # Assumed endpoint - WILL NOT WORK
    response = requests.post(
        "https://erp.company.com/api/sync",
        json=data
    )
    return response.ok
```

**Problem:** Without documentation, agent cannot know the actual API.

### 3. Regulatory/Compliance Requirements

**Example Function:**
```python
def process_compliance_report(transactions: list[dict]) -> dict:
    """Generate compliance report per regulations."""
    # Agent doesn't know:
    # - Which regulations apply (GDPR? SOX? HIPAA?)
    # - Required report formats
    # - Data retention policies
    # - Audit requirements
```

**Demo:**
```
Implement process_compliance_report for our financial services company.
```

**Discussion:**
- What jurisdiction?
- What specific regulations?
- What reporting period?
- What audit trail requirements?

### 4. Subjective Design Decisions

**Example Function:**
```python
def design_dashboard_layout(metrics: list[dict]) -> dict:
    """Design metrics dashboard layout."""
    # Subjective choices:
    # - Metric grouping
    # - Visualization types
    # - Color schemes
    # - Priority ordering
```

**Demo:**
```
Design a dashboard layout for our analytics metrics.
```

**Expected Result:**
Agent makes arbitrary choices that may not match your preferences.

### 5. Specialized Domain Algorithms

**Example Function:**
```python
def calculate_insurance_premium(
    customer_age: int,
    risk_factors: list[str],
    coverage_amount: Decimal,
    policy_type: str,
) -> Decimal:
    """Calculate premium using actuarial models."""
```

**Demo:**
```
Implement calculate_insurance_premium using industry-standard actuarial models.
```

**Expected Result:**
Agent generates a simplified formula that doesn't match real actuarial science:
```python
# Simplified - NOT a real actuarial model
base_rate = Decimal("0.01")
age_factor = Decimal("1") + (customer_age - 25) * Decimal("0.02")
return coverage_amount * base_rate * age_factor
```

**Problem:** Real actuarial calculations require:
- Mortality tables
- Claims history data
- Regulatory rate requirements
- Company-specific models

## Demo Workflow

### Step 1: Ask Without Context
```
Implement all functions in domain_specific.py without asking questions.
Make reasonable assumptions where needed.
```

### Step 2: Review Assumptions
```
For each function you implemented, list the assumptions you made.
```

### Step 3: Discuss Reality
Compare agent's assumptions with reality:
- Are the customer tiers correct?
- Is the discount logic right?
- Would this pass compliance review?
- Does the formula match your actuarial models?

### Step 4: Provide Context
```
Now implement calculate_customer_discount with these rules:
- Tier "enterprise": 25% discount
- Tier "professional": 15% discount
- Tier "starter": 5% discount
- Accounts over 2 years old get additional 5%
- If account_balance > $10,000, additional 3%
- Maximum total discount is 30%
```

**Expected:** Much better implementation with clear requirements.

## When to Avoid AI Agents

| Task Type | Why Agents Struggle | Better Approach |
|-----------|---------------------|-----------------|
| Business rules | No domain knowledge | Document rules first |
| Internal APIs | No access to docs | Provide API specs |
| Compliance | Regulations vary | Consult legal/compliance |
| UI/UX design | Subjective | Design review with team |
| Algorithms | Domain expertise | Work with specialists |

## When to Use AI Agents Effectively

| Task Type | Why Agents Excel | Tips |
|-----------|------------------|------|
| Bug finding | Systematic analysis | Provide full context |
| Test writing | Pattern recognition | Clear specifications |
| Refactoring | Code transformation | Well-defined goals |
| Documentation | Language generation | Review for accuracy |
| Code review | Checklist evaluation | Defined standards |

## Key Takeaways

1. **Agents need context:** Business rules, API specs, requirements
2. **Agents make assumptions:** Always review for domain correctness
3. **Agents aren't domain experts:** They generate plausible, not correct code
4. **Provide specifications:** Clear requirements = better results
5. **Use for technical tasks:** Agents excel at well-defined coding tasks
6. **Review critically:** Never deploy business logic without human review
