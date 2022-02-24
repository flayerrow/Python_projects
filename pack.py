from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name", ["diwakar", "shubham", "piyush"])
table.add_column("type", ["water", "fire", "gas"])
table.align
print(table)
