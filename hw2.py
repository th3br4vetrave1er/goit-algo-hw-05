def generator_numbers(text: str):
    words = text.split()
    for word in words:
        if word.replace('.', '', 1).isdigit() and word.count('.') == 1:
            yield float(word)

def sum_profit(text: str, func) -> float:
    return sum(func(text))


text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов."
total_income = sum_profit(text, generator_numbers)
print(f"Общий доход: {total_income}")
