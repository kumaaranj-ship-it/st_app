import streamlit as st

st.title ("streamlit app")
st.header ("this is a header")

st.code("""
def hello_world():
        print ("hello world")
        return true
        """)

import pandas as pd

df = pd.DataFrame ({
                'Name': ['Alice', 'Bob' , 'Charlie'],
                'Age': [25, 30, 40],
                'City': ['Texas' , 'Kansan', 'Michigan']
                })
st.dataframe(df, use_container_width=True)

st.table(df)

st.metric(
    label="Temp",
    value="70 F",
    delta="1.2 F" 
)

edit_df=st.data_editor(    
    df,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=False
)

csv_data = "Name, Age\nAlice,25\nBob,30"

st.download_button(
label="Download CSV",
data=csv_data,
file_name="data.csv",
mime="text/csv"
)

genre = st.radio(
"Choose your favorite genre:",
["Comedy", "Drama", "Documentary"],
)

st.write(
f"You selected: {genre}"
)

option = st.selectbox(
"Choose a color:",
["Red", "Green", "Blue", "Yellow"],
index=0 # Default setection
)


options = st.multiselect(
"Choose your favorite fruits:",
["Select an option","Apple", "Banana", "Cherry", "Date"],
default=["Apple"] # Pre-selected options
)
# Range slider
values = st.slider(
"Select a raage:",
0.0, 100.0, (25.0, 75.0)
)
# Step slider
temp = st.slider("Temperature", -10, 40, 25, step=2)

name = st.text_input("Enter your name: ")

name = st.text_input(
"Enter your name:",
value="", # Default value
max_chars=50, # Character Limit
placeholder="John Doe",
type="password" # "default" or "password"
)

message = st.text_area(
"Enter your message:",
height=100,
max_chars=500,
placeholder="Type here ... "
)

number = st.number_input(
"Enter a number:",
min_value=0,
max_value=100,
value=50,
step=1
)

from datetime import date

selectdate=st.date_input(
    "Enter a date:",
    min_value=date(1957,1,1),
    max_value=date(2025,12,31),
    value=date.today()
)

uploaded_file = st.file_uploader(
"Choose a file:",
type=['csv', 'txt', 'pdf'],
accept_multiple_files=False
)

uploaded_files = st.file_uploader(
"Choose files:",
accept_multiple_files=True
)
