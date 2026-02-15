import { useState } from "react";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  function onSubmit(event) {
    event.preventDefault();
    // Placeholder form for future auth wiring.
    console.log("login", { username, password });
  }

  return (
    <div className="page">
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="Username"
          onChange={(event) => setUsername(event.target.value)}
          value={username}
        />
        <input
          type="password"
          placeholder="Password"
          onChange={(event) => setPassword(event.target.value)}
          value={password}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
