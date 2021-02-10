# Empty project for kata

only pytest in deps

## How to setup environment

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
``` 

## Tips

### Parametrized tests
```python
@pytest.mark.parametrize("test_input, expected", [
    ("Bob", "Hello, Bob.")
])
def test(test_input, expected):
    pass
```

### How to handle exceptions
```python

def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```
