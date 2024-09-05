class PagingModel:
    def __init__(self, items, current_page, page_size=6):
        self.items = items
        self.current_page = int(current_page)
        self.page_size = page_size

    @property
    def count_pages(self):
        total_items = self.items.count()
        return (total_items + self.page_size - 1) // self.page_size

    def generate_url(self, page_num):
        return f"?page={page_num}"