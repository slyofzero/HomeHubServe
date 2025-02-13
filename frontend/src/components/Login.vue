<template>
  <div
    class="container p-4 p-md-5 rounded border border-dark d-flex flex-column gap-4"
  >
    <h2>Login</h2>
    <span
      v-if="errorMessage"
      class="text-danger bg-danger-subtle rounded px-4 py-1"
    >
      {{ errorMessage }}
    </span>
    <form class="d-flex flex-column gap-4" @submit.prevent="loginUser">
      <div>
        <label for="email" class="form-label">Email</label>
        <input
          type="tel"
          id="email"
          v-model="form.email"
          class="form-control"
          required
        />
      </div>
      <div>
        <label for="password" class="form-label">Password</label>
        <input
          type="password"
          id="password"
          v-model="form.password"
          class="form-control"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { ILoginRes } from "../types";
import { apiPoster, clientFetcher } from "../utils/api";
import { JWT_KEY_NAME } from "../utils/constants";
import router from "../router";
import { UserApiRes, useUserStore } from "../stores";

const form = ref({
  email: "",
  password: "",
});
const errorMessage = ref("");
const userStore = useUserStore();

async function loginUser(event: Event) {
  event.preventDefault();
  const url = `${import.meta.env.VITE_API_URL}/auth/login`;

  try {
    const res = await apiPoster<ILoginRes>(url, form.value);

    if (res.response >= 400) {
      errorMessage.value =
        res.data.message || "Invalid credentials. Please try again.";
    } else {
      errorMessage.value = "";
      localStorage.setItem(JWT_KEY_NAME, res.data.token);
      const userDataUrl = `${import.meta.env.VITE_API_URL}/user/me`;
      const data = await clientFetcher<UserApiRes>(userDataUrl);
      const userData = data.data.data;
      userStore.setUserInfo(userData);

      if (userData.role === "ADMIN") router.push("/admin");
      else router.push("/");
    }
  } catch (error) {
    errorMessage.value = "An unexpected error occurred. Please try again.";
    console.error("Error during login:", error);
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
