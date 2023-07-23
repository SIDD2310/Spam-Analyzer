# Spam Analyzing Tool using Streamlit

## Website: [https://hackathon.streamlit.app/](https://hackathon.streamlit.app/)
## Description
This is a web application built using Streamlit, a Python library for creating interactive web apps for data science and machine learning. The application is designed to analyze spam messages and provide insights into the dataset containing these messages.

## Getting Started
To run this application, you'll need to have the required dependencies installed. Make sure you have the following libraries installed in your Python environment:
- Streamlit
- Huggingface_hub
- Pandas

## How to Run
1. Save the code in a Python file, for example, `spam_analyzing_app.py`.
2. Run the application using Streamlit by executing the following command in your terminal or command prompt:
   ```
   streamlit run spam_analyzing_app.py
   ```
3. The application will start, and a link will be generated. Open the link in your web browser to access the Spam Analyzing Tool.

## Application Workflow
1. The application starts by importing the required libraries and establishing a connection to the Hugging Face model hub using `FilesConnection`.
2. It loads the data from a Parquet file named `test-00000-of-00001-fa9b3e8ade89a333.parquet` stored in the `datasets/Deysi/spam-detection-dataset/data/` directory.
3. The user can choose to view all the data or filter the dataset by selecting either "Spam" or "Not Spam" from the dropdown list.
4. The application displays the filtered data in a tabular format (dataframe) based on the user's selection.

## Caching Data
The application uses Streamlit's caching feature to improve performance. The `load_data` function is decorated with `@st.cache_data(ttl=3600)`, which means the data will be cached for an hour (3600 seconds). This prevents redundant data loading when the application is running.
