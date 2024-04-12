import datetime
from price_analysis import read_data, analyze_price_changes

def test_read_data(monkeypatch):
    # Використовуємо monkeypatch для заміни сьогоднішньої дати
    import datetime
    monkeypatch.setattr(datetime.date, 'today', lambda: datetime.date(2023, 4, 13))

    test_data = [
        ("Milk", "2023-03-10", "1.20"),
        ("Milk", "2023-04-10", "1.25"),
        ("Milk", "2023-04-12", "1.30")
    ]
    # Функція для мокування читання файлу
    def mock_open(*args, **kwargs):
        from io import StringIO
        content = '\n'.join([','.join(row) for row in test_data])
        return StringIO(content)

    monkeypatch.setattr("builtins.open", mock_open)
    
    results = read_data("dummy_path.txt", "Milk")
    assert results == [(datetime.date(2023, 4, 10), 1.25), (datetime.date(2023, 4, 12), 1.30)]

def test_analyze_price_changes():
    data = [(datetime.date(2023, 4, 10), 1.25), (datetime.date(2023, 4, 12), 1.30)]
    result = analyze_price_changes(data)
    assert result == {
        "start_price": 1.25,
        "end_price": 1.30,
        "price_change": 0.05
    }
