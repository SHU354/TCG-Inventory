import React, { useState, useEffect } from "react";

function App() {
  const [cards, setCards] = useState([]);
  const [form, setForm] = useState({ name: "", set: "", rarity: "" });

  useEffect(() => {
    fetch("/api/cards")
      .then((r) => r.json())
      .then(setCards);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("/api/cards", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    const newCard = await res.json();
    setCards([...cards, newCard]);
    setForm({ name: "", set: "", rarity: "" });
  };

  const handleDelete = async (id) => {
    await fetch(`/api/cards/${id}`, { method: "DELETE" });
    setCards(cards.filter((c) => c.id !== id));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Trading Card Inventory</h1>
      <ul>
        {cards.map((c) => (
          <li key={c.id}>
            {c.name} — {c.set} — {c.rarity}{" "}
            <button onClick={() => handleDelete(c.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />
        <input
          placeholder="Set"
          value={form.set}
          onChange={(e) => setForm({ ...form, set: e.target.value })}
          required
        />
        <input
          placeholder="Rarity"
          value={form.rarity}
          onChange={(e) => setForm({ ...form, rarity: e.target.value })}
          required
        />
        <button type="submit">Add Card</button>
      </form>
    </div>
  );
}

export default App;
