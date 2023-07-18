import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = {}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0


    for row in csvreader:
            total_votes += 1
    
    
            if row[2] in candidates:
                candidates[row[2]] += 1

            else:
                candidates[row[2]] = 1

            

print('Election Results')
print('----------------------')

print(f'total votes: {total_votes}')

print('----------------------')

for candidate in candidates:
    print(f'{candidate}: {candidates[candidate]/total_votes*100:.2f}% ({candidates[candidate]})')

print('----------------------')

winner = ""
winner_votes = 0

for candidate in candidates:
    if candidates[candidate] > winner_votes:
        winner_votes = candidates[candidate]
        winner = candidate

print(f'winner: {winner}')

print('----------------------')

output_path = os.path.join('Analysis', 'election_results.txt')

with open(output_path, 'w') as txtfile:
     

    txtfile.write('Election Results\n')
    txtfile.write('----------------------\n')

    txtfile.write(f'total votes: {total_votes}\n')

    txtfile.write('----------------------\n')

    for candidate in candidates:
        txtfile.write(f'{candidate}: {candidates[candidate]/total_votes*100:.2f}% ({candidates[candidate]})\n')

    txtfile.write('----------------------\n')

    txtfile.write(f'winner: {winner}\n')

    txtfile.write('----------------------\n')