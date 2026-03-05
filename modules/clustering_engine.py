from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class ClusteringEngine:

    def elbow_method(self, data, max_k=10):

        inertia = []

        for k in range(1, max_k + 1):
            model = KMeans(n_clusters=k, random_state=42)
            model.fit(data)
            inertia.append(model.inertia_)

        return inertia


    def run_kmeans(self, data, k):

        model = KMeans(n_clusters=k, random_state=42)
        labels = model.fit_predict(data)

        return labels, model


    def silhouette(self, data, labels):

        if len(set(labels)) > 1:
            score = silhouette_score(data, labels)
        else:
            score = -1

        return score