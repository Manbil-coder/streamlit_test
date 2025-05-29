import streamlit as st 
import requests

# Set the app title 
st.title('Selamat datang') 

# Add a welcome message 
st.write('Selamat datang ke aplikasi streamlit saya') 

# Create a text input 
widgetuser_input = st.text_input('Masukkan custom mesej:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)


#API calls
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    st.write('Output:')
    st.json(data)  # nicely formatted JSON output
else:
    st.error(f"API call failed with status code: {response.status_code}")


