
async function testFetch() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();
    console.log("Parsed JSON:", data);
  } catch (err) {
    console.error("Fetch error:", err);
  }
}

testFetch();
