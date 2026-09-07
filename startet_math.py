"""A small reusable module for trade calculations."""


class InvalidTradeError(Exception):
    """Raised when a trade fails business-rule validation."""


def trade_value(quantity: float, price: float) -> float:
    """Return quantity multiplied by price after validation."""
    if quantity <= 0:
        raise InvalidTradeError(
            f"quantity must be positive, got {quantity}"
        )

    if price <= 0:
        raise InvalidTradeError(
            f"price must be positive, got {price}"
        )

    return quantity * price


def classify_trade(value: float, threshold: float = 20000) -> str:
    """Return 'large' if value exceeds threshold, otherwise 'normal'."""
    return "large" if value > threshold else "normal"


def safe_trade_value(trade: dict) -> float:
    """Return trade value and add trade_id to validation errors."""
    try:
        return trade_value(trade["quantity"], trade["price"])
    except InvalidTradeError as e:
        raise InvalidTradeError(
            f"{trade['trade_id']}: {e}"
        ) from e


if __name__ == "__main__":
    print(trade_value(120, 185.32))
