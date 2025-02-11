<template>
  <div
    class="container p-4 p-md-5 rounded border border-dark d-flex flex-column gap-4"
  >
    <h2>Register</h2>
    <span
      v-if="errorMessage"
      class="text-danger bg-danger-subtle rounded px-4 py-1"
      >{{ errorMessage }}</span
    >
    <form class="d-flex flex-column gap-4" @submit.prevent="registerUser">
      <div>
        <label for="name" class="form-label">Name</label>
        <input
          type="text"
          id="name"
          v-model="form.name"
          class="form-control"
          required
        />
      </div>
      <div>
        <label for="mobile" class="form-label">Mobile</label>
        <input
          type="tel"
          id="mobile"
          v-model="form.mobile"
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
      <div>
        <label for="address" class="form-label">Address</label>
        <textarea
          id="address"
          v-model="form.address"
          class="form-control"
          rows="3"
          required
        ></textarea>
      </div>
      <div>
        <label for="pincode" class="form-label">Pincode</label>
        <input
          type="number"
          id="pincode"
          v-model="form.pincode"
          class="form-control"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import router from "../router";
import { IApiRes } from "../types";
import { apiPoster } from "../utils/api";

const form = ref({
  name: "",
  mobile: "",
  password: "",
  address: "",
  pincode: "",
});
const errorMessage = ref("");

async function registerUser() {
  const url = `${import.meta.env.VITE_API_URL}/auth/register`;

  try {
    const res = await apiPoster<IApiRes>(url, form.value);

    if (res.response >= 400) {
      errorMessage.value =
        res.data.message || "Invalid credentials. Please try again.";
    } else {
      errorMessage.value = "";
      router.push("/login");
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
