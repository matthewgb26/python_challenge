import os

import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')





with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    csv_header = next(csvreader)
    
    total_profit_losses = 0
    total_months = 0

    sum_profit_losses = 0

    greatest_increase = 0
    greatest_increase_month = ""

    greatest_decrease = 999999999999
    greatest_decrease_month = ""
   
    for row in csvreader:

     profit_losses = row[1]
     
     total_profit_losses = total_profit_losses + int(profit_losses)
     
     total_months = total_months + 1
     if total_months > 1:
            change = int(profit_losses) - int(last_profit_losses)

            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:
               greatest_increase = change
               greatest_increase_month = row[0]
 
            if change < greatest_decrease:
               greatest_decrease = change
               greatest_decrease_month = row[0]

     last_profit_losses = row[1]

print('Financial Analysis')
print('----------------------')

print(f'total months: {total_months}')
print(f'total: ${total_profit_losses}')

print(f'average change:${sum_profit_losses/(total_months-1):.2f}')



print(f'greatest increase: {greatest_increase_month} ${greatest_increase}')
print(f'greatest decrease: {greatest_decrease_month} ${greatest_decrease}')

output_path = os.path.join('..', 'PyBank', 'Analysis', 'analysis.txt')

with open(output_path, 'w') as txtfile:
    
        txtfile.write('Financial Analysis\n')
        txtfile.write('----------------------\n')
    
        txtfile.write(f'total months: {total_months}\n')
        txtfile.write(f'total: ${total_profit_losses}\n')
    
        txtfile.write(f'average change: ${sum_profit_losses/(total_months-1):.2f}\n')

    
        txtfile.write(f'greatest increase: {greatest_increase_month} ${greatest_increase}\n')
        txtfile.write(f'greatest decrease: {greatest_decrease_month} ${greatest_decrease}\n')
        
        
