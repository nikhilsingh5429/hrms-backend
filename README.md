# HRMS Backend

This is the **backend service** for the HRMS (Human Resource Management System). It provides REST APIs for authentication, employee management, attendance, and other HR-related operations.

---

## 🚀 Tech Stack

* **Node.js**
* **Express.js**
* **MongoDB** (Mongoose)
* **JWT Authentication**
* **dotenv** for environment variables
* **CORS** enabled

---

## 📁 Project Structure

```
hrms-backend/
│── controllers/
│── models/
│── routes/
│── middlewares/
│── config/
│── .env
│── .gitignore
│── package.json
│── server.js (or index.js)
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
```

---

## 📦 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/<your-username>/hrms-backend.git
cd hrms-backend
```

Install dependencies:

```bash
npm install
```

Run the server:

```bash
npm start
```

For development (optional):

```bash
npm run dev
```

Server will run at:

```
http://localhost:5000
```

---

## 🔌 API Features

* User Authentication (Login / Register)
* Employee CRUD Operations
* Attendance Management
* Secure APIs using JWT
* Role-based access (optional)

---

## 🔗 Frontend Connection

Update your frontend API base URL:

```js
const API_BASE_URL = "https://your-backend-url.vercel.app";
```

Ensure **CORS** is enabled in backend.

---

## 🚀 Deployment

You can deploy this backend using:

* **Render** (recommended)
* **Railway**
* **Cyclic**
* **Vercel (Serverless)**

Make sure to add environment variables on the hosting platform.

---

## 🛡️ Security Notes

* Do not commit `.env` file
* Use strong JWT secrets
* Enable HTTPS in production

---

## 📜 License

This project is for educational and internal use.

---

## 👤 Author

**Nikhil Singh**

---

✨ If you like this project, feel free to star the repository!
