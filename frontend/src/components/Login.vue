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
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import router from "../router";
import { apiPoster, clientFetcher } from "../utils/api";
import { JWT_KEY_NAME } from "../utils/constants";

export default {
  name: "Login",
  data() {
    return {
      form: {
        mobile: "",
        password: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async loginUser(event) {
      event.preventDefault();
      const url = `${import.meta.env.VITE_API_URL}/auth/login`;

      try {
        const res = await apiPoster(url, this.form);

        if (res.response >= 400) {
          this.errorMessage =
            res.data.message || "Invalid credentials. Please try again.";
        } else {
          this.errorMessage = "";
          localStorage.setItem(JWT_KEY_NAME, res.data.token);
          this.$router.push("/");
        }
      } catch (error) {
        this.errorMessage = "An unexpected error occurred. Please try again.";
        console.error("Error during login:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
