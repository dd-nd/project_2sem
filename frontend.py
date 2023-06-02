import tkinter as tk
from tkinter import messagebox
from main import get_content
from links import choose_catalog

# Функция для обработки события нажатия кнопки "Поиск"
def search():
    catalog = catalog_var.get()
    count = int(pages_entry.get())
    low_price = int(min_price_entry.get())
    top_price = int(max_price_entry.get())

    shard, query = choose_catalog(catalog_var.get())
    if shard == 'Не найден':
        messagebox.showerror("Ошибка", "Каталог не найден")
        return

    result = get_content(shard, query, count, low_price, top_price)
    result_text.delete(1.0, tk.END)  # Очистка поля с результатами
    for item in result:
        result_text.insert(tk.END, f'{item}\n')

    status_label.config(text="Сбор данных завершен.")
    save_results(result)

# Функция для сохранения результатов в файл
def save_results(data):
    with open("results.txt", "w", encoding="utf-8") as file:
        for item in data:
            file.write(f'{item}\n')

# Создание графического интерфейса
window = tk.Tk()
window.title("Парсер приложения")

# Выпадающее меню выбора каталога
catalog_label = tk.Label(window, text="Выберите каталог:")
catalog_label.pack()

catalog_var = tk.StringVar()
catalog_dropdown = tk.OptionMenu(window, catalog_var, "Здоровье", "Брюки", "Красота")
catalog_dropdown.pack()

# Поле ввода количества страниц
pages_label = tk.Label(window, text="Количество страниц (до 100):")
pages_label.pack()
pages_entry = tk.Entry(window)
pages_entry.pack()

# Поле ввода минимальной цены
min_price_label = tk.Label(window, text="Минимальная цена:")
min_price_label.pack()
min_price_entry = tk.Entry(window)
min_price_entry.pack()

# Поле ввода максимальной цены
max_price_label = tk.Label(window, text="Максимальная цена:")
max_price_label.pack()
max_price_entry = tk.Entry(window)
max_price_entry.pack()

# Кнопка "Поиск"
search_button = tk.Button(window, text="Поиск", command=search)
search_button.pack()

# Поле с результатами
result_text = tk.Text(window)
result_text.pack()

# Label для отображения статуса работы
status_label = tk.Label(window, text="", fg="green")
status_label.pack()

window.mainloop()