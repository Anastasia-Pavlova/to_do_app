<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

const title = ref("");
const description = ref("");
const error = ref("");
const tasks = ref([]);
const route = useRoute();

async function handleAddTask() {
  if (title.value) {
    const newTask = {
      title: title.value,
      ...(description.value && { description: description.value }),
      user_id: "1",
    };
    tasks.value.push(newTask);
    await axios
      .post(
        "http://127.0.0.1:8000/tasks/tasks/",
        {
          task: newTask,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .catch((e) => (error.value = e.message))
      .finally(() => {
        title.value = "";
        description.value = "";
      });
  }
}

onMounted(async () => {
  console.log("route", route.params);
  await axios({
    methods: "get",
    url: "http://127.0.0.1:8000/tasks/tasks/",
  })
    .then((res) => {
      if (res.data.length) {
        tasks.value = res.data;
      }
    })
    .catch((e) => (error.value = e.message));
});
</script>

<template>
  <div>
    <h1>Your Tasks:</h1>
    <ul id="tasks">
      <li v-for="task in tasks" :key="task.title">
        <p class="taskTitle">{{ task.title }}</p>
        <p class="description">{{ task.description }}</p>
      </li>
    </ul>
    <div class="formWrapper">
      <input v-model="title" placeholder="Enter the task title" />
      <textarea
        v-model="description"
        placeholder="Enter the task description"
      ></textarea>
      <button class="submitButton" @click="handleAddTask">Add</button>
    </div>
    <p class="error" v-show="error">Error: {{ error }}</p>
  </div>
</template>

<style>
h1 {
  text-align: center;
}
.formWrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
input,
textarea {
  margin: 5px;
  height: 30px;
  border: 1px solid rgba(136, 136, 136, 0.752);
  border-radius: 5px;
  width: 100%;
}

.submitButton {
  min-width: 100px;
  min-height: 30px;
  border: 1px solid rgba(0, 78, 255, 1);
  border-radius: 5px;
  color: #ffffff;
  background: rgb(6, 1, 80);
  background: linear-gradient(
    90deg,
    rgb(11, 5, 106) 0%,
    rgba(0, 78, 255, 1) 100%
  );
}
.submitButton:hover {
  color: #fff;
  transform: scale(110%);
  transition: 1s;
}
.taskTitle {
  font-size: 18px;
}
.description {
  font-size: 14px;
}
.error {
  text-align: center;
  color: red;
  font-size: 14px;
}
</style>
