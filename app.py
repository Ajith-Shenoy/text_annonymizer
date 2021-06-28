# Core packages
import streamlit as st
import os


def main():

    st.title("Document Redactor")
    st.text("Built with Streamlit and SpaCy")
    choices = ['Redact', 'About']
    choice = st.sidebar.selectbox('Please Select', choices)

    if choice == 'Redact':
        st.subheader('Preserving privacy by text redaction')
        raw_text = st.text_area('Enter Text to Redact', 'type here')
        redaction_items = ['Name', 'Places', 'Dates', 'Organization']
        redaction_choice = st.selectbox(
            'Pick Elements to be Censored', redaction_items)
        save_choice = st.radio(
            'Save the redacted file?', ("Yes", "No"))

    elif choice == 'About':
        st.subheader('About the project')


if __name__ == '__main__':
    main()
