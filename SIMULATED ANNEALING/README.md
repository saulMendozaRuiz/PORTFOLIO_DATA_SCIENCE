# Traveling Salesman Problem (TSP) with Simulated Annealing — U.S. Cities

This project explores the **Traveling Salesman Problem (TSP)** using **Simulated Annealing (SA)** over a large set of cities in the United States.  
The focus is not on exact geographic realism, but on **heuristic optimization**, **emergent behavior**, and **scalability** (CPU / GPU-oriented thinking).

---

## 📌 Problem Description

The Traveling Salesman Problem (TSP) consists of finding the shortest possible tour that:

- visits each city exactly once  
- returns to the starting city  

TSP is **NP-hard**, making it an ideal benchmark for studying heuristic and stochastic optimization methods such as Simulated Annealing.

---

## 🧠 Approach

This project models TSP as an **energy minimization problem**:

- **State**: a permutation of city indices  
- **Energy**: total tour length  
- **Neighbor moves**: local permutations
- **Optimization**: Simulated Annealing  

Simulated Annealing allows controlled exploration of the solution space by occasionally accepting worse solutions, helping the algorithm escape local minima.

---

## 🌎 Dataset

City coordinate data (latitude & longitude) were obtained from the following public dataset:

- **Liknox — U.S. Cities (JSON)**  
  https://gist.github.com/Liknox/09eca60b360ee731dc65ee7861112274

The dataset contains geographic coordinates for major U.S. cities and is used for **experimental and educational purposes only**.

---

## 📐 Distance Model

Distances are computed using a **planar approximation** over latitude and longitude coordinates.

> While latitude/longitude cannot be mapped isometrically to a plane, planar distance approximations preserve **local neighborhood relationships** for geographically bounded regions such as the United States.  
> This makes them suitable for heuristic TSP optimization, where **relative distances and locality** matter more than exact physical measurements.

This choice prioritizes:
- algorithmic clarity
- computational efficiency
- scalability to large problem sizes

---

## ⚙️ Implementation Overview

- Cities are randomly sampled from the dataset
- Coordinates are stored as floating-point values (rounded to 6 decimals)
- A random initial tour is generated
- The tour is iteratively improved using Simulated Annealing
- The objective function evaluates total tour length

The implementation is designed to be:
- modular
- easy to extend (e.g., alternative neighborhood definitions)
- compatible with future GPU acceleration strategies

---

## 🚀 Goals & Extensions

Planned and experimental extensions include:

- Scaling to **thousands or tens of thousands of cities**
- Efficient neighborhood evaluation using **local updates**
- Memory-aware designs for large distance matrices
- GPU-oriented approaches (block-based neighborhoods, vectorized evaluation)
- Comparative analysis with other heuristics (ACO, GA, 2-opt)

---

## 🧪 Status

This project is **experimental and exploratory**.  
The goal is understanding optimization dynamics rather than producing an industrial-grade TSP solver.

---

## 📄 License

This project is intended for educational and research use.  
Please cite the original dataset source if you reuse or redistribute the data.
