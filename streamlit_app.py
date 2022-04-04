import streamlit as st

st.header('**st.button**')
st.write('Allows the display of a button widget')

# Button Logic
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')