import pytest
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


def test_zero_revenue():
    financial_data = {
        "revenue": 0,
        "net_income": 150000,
        "total_assets": 800000,
        "total_liabilities": 400000,
        "current_assets": 300000,
        "current_liabilities": 150000
    }

    with pytest.raises(ValueError, match="Revenue cannot be zero"):
        calculate_financial_metrics(financial_data)
        
def test_zero_total_assets():
    financial_data = {
        "revenue": 1000000,
        "net_income": 150000,
        "total_assets": 0,
        "total_liabilities": 400000,
        "current_assets": 300000,
        "current_liabilities": 150000
    }

    with pytest.raises(ValueError, match="Total assets cannot be zero"):
        calculate_financial_metrics(financial_data)
        
def test_zero_current_liabilities():
    financial_data = {
        "revenue": 1000000,
        "net_income": 150000,
        "total_assets": 800000,
        "total_liabilities": 400000,
        "current_assets": 300000,
        "current_liabilities": 0
    }

    with pytest.raises(ValueError, match="Current liabilities cannot be zero"):
        calculate_financial_metrics(financial_data)