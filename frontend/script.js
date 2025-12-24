async function analyzeCase() {
  const caseText = document.getElementById("caseInput").value;
  const output = document.getElementById("output");
  const button = document.getElementById("analyzeBtn");

  output.innerHTML = `<div class="card loader">⏳ Analyzing case…</div>`;
  button.disabled = true;

  try {
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ case: caseText })
    });

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const data = await response.json();

    output.innerHTML = `
      <div class="card">
        <div class="section-title">⚖️ Legal Issues</div>
        <pre>${data.issues.join("\n")}</pre>
      </div>

      <div class="card">
        <div class="section-title">📚 Context</div>
        <pre>
Dispute Value: ${data.context.dispute_value}

Applicable Law:
- ${data.context.applicable_law.join("\n- ")}
        </pre>
      </div>

      <div class="card">
        <div class="section-title">📜 Relevant Precedents</div>
        <pre>
${data.example_precedents.map(p =>
`${p.case_name} (${p.year})
${p.summary}
Relevance: ${p.relevance}\n`
).join("\n")}
        </pre>
      </div>

      <div class="card">
        <div class="section-title">🧠 Advisory Opinion</div>
        <pre>${data.advisory_opinion}</pre>
      </div>

      <div class="card">
        <div class="section-title">⚠️ Disclaimer</div>
        <pre>${data.note}</pre>
      </div>
    `;
  } catch (err) {
    output.innerHTML = `
      <div class="card error">
        ❌ Unable to connect to backend.<br />
        Make sure the server is running.
      </div>
    `;
  } finally {
    button.disabled = false;
  }
}
