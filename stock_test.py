from stock import Stock


def test_stock_is_empty():
    # Act
    stock = Stock()

    # Assert
    assert stock.is_empty() == False


def test_stock_return_count_of_0_by_default():
    stock = Stock()

    assert stock.count() == 0


# Answer its count of unique symbols (e.g. “IBM,” “AAPL”).
def test_stock_should_return_count_of_1_when_one_symbol_added():
    stock = Stock()

    stock.add_symbol("IBM")

    assert stock.count() == 1


def test_stock_should_return_count_of_1_when_same_symbol_added_twice():
    stock = Stock()
    stock.add_symbol("IBM")
    stock.add_symbol("IBM")
    assert stock.count() == 1

# Make a purchase, given a symbol and # of shares.
def test_purchase_plus_one():
    stock = Stock()
    stock.add_symbol("IBM")
    stock.purchaseNumber("IBM", 2)
    assert stock.calculate("IBM") == 2

#Make a sale, given a symbol and # of shares.
def test_sell_by_symbol():
    stock = Stock()
    stock.add_symbol("IBM")
    stock.purchaseNumber("IBM", 2)

    stock.sale("IBM", 1)

    assert stock.calculate("IBM") == 1





