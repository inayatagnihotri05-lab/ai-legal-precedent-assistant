async function analyzeCase() {
  const caseText = document.getElementById("caseInput").value;
  const outputDiv = document.getElementById("output");

  outputDiv.innerText = "Analyzing case...";

  try {
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ case: caseText })
    });

    const data = await response.json();

    let result = "";
    result += "⚖️ ISSUES:\n" + data.issues.join("\n") + "\n\n";
    result += "📚 CONTEXT:\n";
    result += "Dispute Value: " + data.context.dispute_value + "\n";
    result += "Applicable Law:\n- " + data.context.applicable_law.join("\n- ") + "\n\n";

    result += "📜 PRECEDENTS:\n";
    data.example_precedents.forEach(p => {
      result += `${p.case_name} (${p.year})\n${p.summary}\nRelevance: ${p.relevance}\n\n`;
    });

    result += "🧠 ADVISORY OPINION:\n" + data.advisory_opinion + "\n\n";
    result += "⚠️ NOTE:\n" + data.note;

    outputDiv.innerText = result;
  } catch (err) {
    outputDiv.innerText = "Error connecting to backend.";
  }
}
