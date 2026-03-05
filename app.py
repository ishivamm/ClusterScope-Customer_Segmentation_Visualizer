import streamlit as st
import pandas as pd

from modules.clustering_engine import ClusteringEngine
from modules.data_handler import DataHandler
from modules.visualizer import Visualizer

st.set_page_config(
    page_title="ClusterScope",
    layout="wide"
)

st.title("ClusterScope - Customer Segmentation Visualizer")

data_handler = DataHandler()
cluster_engine = ClusteringEngine()
visualizer = Visualizer()


uploaded_file = st.file_uploader("Upload CSV", type=["csv"])


if uploaded_file:

    df = data_handler.load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    selected_features = st.multiselect(
        "Select features for clustering",
        numeric_columns
    )

    if len(selected_features) >= 2:

        scaled_data, original_data = data_handler.preprocess_data(
            df,
            selected_features
        )

        st.subheader("Elbow Method")

        inertia = cluster_engine.elbow_method(scaled_data)

        visualizer.plot_elbow(inertia)

        k = st.slider("Select number of clusters", 2, 10, 3)

        labels, model = cluster_engine.run_kmeans(scaled_data, k)

        score = cluster_engine.silhouette(scaled_data, labels)

        st.write("Silhouette Score:", round(score, 3))

        st.subheader("Cluster Visualization")

        visualizer.plot_clusters(scaled_data, labels)

        df["Cluster"] = labels

        st.subheader("Clustered Data")

        st.dataframe(df.head())

        csv = df.to_csv(index=False)

        st.download_button(
            "Download Clustered Data",
            csv,
            "clustered_data.csv",
            "text/csv"
        )