from tabulate import tabulate

class TablesDrawing: 
    def __init__(self, columns, headers,style = "grid",indexed =False):
        self.columns =columns
        self.headers = headers
        self.style = style 
        self.indexed = indexed
        
    def print_table(self):
        return tabulate(self.columns, headers= self.headers, tablefmt=self.style, showindex= self.indexed)
    

def create_columns(*columns): 
    # [[x, y, z] for x, y, z in zip(a, b, c)]
    return [list(column) for column in zip(*columns)]