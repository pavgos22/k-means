# K-means Clustering Implementation

This project implements the K-means clustering algorithm, including both the standard initialization (Forgy method) and the K-means++ initialization. The implementation is tested on the Iris dataset to evaluate the clustering performance.

## Project Structure

- **Main Functions**:
  - **load_iris**: Loads the Iris dataset from a CSV file and returns the features and labels.
  - **evaluate**: Evaluates and prints the composition of each cluster by counting how many samples of each class are present in each cluster.
  - **clustering**: Main function that runs the K-means algorithm multiple times, evaluates the clusters, and calculates the mean intra-class variance.

- **K-means Algorithm (`k_means.py`)**:
  - **calculate_distance**: Computes the Euclidean distance between two points.
  - **initialize_centroids_forgy**: Implements the Forgy method for randomly initializing the centroids by selecting `k` data points from the dataset.
  - **initialize_centroids_kmeans_pp**: Implements the K-means++ initialization, which selects the first centroid randomly and then selects subsequent centroids to be as far away as possible from the existing centroids.
  - **assign_to_cluster**: Assigns each data point to the nearest centroid.
  - **update_centroids**: Updates the centroid positions by calculating the mean of all data points assigned to each centroid.
  - **mean_intra_distance**: Computes the mean intra-cluster distance, which is used as a measure of cluster compactness.
  - **k_means**: The main K-means algorithm that iteratively assigns data points to clusters and updates centroids until convergence or a maximum number of iterations is reached.

## How It Works

### K-means Clustering
K-means is an unsupervised machine learning algorithm used for clustering data into a specified number of clusters. The algorithm works by:

1. **Initialization**: 
   - **Forgy Method**: Centroids are initialized by randomly selecting `k` data points.
   - **K-means++**: The first centroid is chosen randomly, and subsequent centroids are selected to be as far away as possible from the existing centroids, reducing the likelihood of poor clustering results.

2. **Assignment**:
   - Each data point is assigned to the nearest centroid based on the Euclidean distance.

3. **Update**:
   - The centroids are updated by calculating the mean position of all data points assigned to each centroid.

4. **Iteration**:
   - Steps 2 and 3 are repeated until the centroids no longer change or the maximum number of iterations is reached.

5. **Evaluation**:
   - The clustering quality is evaluated by calculating the mean intra-cluster variance, which measures the compactness of the clusters.

### Execution

The `main.py` script loads the Iris dataset, applies the K-means algorithm (with optional K-means++ initialization), and evaluates the results. The script runs the clustering process 100 times to calculate the mean intra-cluster variance, providing an overall measure of clustering performance.

### Dataset

The project uses the Iris dataset, which should be stored in the data directory under the name iris.data. The dataset contains measurements of sepal length, sepal width, petal length, and petal width for three species of iris flowers.

### Output
The script prints the following information for each run:

- The composition of each cluster (i.e., how many samples of each class are in each cluster).
- The mean intra-class variance, which is a measure of how well-separated the clusters are.

## Usage

To run the project, ensure you have the necessary dependencies installed. You can then execute the `main.py` script.


