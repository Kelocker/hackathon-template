
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

### ✅ Step 3: Changing GitHub Action (Optional)

<details>
<summary>⚠️ Disclaimer (Please read)</summary>

This project includes a GitHub Actions workflow set to **manual-only** (`workflow_dispatch`).  
No automated workflows will run during cloning, pushing, or using this template — unless a user explicitly chooses to run them.

If you click **"Run workflow"** or manually enable automatic workflows  
(e.g., by renaming `.github/workflows/docker-composer-autobuild.txt` to `.yml`),  
you are doing so **at your own discretion** and accept full responsibility for any usage, billing, or side effects.

This template is provided as-is. I maintain versioning and structure, but I am **not responsible** for:
- GitHub Actions billing  
- Workflow behavior (e.g., broken Docker builds)  
- Security or compliance of any changes made after using this template

</details>

<details>
<summary>⚙️ What the Manual GitHub Action Does (By opening this, you agree to the disclaimer above)</summary>

When you click **“Run workflow”** in the Actions tab, the workflow:

1. Checks out the current branch  
2. Sets up Docker with BuildKit support  
3. Runs `docker compose build`  
   → This builds the **frontend and backend images** using the `Dockerfile` and `docker-compose.yml`

> ✅ No containers are run  
> ❌ No tests or deployments  
> 🔒 Only builds — safe for checking Docker config


>⚠️ Note: Running this workflow will consume GitHub Actions minutes.
>Please be mindful of usage if you're on a free plan without GitHub Education or Pro benefits.
>Refer to the disclaimer above for more details on usage, responsibility, and billing.

</details>

<details>
<summary>⚙️ What the Automatic GitHub Action Would Do (By opening this, you agree to the disclaimer above if re-enabled)</summary>

If you rename `.github/workflows/docker-composer-autobuild.txt` to `.yml`,  
this workflow will be automatically triggered on:

- ✅ Any `push` to any branch  
- ✅ Any pull request targeting the `main` branch (excluding `.md` or documentation-only changes)

### 🔧 What it does:

Automatically runs on code-related changes (excluding markdown and docs):

1. **Checks out the current branch**  
2. **Sets up Docker with BuildKit support**  
3. **Runs** `docker compose build`  
   → This builds both the **frontend** and **backend** images using the `Dockerfile` and `docker-compose.yml`

### ⚠️ Key Behavior:

- This workflow will **run every time code is pushed or a pull request is opened**
- If the Docker build fails (e.g., due to code errors or misconfigurations), the workflow will **fail**
- This **consumes GitHub Actions minutes**, even if the push is small

> ⚠️ Enable this only if you are confident in your Docker setup  
> and accept the billing and runtime implications of automated workflows.  
>
> 📌 **Refer to the disclaimer above for full details regarding usage responsibility and billing.**

</details>


---


### ✅ Step 4: Start Coding

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



---

### ✍️ Template Info

This project template is created and maintained by [Kelocker](https://github.com/Kelocker).  
Original repository: [hackathon-template](https://github.com/Kelocker/hackathon-template)

If you find this useful, feel free to ⭐ the repo or mention it in your own project!
