
cost_per_system = float(input("What is the price per month for one VPS? "))
amount_of_servers = int(input("Amount of servers? "))
time_per_server = int(input("Amount of minutes per VPS (initial config)? "))
costs_administrator_per_hour = 84.00
total_costs = amount_of_servers * cost_per_system + amount_of_servers * (time_per_server/60) * costs_administrator_per_hour
print("Total costs: ", total_costs)

