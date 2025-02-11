import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from datetime import date

st.title("🔷 st.dataframe()")

st.divider()

st.write('''
- Display a dataframe as an interactive table
- This command works with a wide variety of collection-like and dataframe-like object types
''')

st.divider()

code = '''
df = pd.DataFrame(
    np.random.randn(6, 10),
    columns=[f"col {i}" for i in range(10)])
    
st.dataframe(df)  # Same as st.write(df)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    np.random.randn(6, 10),
    columns=[f"col {i}" for i in range(10)])

st.dataframe(df)  # Same as st.write(df)

st.divider()

code = '''
df = pd.DataFrame(
    np.random.randn(6, 9),
    columns=[f"col {i}" for i in range(9)])

st.dataframe(df.style.highlight_max(axis=0))
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    np.random.randn(6, 9),
    columns=[f"col {i}" for i in range(9)])

st.dataframe(df.style.highlight_max(axis=0))

st.divider()

code = '''
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "url": st.column_config.LinkColumn("App URL"),
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "url": st.column_config.LinkColumn("App URL"),
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.divider()

code = '''
df = pd.DataFrame(
    {
        "Date": [date(2024, 1, 1), date(2024, 2, 1), date(2024, 3, 1)],
        "Total": [13429, 23564, 23452],
    }
)
df.set_index("Date", inplace=True)

config = {
    "_index": st.column_config.DateColumn("Month", format="MMM YYYY"),
    "Total": st.column_config.NumberColumn("Total ($)"),
}

st.dataframe(df, column_config=config)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    {
        "Date": [date(2024, 1, 1), date(2024, 2, 1), date(2024, 3, 1)],
        "Total": [13429, 23564, 23452],
    }
)
df.set_index("Date", inplace=True)

config = {
    "_index": st.column_config.DateColumn("Month", format="MMM YYYY"),
    "Total": st.column_config.NumberColumn("Total ($)"),
}

st.dataframe(df, column_config=config)

st.divider()

code = '''
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
)

event.selection
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
)

st.write(event.selection)

st.divider()

code = '''
df1 = pd.DataFrame(
    np.random.randn(5, 6), columns=["col %d" % i for i in range(6)]
)

add_btn = st.button("Add Row")
my_spinner = st.spinner("Wait for it...", show_time=True)
my_chart = st.line_chart(df1)

if add_btn:
    with my_spinner:
        for i in range(6):
            time.sleep(2)
            df2 = pd.DataFrame(
                np.random.randn(1, 6), columns=["col %d" % i for i in range(6)]
            )
            my_chart.add_rows(df2)

    st.success("Done!")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df1 = pd.DataFrame(
    np.random.randn(5, 6), columns=["col %d" % i for i in range(6)]
)

add_btn = st.button("Add Row")
my_spinner = st.spinner("Wait for it...", show_time=True)
my_chart = st.line_chart(df1)

if add_btn:
    with my_spinner:
        for i in range(6):
            time.sleep(2)
            df2 = pd.DataFrame(
                np.random.randn(1, 6), columns=["col %d" % i for i in range(6)]
            )
            my_chart.add_rows(df2)

    st.success("Done!")
