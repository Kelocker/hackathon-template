
# 📘 Project Setup Instructions

This project uses **Docker + Docker Compose** to run a full-stack app with a **React frontend** and a **Flask backend**.

---

### ✅ Step 1: Use This Template

1. Click the green **"Use this template"** button at the top of the page
2. Create your own repository based on this template

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Rq7Jgv8IT8DtmL-SbLFdIRNwLMuqHIgF" alt="Use this template" width="600"/>
</p>


---

### ✅ Step 2: Build and Run the App with Docker

After cloning your repository into your machine, run:

```bash
docker compose up --build
```

Open your browser and check:

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend: [http://localhost:5000/api/hello](http://localhost:5000/api/hello)

✅ Both should be running fine.

---

### ✅ Step 3: Start Coding

You can now edit your code in your editor — Docker will reflect the changes automatically via volume mounting.

---

### 🔁 After Pulling Updates from GitHub

Always rebuild after pulling code to ensure updates (especially dependencies) are applied:

```bash
docker compose up --build
```

---

### 🧼 Optional: Clean Up Occasionally

If you’ve been switching branches or running lots of containers/images:

```bash
docker system prune -a --volumes -f
```

> ⚠️ This removes **all unused containers, images, volumes, and networks**. Use with care.
