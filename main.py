import streamlit as st
from st_files_connection import FilesConnection
from huggingface_hub import HfFileSystem
from json import JSONDecodeError
import pandas as pd

st.header('🤗 Spam Analysing tool')
conn = st.experimental_connection('hf', type=FilesConnection)
nrows = st.slider("Rows to retrieve", value=50)

datafile_path = 'datasets/Deysi/spam-detection-dataset/data/test-00000-of-00001-fa9b3e8ade89a333.parquet'


@st.cache_data(ttl=3600)
def load_data():
    kwargs = dict(ttl=3600)
    try:
        if datafile_path.endswith('.parquet'):
            data_dict = conn.read(datafile_path, **kwargs)
        else:
            data_dict = conn.read(datafile_path)
    except JSONDecodeError as e:
        # often times because a .json file is really .jsonl
        try:
            data_dict = conn.read(datafile_path, input_format='jsonl', **kwargs)
        except:
            raise e

    df = pd.DataFrame.from_dict(data_dict)
    return df


df = load_data()

Options = ["View All", "Spam", "Not Spam"]
select = st.selectbox("Select Spam or Not Spam", Options)
if select == "Spam":
    df_spam = df[df['label'] == 'spam']
    st.dataframe(df_spam.head(nrows), use_container_width=True)

elif select == "Not Spam":
    df_notspam = df[df['label'] == 'not_spam']
    st.dataframe(df_notspam.head(nrows), use_container_width=True)

elif select == "View All":    
    st.dataframe(df.head(nrows), use_container_width=True)

st.write("Unmasking the deceptive, revealing the genuine. Analyzing spam, one message at a time. - Siddharth Choudhury")
