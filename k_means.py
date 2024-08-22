import random
import numpy as np


def calculate_distance(point1, point2):
    distance = 0
    for (a, b) in zip(point1, point2):
        distance += pow(a - b, 2)
    return np.sqrt(distance)


def initialize_centroids_forgy(data, k):
    centroids = np.array(random.sample(list(data), k))
    return centroids


def initialize_centroids_kmeans_pp(data, k):
    centroids = []
    random_centroid = random.sample(list(data), 1)
    centroid = []
    for i in range(len(random_centroid[0])):
        centroid.append(random_centroid[0][i])
    centroids.append(centroid)

    for i in range(k-1):
        max_distance = -np.inf
        max_index = -1
        for j in range(len(data)):
            element_min_distance = np.inf
            for k in range(len(centroids)):
                distance = calculate_distance(data[j], centroids[k])
                if distance < element_min_distance:
                    element_min_distance = distance
            if element_min_distance > max_distance:
                max_distance = element_min_distance
                max_index = j
        centroids.append(np.array(data[max_index]))

    return np.array(centroids)


def assign_to_cluster(data, centroids):
    assignments = []
    for element in data:
        min_distance = np.inf
        selected_index = -1
        for i in range(centroids.shape[0]):
            distance_to_centroid = calculate_distance(element, centroids[i])
            if distance_to_centroid < min_distance:
                selected_index = i
                min_distance = distance_to_centroid
        assignments.append(selected_index)
    return assignments


def update_centroids(data, assignments):
    number_of_centroids = len(sorted(set(assignments)))
    centroids = []

    for i in range(number_of_centroids):
        elements_assigned_to_centroid = []
        for j in range(len(data)):
            if assignments[j] == i:
                elements_assigned_to_centroid.append(data[j])

        properties = [0] * len(data[0])
        for element in elements_assigned_to_centroid:
            for j in range(len(element)):
                properties[j] += element[j]

        for j in range(len(properties)):
            properties[j] /= len(elements_assigned_to_centroid)
        centroids.append(properties)

    return np.array(centroids)


def mean_intra_distance(data, assignments, centroids):
    return np.sqrt(np.sum((data - centroids[assignments, :])**2))


def k_means(data, num_centroids, kmeansplusplus=False):
    if kmeansplusplus:
        centroids = initialize_centroids_kmeans_pp(data, num_centroids)
    else: 
        centroids = initialize_centroids_forgy(data, num_centroids)

    assignments = assign_to_cluster(data, centroids)
    for i in range(100):
        print(f"Intra distance after {i} iterations: {mean_intra_distance(data, assignments, centroids)}")
        centroids = update_centroids(data, assignments)
        new_assignments = assign_to_cluster(data, centroids)
        if np.all(new_assignments == assignments):  # stop if nothing changed
            break
        else:
            assignments = new_assignments

    return new_assignments, centroids, mean_intra_distance(data, new_assignments, centroids)         

