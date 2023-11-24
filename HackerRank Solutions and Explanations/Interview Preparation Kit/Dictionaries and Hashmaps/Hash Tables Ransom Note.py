def checkMagazine(magazine, note):
    import collections
    magazine_dict = collections.Counter(magazine)
    note_dict = collections.Counter(note)
    for note in note_dict:
        if note not in magazine_dict or magazine_dict[note]<note_dict[note]:
            print("No")
            return
    
    print("Yes")
        