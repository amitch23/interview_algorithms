"""
Ticket Sorting
Given an input of list of origin and destination cities,
sort the list to be an accurate itinerary

ticket = (SRC, DEST)

input = [(SFO, LAX), (JFK, SJC), (SJC, SFO)]

output = [(JFK, SJC), (SJC, SFO), (SFO, LAX)]
"""
#runtime: 2(O(n * m)) + O(n) + O(n^2)

def sort_tickets(input):

    ticket_dict = {}
    
    #Find unique occurances of city to find which tuple to start with
    #assign key value pairs to count so that dict looks like {'SFO': 2, 'JFK':1}
    for city in input:
        if city[0] not in ticket_dict:
            ticket_dict[city[0]] = 1
        else:
            ticket_dict[city[0]] += 1
            
        if city[1] not in ticket_dict:
            ticket_dict[city[1]] = 1
        else:
            ticket_dict[city[1]] += 1
        
    #Find the starting tuple    
    for pair in input:
 
       if ticket_dict[pair[0]] == 1:
           start = (pair[0], pair[1])
          
    results = [start]
    
    #check if first item in pair is equal to 2nd item in tuple 
    #if so, append the tuple to the results and update the start value to 
    #the next tuple
    while len(results) < len(input):
   
        for pair in input:
        
            if start[1] == pair[0]:    
                results.append(pair)
                start = pair
                