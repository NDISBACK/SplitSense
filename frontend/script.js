function analyseRepo() {
  console.log("🔵 Button clicked");

  fetch("/explain", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ test: "hello" })
  })
  .then(res => {
    console.log("🟢 Response status:", res.status);
    return res.json();
  })
  .then(data => {
    console.log("🟢 Data received:", data);
    document.getElementById("output").innerText = data.result;
  })
  .catch(err => {
    console.error("🔴 Fetch error:", err);
  });
}
