e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

print("Словарь e2f:")
for eng, fra in e2f.items():
    print(f"{eng}/{fra}")

# Выводим французский вариант слова "walrus"
print("Французский вариант слова 'walrus':", e2f["walrus"])
