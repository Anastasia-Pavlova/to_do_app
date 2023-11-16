<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const name = ref("");
const email = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();

async function handleSubmit() {
  const user = {
    username: name.value,
    email: email.value,
    password: password.value,
  };
  await axios
    .post(
      "http://127.0.0.1:8000/tasks/login/",
      {
        user,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
    .then(() => {
      router.push({ path: "todo" });
    })
    .catch((e) => {
      error.value = e.response?.data.message || e.message;
    });
}
</script>

<template>
  <div class="wrapper">
    <h1>Please, enter the data:</h1>
    <p>Name:</p>
    <input v-model="name" placeholder="Enter the name" />
    <p>Email:</p>
    <input v-model="email" placeholder="Enter the email" />
    <p>Password:</p>
    <input v-model="password" placeholder="Enter the password" />
    <button @click="handleSubmit">Log In</button>
    <p class="error" v-show="error">Error: {{ error }}</p>
  </div>
</template>

<style>
.wrapper {
  text-align: center;
}
input {
  width: 100%;
}
p {
  text-align: left;
}
.error {
  text-align: center;
  color: red;
  font-size: 14px;
}
</style>
