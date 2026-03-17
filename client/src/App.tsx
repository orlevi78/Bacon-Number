import { useState } from "react"

function App() {

  const [personName, setPersonName] = useState("");

  const get_bacon_number = () => {
    fetch(`http://localhost:5000/${personName}`).then(response => response.json()).then(data => setPersonName(decode_response_data(data))).catch(error => console.log('Error:', error));
  }

  const decode_response_data = (data: string) => {
    if (data == "-1") {
      return `Error! Person ${personName} is unknown.`
    }
    else if (data == "-2") {
      return `Error! ID ${personName} is unknown.`
    }
    return data
  }

  return (
    <>
      <input placeholder="Enter actor's name!" value={personName} onInput={e => setPersonName(e.target.value)} />
      <button onClick={get_bacon_number}>Find Bacon number</button>
    </>

  )
}

export default App