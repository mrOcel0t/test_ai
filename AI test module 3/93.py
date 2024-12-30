import tkinter as tk

root = tk.Tk()

# Создаем 3x3 сетку из рамок
for i in range(3):
    for j in range(3):
        frame = tk.Frame(root, padx=10, pady=10)
        frame.grid(row=i, column=j)
        
        # Добавляем ярлык внутри каждой рамки
        label = tk.Label(frame, text=f"Рамка {i+1}x{j+1}")
        label.pack()

root.mainloop()