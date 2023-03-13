import csv
with open('playboys_playgirls.csv', mode='r') as csvfile:
    with open('playboys_and_playgirls_leaderboard.csv', mode='w') as new_csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        writer = csv.writer(new_csvfile)
        sortedlist = sorted(reader, key=lambda row: row[1], reverse=True)
        writer.writerow(['Name', 'Highest score']) 
        for row in sortedlist:
            writer.writerow(row)
        









    