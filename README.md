# Election Analysis

## Purpose
Seth and Tom request for the election audit results and the completion of additional data requested by the election commission. Other than finding out the winning candidate of the election, the commission asks for the voter turnout for each county, the percentage of votes from each county out of the total count, and report the county with the highest turnout.

## Analysis and Challenges
### Dependencies
There are two denpendencies for our program.The first is the **_csv_** import necessary for us to read the csv file provided by the commission. Second, we have to import the **_os_** to manipulate the paths in order to open and save our results in a text file. (below)

```python:PyPoll_Challenge.py [6,8]
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

### Execution 
Within the program, we initialize our variables and set them to integer 0 and empty strings. We also created empty lists and dictionaries so we can systematically loop to check/print our election results and county turnout and votes. For example, for the county variables:

```python:PyPoll_Challenge.py [18-19]
county_options = []
county_votes = {}
```

The loops embeded in the first _with_ operation are used to add candidate/county options to our lists and increase their respective vote counts as long as the county does not exist in the the list. **below**

```python:PyPoll_Challenge.py [67-74]
if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```

Next we use with **with** command to open a text file we want to save our results. Below are codes we used to print the respective results:

```python:PyPoll_Challenge.py [81-87,111-117,144-150]
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
------------------------------------------------

largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}"
        f"\n-------------------------\n"
    )
    print(largest_county_turnout)
------------------------------------------------
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```


Finally, we inserted within for loops a _.write_ command to print the results on the text file named _election_analysis.txt_.

```python:PyPoll_Challenge.py [89]
txt_file.write(election_results)
```

**example code shown saves the result to the file named election_results.txt**

### Results
When we execute the program, it printed the election results on the terminal saved them on election_analysis.txt. Results are as follows in the election_analysis.txt:

```text file: analysis/election_analysis.txt

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```
Above printed results contains the following:
- **Total votes**
- **County votes and their vote percentages**
- **The Largest county turnout for the election**
- **Candidate votes and their percentages**
- **Winner of the election, their vote count, and the percentage vote received**

### Challenges and Difficulties Encountered
The overall challenge is fairly straight foward, similiar to the module exercices, counting county by votes instead of the candidates by their votes. There were some hiccups using the _os.path.join_ command when loading the file but eventually resolved.

## For the election commission! The election results are as follows:
- The total vote count is 369,711.
- The county vote counts:
	- Jefferson county at 10.5% of total votes with 38,855 votes
	- Denver at 82.8% of total votes with 306,055 votes
 	- Arapahoe at 6.7% of total votes with 24,801 votes
- The largest county turnout is Denver county.
- The candidate vote counts:
	- Charles Casper Stockham at 23.0% of total votes with 85,213 votes
	- Diana DeGette at 73.8%  of total votes with 272,892 votes
	- Raymon Anthony Doane at 3.1% of total votes with 11,606 votes
- The winning candidate is Diana DeGette at 73.8% of total vote with 272,892 votes


### Pros and Cons of this program
The major pro to this program is the use of csv file and the ability to read all the rows and assigning new candidates/counties that are not in our variable lists/dictionaries. This is significant as we can use data sets that contain more lines(votes in this case) and display the results without changing our codes. This program can be used as long as the file we are trying to read is a _csv file_ and is columned by "Ballot ID","County","Candidate."

The only con I forsee is unfortunately an issue with _csv_. The program can only read csv files and only if the columns are in the apporpriate order, since we assigned the variables to very specific columns in the file.

### Other uses for the program
As addressed above on under Pros and Cons, the program can be utlized for any numbers of candidates and their counties as long as the csv file contains commas seperating the values in the order of "Ballot ID","County","Candidate."
