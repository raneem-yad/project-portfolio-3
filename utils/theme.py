class Colors:
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = "\u001b[0m"
    def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"
