import csv
import os

#---------------------------------------------------             
#Read the input file and analize the election data
#---------------------------------------------------

# Path to collect data from the Resources folder
csvpath=os.path.join ('Resources', 'election_data.csv')

## Declare variables to store data
voter_id=[]
county=[]
candidate=[]
Vote_num=[]
Percentage_vote=0.0
candidate_vote=0
Perc_vote=[]
dict_vote={}

#Read election_data.csv file
with open(csvpath) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=',')

    #Skip the header
    csv_header=next(csvreader)
    
    ##For each row in the file
    for row in csvreader:
        #Add Voter Id in a list
        voter_id.append(row[0])

        #Add County in a list
        county.append(row[1])

        #Add Candidates in a list
        candidate.append(row[2])

# use set to get Unique candidates  
output = set()
for x in candidate:
    output.add(x)

#sorted unique candidate list   
Unique_candidate=sorted(list(output))

#total number of candidates
Unique_list=len(Unique_candidate)

#Get total number of Votes
total_vote= len(voter_id)

#For each candidate
for y in range(Unique_list):

    #For each row, get the total vote for each candidate
    for index in range(total_vote):

        #check if candidate name match and add to total vote for that candidate
        if Unique_candidate[y]==candidate[index]:
            candidate_vote +=1

    #Calculate the total percentage Vote for each candidate  and add it to alist     
    Percentage_vote=round((candidate_vote/total_vote)*100,3)
    Perc_vote.append(Percentage_vote)

    #Add total vote for each candidate in a list
    Vote_num.append(candidate_vote)

    #Set the value of vote number and percentage vote value to zero for next candidate
    candidate_vote=0
    Percentage_vote=0.0

#Get the index of maximum vote
Maxindex= Vote_num.index(max(Vote_num))

#Create a dictionary to store Candidate name, Total votes and Percentage for each candidate
dict_vote={"candidate":Unique_candidate, "Vote": Vote_num, "PercentVote": Perc_vote }

#-----------------------------------             
#print the analysis to the terminal
#-----------------------------------

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_vote}')
print("-------------------------")
#Print the winner election data first
print(f'{dict_vote["candidate"][Maxindex]}: {dict_vote["PercentVote"][Maxindex]}% ({dict_vote["Vote"][Maxindex]})')
#Print rest of the candidate election data  
for z in range(Unique_list):
    if z != Maxindex:
        print(f'{dict_vote["candidate"][z]}: {dict_vote["PercentVote"][z]}% ({dict_vote["Vote"][z]})')
#Print Winner Name
print("-------------------------")
print(f'Winner: {dict_vote["candidate"][Maxindex]}')
print("-------------------------")

#-----------------------------------
#Write the analysis to the text file
#-----------------------------------

# Set variable for output file
output_file = os.path.join("analysis/Voter.txt")
#  Open the output file
datafile= open(output_file,"w")

# store the analysis to a list L1,L2 and L3 and write to datafile
L1=["Election Results\n",
"-------------------------\n",
(f'Total Votes: {total_vote}\n'), 
"-------------------------\n",
(f'{dict_vote["candidate"][Maxindex]}: {dict_vote["PercentVote"][Maxindex]}% ({dict_vote["Vote"][Maxindex]})\n')]

datafile.writelines(L1)

for z in range(Unique_list):
    if z != Maxindex:
        L2=[(f'{dict_vote["candidate"][z]}: {dict_vote["PercentVote"][z]}% ({dict_vote["Vote"][z]})\n')]
        datafile.writelines(L2)

L3=[
"-------------------------\n",
(f'Winner: {dict_vote["candidate"][Maxindex]}\n'), 
"-------------------------\n"]

datafile.writelines(L3)

#Close text file
datafile.close()