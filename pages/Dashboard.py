import streamlit as st
from Modules import VisualHandler
import pandas as pd
def take_data(file):
    df = pd.read_excel(file)
    return df
VisualHandler.initial()
def display_dasboard():
    if st.session_state.log == True:
        col1, col2, col3 = st.columns(3)
        col1.metric("Student", "1250", "1.2%", border = True)
        col2.metric("Teachers", "50", "-8%", border = True)
        col3.metric("Earning", "$240000", "5%", border = True)

        st.divider()
        st.subheader("Top Student")
        st.dataframe(take_data('top_20_students.xlsx'))
    else:
        st.warning("Please log in to continue")
display_dasboard()