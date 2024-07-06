import streamlit as st
import pandas as pd
import plotly.express as px
from AI import generate_sql_query, execute_query

def main():
    st.set_page_config(
        page_title="SQL Database Visualization",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="auto"
    )
    st.markdown(
        """
        <style>
        .stTextArea > div:first-child {
            max-width: 50%; /* Decrease width */
        }
        .stSelectbox > div:first-child {
            max-width: 50%; /* Decrease width */
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-color: #1f77b4;
        }
        .stButton>button:hover {
            background-color: #2ca02c;
            color: white;
            border-color: #2ca02c;
        }
        .title {
            color: black;
        }
        .error-box {
            border: 1px solid red;
            padding: 10px;
            border-radius: 5px;
            background-color: #ffe6e6;
            color: red;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("SQL Database Query & Visualization through LLM")
    st.markdown(
        """
        Welcome to SQL Database Visualization 
        Enter a natural language query related to the database 
        """
    )
    user_input = st.text_area("Enter your query:")
    
    sql_query = None  
    chart_type = st.selectbox("Select chart type", ["Bar", "Line", "Area", "Pie"])

    if st.button("Execute", key="execute_query"):
        if user_input:
            sql_query = generate_sql_query(user_input)
            
            if sql_query.startswith("Error") or sql_query == "Please provide a query related to the database tables.":
                st.error(sql_query)
            else:
                st.write("SQL query :")
                st.write(sql_query)
                result, keys = execute_query(sql_query)
                
                if isinstance(result, str):
                    st.error(result)
                else:
                    df = pd.DataFrame(result, columns=keys)
                    
                    if df.empty:
                        st.warning("No data found for the query.")
                    else:
                        st.subheader("Query Result:")
                        st.dataframe(df)

                        try:
                            st.subheader("Chart:")
                            if chart_type == "Bar":
                                fig = px.bar(df, x=df.columns[0], y=df.columns[1:], title=f"{chart_type} Chart")
                            elif chart_type == "Line":
                                fig = px.line(df, x=df.columns[0], y=df.columns[1:], title=f"{chart_type} Chart")
                            elif chart_type == "Area":
                                fig = px.area(df, x=df.columns[0], y=df.columns[1:], title=f"{chart_type} Chart")
                            elif chart_type == "Pie":
                                fig = px.pie(df, names=df.columns[0], values=df.columns[1], title=f"{chart_type} Chart")
                            
                            if fig:
                                st.plotly_chart(fig, use_container_width=True, className='plotly-chart')
                        
                        except Exception as e:
                            st.markdown(
                                f'<div class="error-box">Cannot generate {chart_type} chart for the given query. Error: {str(e)}</div>',
                                unsafe_allow_html=True
                            )

if __name__ == "__main__":
    main()
