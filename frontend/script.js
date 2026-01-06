async function explain() {
  try {
    const res = await fetch("http://127.0.0.1:5000/explain", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ test: "hello" })
    });

    const data = await res.json();
    alert(data.result);

  } catch (err) {
    alert("ERROR: " + err);
    console.error(err);
  }
}
