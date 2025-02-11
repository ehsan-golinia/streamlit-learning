import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.bar_chart()")

st.divider()

st.write('''
- Display a bar chart
''')

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")

st.divider()

code = '''import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": np.random.randn(20),
        "col3": np.random.randn(20),
    }
)

st.bar_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": np.random.randn(20),
        "col3": np.random.randn(20),
    }
)

st.bar_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()

code = '''import streamlit as st
from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

source = data.barley()

st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)

st.divider()

code = '''import streamlit as st
from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)