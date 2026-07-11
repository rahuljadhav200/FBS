#Q.2 Convert the time entered in hh, min, and sec into seconds

hours=int(input("Enter hours:"))
min=int(input("Enter minutes:"))
sec=int(input("Enter seconds:"))
second =(hours*3600) + (min*60) + sec
print("Total time in seconds is :",second)