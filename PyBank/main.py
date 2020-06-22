import csv
import os

#---------------------------------------------------             
#Read the input file and analize the budget data
#---------------------------------------------------

# Path to collect data from the Resources folder
csvpath=os.path.join ('Resources', 'budget_data.csv')

# Declare variables to store data
cdate = []
profit_loss = []
dict_change={}
Pchange= []
total=0

#Read budget_data.csv File
with open(csvpath) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=',')
    
    #Skip the header
    csv_header=next(csvreader)

    #For each row in the file
    for row in csvreader:
        # Add dates in a list
        cdate.append(row[0])

        # Add profit and loss in a list
        profit_loss.append(row[1])

        # Calculate Total amount and total month
        total += int(row[1])
        total_mon= len(cdate)

    #For loop to calculate the change in amount and store in a list   
    for index in range(total_mon-1):
            
        change= round(int(profit_loss[index+1]) -int(profit_loss[index]), 2)
        Pchange.append(change)

#Calculate Average change
average=round((sum(Pchange))/(total_mon-1),2)

# Get Max and Minimum change and the respective index
MaxChange= max(Pchange)
MinChange= min(Pchange)
Maxindex= Pchange.index(max(Pchange))
Minindex= Pchange.index(min(Pchange))

#Dictionary to store the date and corresponding profit-loss change 
dict_change= {"date":cdate, "dchange":Pchange}


#-----------------------------------             
#print the analysis to the terminal
#-----------------------------------
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {total_mon}")
print(f"Total: ${total}")
print(f"Average  Change: ${average}")
print(f'Greatest Increase in Profits: {dict_change["date"][Maxindex+1]} (${MaxChange})')
print(f'Greatest Decrease in Profits: {dict_change["date"][Minindex+1]} (${MinChange})')

#-----------------------------------
#Write the analysis to the text file
#-----------------------------------

# Set variable for output text file
output_file = os.path.join("analysis/Finance.txt")

# store the analysis to a list
L=["Financial Analysis \n",
"----------------------\n",
(f"Total Months: {total_mon}\n"), 
(f"Total: ${total}\n"),
(f"Average  Change: ${average}\n"),
(f'Greatest Increase in Profits: {dict_change["date"][Maxindex+1]} (${MaxChange})\n'),
(f'Greatest Decrease in Profits: {dict_change["date"][Minindex+1]} (${MinChange})')]

#  Open the output file
data_file= open(output_file,"w")

# write to the text file and close
data_file.writelines(L)
data_file.close()
