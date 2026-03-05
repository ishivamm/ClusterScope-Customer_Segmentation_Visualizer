# ClusterScope: Customer Segmentation Visualizer

ClusterScope is an interactive data science web application that enables users to perform **customer segmentation using K-Means clustering**. The application allows users to upload customer datasets, determine the optimal number of clusters using the **Elbow Method**, evaluate clustering quality with the **Silhouette Score**, and visualize customer segments through interactive plots.

The project demonstrates an end-to-end **unsupervised machine learning workflow**, including data preprocessing, clustering, model evaluation, and visualization using a Streamlit-based interface.

## Youtube link: https://youtu.be/Xr95QW54nvc \
## Live App:https://clusterscope-customersegmentationvisualizer-dxrwmnzbkspugm4jky.streamlit.app/
---

# Project Overview

Customer segmentation is widely used in retail, e-commerce, and marketing to identify groups of customers with similar behaviors. Businesses can use these insights to create targeted marketing strategies, improve customer retention, and optimize product offerings.

ClusterScope provides an easy-to-use interface where users can:

• Upload a customer dataset
• Select features for clustering
• Determine the optimal number of clusters
• Run K-Means clustering
• Visualize clusters in 2D using PCA
• Evaluate clustering performance with Silhouette Score
• Download clustered results

---

# Features

**1. Data Upload**

* Upload customer dataset in CSV format
* Preview dataset directly in the application

**2. Feature Selection**

* Select relevant numeric features for clustering

**3. Elbow Method Visualization**

* Automatically compute inertia values for different K values
* Plot Elbow curve to help determine optimal clusters

**4. K-Means Clustering**

* Apply K-Means clustering using scikit-learn
* Assign cluster labels to customers

**5. Cluster Visualization**

* Dimensionality reduction using PCA
* Scatter plot visualization of customer clusters

**6. Silhouette Score Evaluation**

* Measure clustering quality

**7. Download Results**

* Export clustered dataset as CSV

---

# Project Architecture

The application follows a modular architecture separating responsibilities across different components.

```
ClusterScope/
│
├── app.py
│
├── modules/
│   ├── clustering_engine.py
│   ├── data_handler.py
│   └── visualizer.py
│
├── data/
│   └── sample_customers.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Module Responsibilities

**app.py**
Main Streamlit application controlling the workflow.

**data_handler.py**
Handles data loading, cleaning, and preprocessing.

**clustering_engine.py**
Implements machine learning logic including:

* Elbow Method
* K-Means clustering
* Silhouette Score evaluation

**visualizer.py**
Generates visualizations for:

* Elbow curve
* Cluster scatter plots

---

# Technology Stack

Programming Language
Python

Framework
Streamlit

Machine Learning
scikit-learn

Data Processing
pandas, numpy

Visualization
matplotlib, seaborn

Dimensionality Reduction
PCA (Principal Component Analysis)

---

# Installation

Clone the repository:

```
git clone https://github.com/ishivamm/ClusterScope-Customer_Segmentation_Visualizer.git
cd ClusterScope-Customer_Segmentation_Visualizer
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---



# Workflow

1. Upload CSV dataset
2. Select clustering features
3. Generate Elbow Method plot
4. Choose number of clusters
5. Run K-Means clustering
6. Visualize clusters
7. Evaluate with Silhouette Score
8. Download results

---

# Use Cases

• Retail customer segmentation
• Marketing analytics
• Customer behavior analysis
• Educational demonstrations of clustering algorithms
• Rapid prototyping of segmentation models

---



# License

This project is open-source and available under the MIT License.

---


