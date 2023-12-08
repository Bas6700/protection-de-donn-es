import pandas as pd
import plotly.express as px
import streamlit as st


encodings = ["utf-8", "utf-16", "utf-32", "ascii", "us-ascii", "latin-1", "cp1252"]
separators = {
    "comma": ",",
    "semicolon": ";",
    "tab": "\t",
    "pipe": "|",
    "space": " ",
    "hyphen": "-",
    "underscore": "_",
    "dot": ".",
}
plot_types = {
    "line": px.line,
    "scatter": px.scatter,
    "bar": px.bar,
    "box": px.box,
    "violin": px.violin,
    "histogram": px.histogram,
    "pie": px.pie,
    "sunburst": px.sunburst,
    "treemap": px.treemap,
    "funnel": px.funnel,
}

encoding = encodings[0]
separator = separators["comma"]


def main():
    st.title("Data Visualization")

    # add a menu for encoding and separator
    st.sidebar.subheader("File Encoding")
    encoding = st.sidebar.selectbox("Select a file encoding", encodings)
    st.sidebar.subheader("Separator")
    separator = st.sidebar.selectbox("Select a separator", list(separators.keys()))

    st.subheader("Select a csv file to visualize")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        st.success("File successfully uploaded")
        df = pd.read_csv(file, sep=separators[separator], encoding=encoding)
        st.dataframe(df)
        st.subheader("Select columns to plot")
        columns = df.columns.tolist()
        x_axis = st.selectbox("X axis", columns)
        y_axis = st.selectbox("Y axis", columns)
        plot_type = st.selectbox(
            "Plot Type", list(plot_types.keys()), index=0, key="plot_type"
        )
        if st.button("Generate Plot"):
            st.success("Generating Plot")
            fig = plot_types[plot_type](df, x=x_axis, y=y_axis)
            st.plotly_chart(fig)
    else:
        st.warning("Please upload a csv file")


if __name__ == "__main__":
    main()