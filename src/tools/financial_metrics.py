
def calculate_financial_metrics(financial_data: dict) -> dict:
    """
    Calculate basic financial ratios from company financial data.
    """

    required_fields = [
        "revenue",
        "net_income",
        "total_assets",
        "total_liabilities",
        "current_assets",
        "current_liabilities"
    ]

    # Validate required fields
    for field in required_fields:
        if field not in financial_data:
            raise ValueError(f"Missing required field: {field}")

    # Extract values
    revenue = financial_data["revenue"]
    net_income = financial_data["net_income"]
    total_assets = financial_data["total_assets"]
    total_liabilities = financial_data["total_liabilities"]
    current_assets = financial_data["current_assets"]
    current_liabilities = financial_data["current_liabilities"]

    # Validate numeric values
    for field, value in financial_data.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{field} must be a numeric value")

    # Validate denominators
    if revenue == 0:
        raise ValueError("Revenue cannot be zero")

    if total_assets == 0:
        raise ValueError("Total assets cannot be zero")

    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero")

    # Calculate financial metrics
    metrics = {
        "net_profit_margin": (net_income / revenue) * 100,
        "debt_ratio": (total_liabilities / total_assets) * 100,
        "current_ratio": current_assets / current_liabilities
    }

    return metrics

if __name__ == "__main__":
    financial_data = {
        "revenue": 1000000,
        "net_income": 150000,
        "total_assets": 800000,
        "total_liabilities": 400000,
        "current_assets": 300000,
        "current_liabilities": 150000
    }

    results = calculate_financial_metrics(financial_data)

    print("Financial Metrics:")
    for metric, value in results.items():
        print(f"{metric}: {value:.2f}")