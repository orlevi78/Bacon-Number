function App() {

  const get_bacon_number = (name: string) => {
    console.log("here")
  }

  return (
    <>
      <input placeholder="Enter actor's name!" />
      <button onClick={() => get_bacon_number("here")}>Find Bacon number</button>
    </>

  )
}

export default App