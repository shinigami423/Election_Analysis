# Election Analysis

## Purpose
Seth and Tom asks for the submission for the election audit results and complete the additional data requested by the election commission. The additional information includes the voter turnout for each county, the percentage of votes from each county out of the total count, and report the county with th ehighest turnout.

## Analysis and Challenges
### Dependencies
There are two denpendencies for our program.The first is the **_csv_** import necessary for us to read the csv file provided by the commission. Second, we have to import the **_os_** to manipulate the paths in order to open and write/print out results in a text file.

### Execution 
Within the program, we initialize our variables and set them to integer 0 and empty strings. We also created empty lists and dictionarys so we can systematically loop to check/print our election results and county turnout and votes. 

The for loops embeded in the first _with_ operation are used to add candidate/county options to our lists and assign their respective vote counts. And print out the candidate/county and their vote counts respectively as long as they are in the lists and dictionarys.

Finally, we embedded in the for loops a _.write_ command to print trhe results onto the text file.

### Results
After executing the program, we have the printed results on the terminal showing the electrion results including:
- total votes
- county votes and it's percentages
- declaration of largest county turnout
- candidate votes and it's percentages
- winner of the election

### Challenges and Difficulties Encountered
The overall challenge is fairly straight foward and counting county and their votes instead of the candidates and their votes. There were some struggles using the _os.path.join_ command when loading the file but eventuallys resolved.

## Summary
Election results are printed on the text files name election_analysis.txt, printing the outcomes the same outline as was printed on the terminal. The largest county turnout is Denver and the winning candidate is Diana DeGette.

### Pros and Cons
The major pro to this program is the use of csv file and the ability to read all the rows and assigning new candidates/counties that are not in the list. This is significant as we can use data sets that contain more lines(votes in this case) and display the results without changing our codes. This program can be used as long as the file we are trying to read is a _csv file_ and is columned by "Ballot ID""County""Candidate.
"

The only con I forsee is unfortunately an issue with _csv_. The program can only read csv files and only if the columns are in the apporpriate order, as discussed above.