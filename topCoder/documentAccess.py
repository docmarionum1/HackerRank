def documentAccess(records, groups, rooms):
    access = set()
    for s in records:
        rec, room, group = s.split(' ')
        if room in rooms and group in groups:
            access.add(rec)
            
    return len(access)
    
documentAccess(
    ["diary computers editor","fairytale gardening editor","comix cars author","comix cars librarian"], 
    ["employee","editor","author", "librarian"], ["history","cars","computers"]
) #2

documentAccess(["a b c","a b d","b b c","b b d","e c d","e c b","e c c","t d e"], ["c","d","x"], ["a","b","c"]) #3