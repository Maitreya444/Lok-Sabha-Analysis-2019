import csv
import streamlit as st

def GetInfo(constituency):
    Affidavait = []
    with open('neta.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            if constituency.upper() in row[2].upper():
                Affidavait.append(row)
    return Affidavait

def main():
    st.set_page_config(page_title="Candidate Information Finder", page_icon="🔍", layout="wide")
    
    st.title("🔍 Candidate Information Finder")
    st.write("Enter your constituency to find information about candidates, including their party, criminal cases, education, total assets, and liabilities.")

    constituency = st.text_input("Enter your Constituency", placeholder="Type your constituency name here")
    
    if st.button("Search"):
        info = GetInfo(constituency)

        if info:
            st.success(f"Candidates and their background in {constituency}:")
            for iCnt in info:
                with st.expander(f"Candidate: {iCnt[1]}"):
                    col1, col2 = st.columns(2)
                    col1.write(f"**Party:** {iCnt[3]}")
                    col1.write(f"**Criminal Cases:** {iCnt[4]}")
                    col1.write(f"**Education:** {iCnt[5]}")
                    col2.write(f"**Total Assets:** {iCnt[6]}")
                    col2.write(f"**Liabilities:** {iCnt[7]}")
        else:
            st.error("No information found. Please check if you entered your constituency correctly.")

if __name__ == "__main__":
    main()
