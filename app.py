import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Enzyme & Metabolic Reaction Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Enzyme & Metabolic Reaction Analyzer")

csv_file = "metxbiodb.csv"
df = pd.read_csv(csv_file)

st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Select a module",
    [
        "Dashboard",
        "Enzyme Analysis",
        "Reaction Analysis",
        "Substrate Search",
        "Enzyme Search"
    ]
)

if option == "Dashboard":
    st.header("📊 Dataset Dashboard")

    st.metric("Total Records", len(df))

    st.metric(
        "Columns",
        len(df.columns)
    )

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), width="stretch")

elif option == "Enzyme Analysis":
    st.header("🧪 Enzyme Analysis")

    if "enzyme" in df.columns:
        counts = df["enzyme"].value_counts().head(10)
        st.bar_chart(counts)
        st.dataframe(counts.rename("Number of Reactions"))
    else:
        st.error("The dataset does not contain an enzyme column.")

elif option == "Reaction Analysis":
    st.header("⚗️ Reaction Analysis")

    if "reaction_type" in df.columns:
        counts = df["reaction_type"].value_counts().head(10)
        st.bar_chart(counts)
        st.dataframe(counts.rename("Number of Reactions"))
    else:
        st.error("The dataset does not contain a reaction_type column.")

elif option == "Substrate Search":
    st.header("🔎 Substrate Search")

    if "substrate_name" in df.columns:
        search = st.text_input("Enter substrate name")

        if search:
            results = df[
                df["substrate_name"].astype(str).str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

            st.write("Results found:", len(results))
            st.dataframe(results, width="stretch")
    else:
        st.error("The dataset does not contain a substrate_name column.")

elif option == "Enzyme Search":
    st.header("🔬 Enzyme Search")

    if "enzyme" in df.columns:
        search = st.text_input("Enter enzyme name")

        if search:
            results = df[
                df["enzyme"].astype(str).str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

            st.write("Results found:", len(results))
            st.dataframe(results, width="stretch")
    else:
        st.error("The dataset does not contain an enzyme column.")
