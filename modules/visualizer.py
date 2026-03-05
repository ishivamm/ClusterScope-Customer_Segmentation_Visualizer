import matplotlib.pyplot as plt
import streamlit as st
from sklearn.decomposition import PCA


class Visualizer:

    def plot_elbow(self, inertia):

        fig, ax = plt.subplots()

        ax.plot(range(1, len(inertia)+1), inertia, marker='o')
        ax.set_xlabel("Number of Clusters (K)")
        ax.set_ylabel("Inertia")
        ax.set_title("Elbow Method")

        st.pyplot(fig)


    def plot_clusters(self, data, labels):

        pca = PCA(n_components=2)
        reduced = pca.fit_transform(data)

        fig, ax = plt.subplots()

        scatter = ax.scatter(
            reduced[:,0],
            reduced[:,1],
            c=labels
        )

        ax.set_title("Customer Segmentation")
        ax.set_xlabel("PCA 1")
        ax.set_ylabel("PCA 2")

        st.pyplot(fig)