import csv 
def FetchInfo(name):
    Details = []
    try:
        with open('17_LS_MP_Track.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)  # Skip the header row
            
            # Iterate over each row to find matching MP name
            for row in csvreader:
                if len(row) > 1 and name.lower() in row[1].lower():
                    Details.append(row)
    except FileNotFoundError:
        print("Error: CSV file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    return Details

def main():
    name = input("Please enter your elected MP from 2019: ").strip()
    
    # Input validation to ensure a name is provided
    if not name:
        print("Invalid input. Please enter a valid MP name.")
        return
    
    output = FetchInfo(name)
    
    if output:
        print(f"Details of MP: '{name}':")
        for dest in output:
            print("Membership : ", dest[2] if len(dest) > 2 else "N/A")
            print("Term start date : ", dest[3] if len(dest) > 3 else "N/A")
            print("Term end : ", dest[4] if len(dest) > 4 else "N/A")
            print("Term : ", dest[5] if len(dest) > 5 else "N/A")
            print("Constituency : ", dest[6] if len(dest) > 6 else "N/A")
            print("State : ", dest[7] if len(dest) > 7 else "N/A")
            print("Party : ", dest[8] if len(dest) > 8 else "N/A")
            print("Gender : ", dest[9] if len(dest) > 9 else "N/A")
            print("Educational Qualifications : ", dest[10] if len(dest) > 10 else "N/A")
            print("Educational Qualifications Details : ", dest[11] if len(dest) > 11 else "N/A")
            print("Age : ", dest[12] if len(dest) > 12 else "N/A")
            print("Debates : ", dest[13] if len(dest) > 13 else "N/A")
            print("Private Member Bills : ", dest[14] if len(dest) > 14 else "N/A")
            print("Number of Questions : ", dest[15] if len(dest) > 15 else "N/A")
            print("Attendance : ", dest[16] if len(dest) > 16 else "N/A")
            print("------------")
    else:
        print(f"No data found for MP: {name}")

if __name__ == "__main__":
    main()
