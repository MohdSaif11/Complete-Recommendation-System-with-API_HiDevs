# 🚀 Complete Recommendation System with API

## 📌 Overview

This project implements a complete **Recommendation System** using Python. It integrates a database, recommendation engine, and REST API to simulate how platforms like Netflix and Amazon provide personalized suggestions.

The system combines **candidate generation, scoring, ranking, and evaluation metrics** to produce meaningful recommendations.

---

## 🧠 Key Features

* 🔹 Recommendation Engine (Day 29 integration)
* 🔹 SQLite Database (Users, Content, Interactions)
* 🔹 REST API using Flask
* 🔹 Candidate Generation + Scoring + Ranking
* 🔹 Cold Start Handling (new users supported)
* 🔹 Feedback Recording System
* 🔹 Evaluation Metrics (Precision@K, Recall@K, NDCG@K)
* 🔹 Request Logging with unique request IDs
* 🔹 Performance Metrics Tracking (average response time)
* 🔹 In-memory Caching for faster responses
* 🔹 Load Testing (10 concurrent users simulation)
* 🔹 Unit Testing with >85% coverage (Pytest)

---

## 📂 Project Structure

```
day30_capstone/
├── data/              # Database layer (SQLite + repositories)
├── engine/            # Recommendation engine (orchestrator + evaluator)
├── api/               # Flask API
├── scripts/           # Utilities (seed, evaluate, load test)
├── tests/             # Unit tests
├── requirements.txt
├── README.md
└── evaluation_report.md
```

---

## ⚙️ Technologies Used

* Python 3.x
* Flask
* SQLite
* Pytest
* Requests (for load testing)

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/<your-username>/Complete-Recommendation-System-with-API_HiDevs.git
cd Complete-Recommendation-System-with-API_HiDevs
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Reset & Seed Database

```
rm recommendation.db
python -m scripts.seed_data
```

---

### 4. Run API Server

```
python -m api.app
```

---

### 5. Access API (Codespaces)

* Open **PORTS tab**
* Open port **5000**

---

## 🌐 API Endpoints

| Endpoint            | Method   | Description                   |
| ------------------- | -------- | ----------------------------- |
| `/`                 | GET      | API overview                  |
| `/health`           | GET      | Health check                  |
| `/recommend/<user>` | GET      | Get recommendations           |
| `/feedback`         | GET/POST | Submit or view feedback usage |
| `/metrics`          | GET      | Performance metrics           |

---

## 📊 Example Output

```json
{
  "request_id": "abc-123",
  "user": "u1",
  "recommendations": [
    {
      "item": "c5",
      "reason": "based on popularity + unseen"
    }
  ]
}
```

---

## 🧪 Testing

Run all tests:

```
pytest --cov
```

Expected:

```
Coverage: 85%+
All tests passed ✅
```

---

## 📈 Evaluation

Run evaluation:

```
python -m scripts.evaluate
```

Example output:

```
{'precision': 0.6, 'recall': 1.0, 'ndcg': 0.9}
```

---

## ⚡ Load Testing

Simulate concurrent users:

```
python -m scripts.load_test
```

Example output:

```
🚀 Starting Load Test...

[1] ✅ Success | Time: 0.0012s
...

📊 Load Test Summary
---------------------------
Total Requests   : 10
Successful       : 10
Failed           : 0
Average Time     : 0.0013s

✅ Load Test Completed Successfully 🚀
```

---

## 🎯 Results

* ✔ High Recall (~1.0)
* ✔ Good Precision (~0.6–0.7)
* ✔ Fast Response Time (< 200ms)
* ✔ Stable under concurrent load
* ✔ Clean modular architecture

---

## 🎥 YouTube Demo

Demo Link: https://youtu.be/LroBDuMORoE

---

## 🔮 Future Improvements

* Machine Learning-based recommendations
* Knowledge graph integration
* Real-time personalization
* Frontend dashboard (React / Streamlit)
* Deployment on cloud (Render / AWS)

---

## 👨‍💻 Author

**Mohammed Saif R**

---


This project demonstrates the architecture of a modern recommendation system, including API design, database integration, evaluation metrics, and performance testing. It is designed as a scalable foundation for real-world systems.
