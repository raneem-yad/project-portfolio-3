from utils import Colors
from utils import Message
from tabulate import tabulate

# make table by string
# ome_data = [['08:01', 1.00, 32], ['08:02', 1.01, 33], ['08:03', 1.02, 33]]
# h = ['Time', 'x', 'n']

# print('{:<10s} {:<5s} {:<5s}'.format(*h))
# for list_ in some_data:
#     print('{:<10s} {:.2f} {:<5d}'.format(*list_))

# make lines around the table



main_page_messages = [
    ["Login\n", 1],
    ["Create Account\n", 2],
    ["App preview\n", 3]
]
# Table headers
headers = [ "How we can Help you", "Press"]

# Print the table



def main():
    print(Colors.UNDERLINE+Colors.BOLD+Colors.RED + "\n Welcome to TaskTracker App!\n" + Colors.RESET)
    # print(tabulate(main_page_messages, headers=headers, tablefmt="grid",showindex="always"))
    print(tabulate(main_page_messages, headers=headers, tablefmt="grid"))


main()
