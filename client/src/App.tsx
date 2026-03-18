import { useState } from "react";
import "./App.css";

function App() {
  const [personName, setPersonName] = useState("");
  const [result, setResult] = useState("");

  const get_bacon_number = () => {
    fetch(`http://localhost:5000/${personName}`)
      .then((response) => response.json())
      .then((data) => setResult(decode_response_data(data)))
      .then(() => setPersonName(""))
      .catch((error) => console.log("Error:", error));
  };

  const decode_response_data = (data: string) => {
    if (data == "-1") {
      return `Error! Person: '${personName}' is unknown.`;
    } else if (data == "-2") {
      return `Error! ID: '${personName}' is unknown.`;
    }
    return `Bacon number of ${personName} is: ${data}`;
  };

  return (
    <div className="user-input-output">
      <input
        placeholder="Enter actor's name or ID as written in IMDB!"
        value={personName}
        onInput={(e) => setPersonName(e.currentTarget.value)}
      />
      <button id="find-number-button" onClick={get_bacon_number}>Find Bacon number</button>
      <label>{result}</label>
    </div>
  );
}

export default App;
