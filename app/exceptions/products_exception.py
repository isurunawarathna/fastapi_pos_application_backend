class DuplicateProductCode(Exception):
    def __init__(self, message):
        super().__init__(message)

class ProductCategoryInActive(Exception):
    def __init__(self, message):
        super().__init__(message)
