#counties = ["Arapahoe","Denver","Jefferson"]
#if "Arapahoe" in counties or "El  Paso" in counties:
    #print("Arapahoe or El Paso are in the list of counties")
#else:
    #print("Arapahoe and El Paso is not the list of counties")

    #for i in range(len(counties)):
  #  print(counties[i])


#------------------------------------------------------------------------------------------

#counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}

#for county,voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")


#------------------------------------------------------------------------------------------
#voting_data = [{"county":"Arapahoe","registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict['county'])


#------------------------------------------------------------------------------------------
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)