import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.line_chart()")

st.divider()

st.write('''
- Display a line chart''')

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.line_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.line_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()
