class QuoteModel:
    def __init__(self, quote, name):
        self.quote = quote
        self.name = name
    
    def __repr__(self):
        return f"<{self.quote}, {self.name}>"
        