from prettytable import PrettyTable
table = PrettyTable() 
table.add_column("POKEMON NAME",["Pikachu","Squirtle","Charmander"]) 
table.add_column("TYPE",["Electric","Water","Fire"])
table.align = "r"
print(table)