import sys
import numpy as np

def nearest_neighbor(V):
    home = V[0]

    U = np.array([V[0]])
    V = V[1:]

    while np.size(V) > 0:
        u = U[-1]

        dists = (V[:,1:3] - u[1:3]) ** 2
        dists = np.sum(dists, axis=1)
        dists = np.sqrt(dists)
        dists = np.around(dists).astype(int)

        min_dist = np.min(dists)
        idx = np.where(dists == min_dist)[0]

        U = np.vstack((U, V[idx]))
        V = np.delete(V, idx, 0)

    # Now go home
    U = np.append(U, home)

    # Reshape
    U = np.reshape(U, (-1, 3))

    return U

def two_opt(T):
    changed = True

    best_dist = tour_distance(T)
    while changed:
        changed = False

        for i in range(1, len(T) - 2):
            print("At", i, "of", len(T))
            for j in range(i + 1, len(T) - 1):
                new_dist = best_dist
                new_dist -= distance(T[i-1], T[i]) + distance(T[j-1], T[j])
                new_dist += distance(T[i-1], T[j-1]) + distance(T[j], T[i])

                if new_dist < best_dist:
                    T[i:j] = T[i:j][::-1]

                    best_dist = new_dist
                    changed = True
                    break

            if changed:
                break

    return T

def distance(u, v):
    return int(round(np.sqrt((u[1] - v[1]) ** 2 + (u[2] - v[2]) ** 2)))

def tour_distance(V):
    dist = 0
    last = V[0]
    for v in V[1:]:
        dist += distance(v, last)
        last = v

    return dist

def run(source):
    cities = np.genfromtxt(source, delimiter=" ", dtype=int)

    tour = nearest_neighbor(cities)
    tour = two_opt(tour)
    length = tour_distance(tour)

    print(length)
    for city_id in tour[0:-1,0]:
        print(city_id)

if __name__ == "__main__":
    run(sys.argv[1])
