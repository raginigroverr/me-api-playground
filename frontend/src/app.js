import React, { useState, useEffect } from "react";

function App() {
  const [profiles, setProfiles] = useState([]);
  const [projects, setProjects] = useState([]);
  const [skill, setSkill] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/profiles/")
      .then(res => res.json())
      .then(data => setProfiles(data));
  }, []);

  const searchProjects = () => {
    fetch(`http://127.0.0.1:8000/projects/?skill=${skill}`)
      .then(res => res.json())
      .then(data => setProjects(data));
  };

  return (
    <div className="p-4">
      <h1>Me API Playground</h1>

      <h2>Profiles</h2>
      <ul>
        {profiles.map(p => (
          <li key={p.id}>{p.name} - {p.skills}</li>
        ))}
      </ul>

      <h2>Search Projects</h2>
      <input value={skill} onChange={e => setSkill(e.target.value)} placeholder="Search by skill" />
      <button onClick={searchProjects}>Search</button>

      <h2>Projects</h2>
      <ul>
        {projects.map(pr => (
          <li key={pr.id}>{pr.title}: {pr.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
