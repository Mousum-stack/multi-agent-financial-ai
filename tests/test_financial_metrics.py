
from src.tools.financial_metrics import calculate_financial_metrics


def test_valid_financial_data():
    financial_data = {
        "revenue": 1000000,
        "net_income": 150000,
        "total_assets": 800000,
        "total_liabilities": 400000,
        "current_assets": 300000,
        "current_liabilities": 150000
    }

    result = calculate_financial_metrics(financial_data)

    assert result["net_profit_margin"] == 15.0
    assert result["debt_ratio"] == 50.0
    assert result["current_ratio"] == 2.0
