#!/usr/bin/env node
import axios from "axios";

async function main() {
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/users"
    );

    const users = response.data;

    console.log("Fetched Users:\n");

    users.forEach(user => {
      console.log(`Name: ${user.name}`);
      console.log(`Email: ${user.email}`);
      console.log(`Company: ${user.company.name}`);
      console.log("--------------------------");
    });

  } catch (err) {
    console.error("Error fetching users:", err);
  }
}

main();
