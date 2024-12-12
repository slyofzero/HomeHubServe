<template>
  <header class="bg-light border-bottom shadow-sm">
    <nav
      class="navbar navbar-expand-lg navbar-light container px-4 d-flex items-center"
    >
      <!-- Brand -->
      <h5>Welcome Customer</h5>

      <!-- Toggler -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Collapsible Content -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto d-flex align-items-center gap-4">
          <li class="nav-item">
            <RouterLink class="nav-link active" aria-current="page" to="/"
              >Home</RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/search">Search</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/summary">Summary</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/profile">Profile</RouterLink>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <RouterLink to="/register" class="btn btn-outline-success btn-sm"
              >Register</RouterLink
            >
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <RouterLink to="/login" class="btn bg-dark text-white px-3 btn-sm"
              >Login</RouterLink
            >
          </li>
          <li v-if="isLoggedIn" @click="logout" class="nav-item">
            <button class="btn btn-outline-danger btn-sm">Logout</button>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script lang="ts">
import { RouterLink } from "vue-router";
import { JWT_KEY_NAME } from "../utils/constants";
import { clientFetcher } from "../utils/api";
import { UserApiRes, useUserStore } from "../stores";

export default {
  name: "Header",
  computed: {
    isLoggedIn() {
      return useUserStore().isLoggedIn;
    },
  },
  methods: {
    logout() {
      localStorage.removeItem(JWT_KEY_NAME);
      const userStore = useUserStore();
      userStore.clearUserInfo();
    },
  },
  async created() {
    try {
      const userDataUrl = `${import.meta.env.VITE_API_URL}/user/me`;
      const userData = await clientFetcher<UserApiRes>(userDataUrl);
      const userStore = useUserStore();
      if (userData.response === 200) {
        userStore.setUserInfo(userData.data.data);
      } else {
        userStore.clearUserInfo();
      }
    } catch (error) {
      console.error("Failed to fetch user data:", error);
    }
  },
};
</script>
