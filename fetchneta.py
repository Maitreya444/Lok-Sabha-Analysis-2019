import csv

def GetInfo(constituency):
    Affidavait = []
    with open ('neta.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            if constituency.upper() in row[2].upper():
                Affidavait.append(row)
    return Affidavait

def main():
    constituency = input("Enter your Constituency : ")
    info = GetInfo(constituency)

    if info:
        print("Candidates and their background in {}:".format(constituency))
        print(" ")

        for iCnt in info:
            print("Candidate: ", iCnt[1])
            print("Party : ", iCnt[3])
            print("Criminal Cases : ", iCnt[4])
            print("Education : ", iCnt[5])
            print("Total Assets : ", iCnt[6])
            print("Liabilities : ", iCnt[7])
            print(" ")

    else:
        print("Please check if you entered your constituency correct or not?")


if __name__ =="__main__":
    main()