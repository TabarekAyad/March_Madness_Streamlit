import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


st.title("NCAA March Madness")
st.write("# Using Streamlit to build a website showing visualizations of NCAA March Madness using  ")

with st.expander('About Streamlit'):
     st.markdown(
                """
                Streamlit is a free and open-source Python library that allows you to rapidly build and share beautiful machine learning and data science web apps¹². It's designed specifically for data scientists and machine learning engineers². 

                With Streamlit, you can create stunning-looking applications with only a few lines of code¹². It's especially useful for people with no front-end knowledge as it requires no experience with HTML, JavaScript, or CSS². 

                Streamlit allows you to build an app in a few lines of code with its simple API¹. You can add widgets, which is as simple as declaring a variable¹. It also allows you to deploy your apps directly from Streamlit, making it easy to share, manage, and deploy your apps¹.

                It's compatible with the majority of Python libraries (e.g., pandas, matplotlib, seaborn, plotly, Keras, PyTorch, SymPy (latex))². This makes it a powerful tool for creating interactive web applications for machine learning and data science⁴.

                Source:\n
                (1) Streamlit • A faster way to build and share data apps. https://streamlit.io/.\n
                (2) Python Tutorial: Streamlit | DataCamp. https://www.datacamp.com/tutorial/streamlit.\n
                (3) Streamlit in 3 Minutes. Streamlit is an open-source Python… | by .... https://medium.com/data-and-beyond/streamlit-d357935b9c.\n
                (4) Streamlit documentation. https://main--streamlit-docs.netlify.app/.\n


                ### Want to learn how to use it?

                - Check out [streamlit.io](https://streamlit.io)
                - Jump into the [documentation](https://docs.streamlit.io)
                - Ask a question in their [community
                forums](https://discuss.streamlit.io)


            """
            )
     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)


# Add the caching decorator
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

# Load the data CSV file
NCAA = load_data("data/NCAA.csv")

# Load the names CSV file
NCAA_names = load_data("data/NCAA_names.csv")


with st.expander('The data used'):
     st.dataframe(NCAA)
     st.dataframe(NCAA_names)