# question 2
open_file = open("CupcakeInvoices.csv")

# # question 3
for line in open_file:
    print(line)

# # question 4    
for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values[2])

# question 5
for line in open_file:
  values = line.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

# question 6
for line in open_file:
    values = line.split(",")
    total = total + int(values[3]) * float(values[4])

    print(total)

# question 7
open_file.close()