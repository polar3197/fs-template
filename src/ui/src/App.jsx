import { useEffect, useState } from "react";

import { createUser, getHealth, getUsers } from "./api";
import "./styles/page.css";

export default function App() {
  const [health, setHealth] = useState("checking");
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  async function loadUsers() {
    const data = await getUsers();
    setUsers(data);
  }

  useEffect(() => {
    (async () => {
      try {
        const healthData = await getHealth();
        setHealth(healthData.status);
        await loadUsers();
      } catch (err) {
        setHealth("down");
        setError(err.message);
      }
    })();
  }, []);

  async function onSubmit(event) {
    event.preventDefault();
    setError("");

    try {
      await createUser({ username, email });
      setUsername("");
      setEmail("");
      await loadUsers();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <main className="page">
      <h1>fs-template</h1>
      <p>API health: {health}</p>

      <form className="user-form" onSubmit={onSubmit}>
        <input
          required
          value={username}
          onChange={(event) => setUsername(event.target.value)}
          placeholder="username"
        />
        <input
          required
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          placeholder="email"
        />
        <button type="submit">Create user</button>
      </form>

      {error ? <p className="error">{error}</p> : null}

      <h2>Users</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} ({user.email})
          </li>
        ))}
      </ul>
    </main>
  );
}
