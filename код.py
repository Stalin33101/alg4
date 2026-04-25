class LinkShortener:
    def __init__(self):
        # прямой поиск: короткий код -> длинная ссылка
        self.short_to_long = {}
        # обратный поиск (пункт 10): длинная ссылка -> короткий код
        self.long_to_short = {}
        self.counter = 1  # для генерации коротких кодов

    def generate_code(self):
        #генерирует короткий код (просто число)
        code = str(self.counter)
        self.counter += 1
        return code

    def add_link(self, long_url):
        """добавляет новую ссылку"""
        # проверяем, существует ли уже такая длинная ссылка (пункт 10 поможет)
        if long_url in self.long_to_short:
            print("Такая ссылка уже есть, её код:", self.long_to_short[long_url])
            return self.long_to_short[long_url]
        
        # создаём новый короткий код
        short_code = self.generate_code()
        self.short_to_long[short_code] = long_url
        self.long_to_short[long_url] = short_code  # обратный поиск
        print("Добавлено:", short_code, "->", long_url)
        return short_code

    def get_long_url(self, short_code):
        """получает длинную ссылку по короткому коду"""
        if short_code in self.short_to_long:
            return self.short_to_long[short_code]
        else:
            return None

    def exists(self, short_code):
        """проверяет, существует ли короткий код"""
        return short_code in self.short_to_long

    def get_all_links(self):
        """выводит все сокращённые ссылки"""
        return self.short_to_long

    #ПУНКТ 10
    def find_by_long_url(self, long_url):
        #находит короткий код по длинной ссылке
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]
        else:
            return None



ls = LinkShortener()

ls.add_link("https://example.com/python")
ls.add_link("https://google.com")
ls.add_link("https://example.com/java")

print("\n--- Прямой поиск ---")
print("Код 1 ->", ls.get_long_url("1"))
print("Код 2 ->", ls.get_long_url("2"))
print("Существует ли код 5?", ls.exists("5"))

print("\nВсе ссылки")
print(ls.get_all_links())

print("\n ПУНКТ 10: обратный поиск")
print("Ищем код для https://google.com:", ls.find_by_long_url("https://google.com"))
print("Ищем код для https://yandex.ru:", ls.find_by_long_url("https://yandex.ru"))
