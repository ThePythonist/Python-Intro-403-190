bank_mellat = {
    "type": "private",
    "symbol": "BMLT1",
    "industry": "financial",
    "shareholder": {
        "دولت جمهوری اسلامی ایران": 11.16,
        "سرمایه گذاری‌های استانی": 11.16,
        "بازارگردانی ملت": 8.54,
        "سهامداران حقیقی": 11.25
    },
}

info = {
    "subsidiaries": ["بانکداری ایران", "فرهنگی ورزشی پرسپولیس"],
    "foundation": 1980,
}

bank_mellat.update(info)

print(bank_mellat)

# print(bank_mellat["symbol"])
# print(bank_mellat["shareholder"])
# print(bank_mellat["shareholder"]["بازارگردانی ملت"])

# print(bank_mellat.keys())
# print(bank_mellat.values())
# print(bank_mellat.items())
