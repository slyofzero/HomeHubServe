<template>
  <header class="bg-light border-bottom shadow-sm">
    <nav
      class="navbar navbar-expand-lg navbar-light container px-4 d-flex items-center"
    >
      <!-- Brand -->
      <h5 class="text-capitalize">Welcome {{ name }}</h5>

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
        <ul class="navbar-nav ms-auto d-flex align-items-center gap-1 gap-md-4">
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
          <li v-if="isAdmin" class="nav-item">
            <RouterLink class="nav-link special-link" to="/admin"
              >Admin Dashboard</RouterLink
            >
          </li>
          <li v-if="!isProfessional && !isAdmin && isLoggedIn" class="nav-item">
            <RouterLink
              class="nav-link special-link"
              to="/professional/register"
              >Register as a professional</RouterLink
            >
          </li>
          <li v-if="isProfessional" class="nav-item">
            <RouterLink class="nav-link special-link" to="/professional"
              >Professional Dashboard</RouterLink
            >
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

<script lang="ts" setup>
import { JWT_KEY_NAME } from "../utils/constants";
import { useApi } from "../utils/api";
import { useUserStore } from "../stores";
import { computed, watch } from "vue";
import { SingleUserApiRes } from "../types/user";

const userStore = useUserStore();
const userDataUrl = `${import.meta.env.VITE_API_URL}/user/me`;
const { data: userDataRes } = useApi<SingleUserApiRes>(userDataUrl);

watch(userDataRes, () => {
  const response = userDataRes.value?.response;
  if (response === 200) {
    const userData = userDataRes.value?.data.data;
    if (userData) userStore.setUserInfo(userData);
  } else {
    userStore.clearUserInfo();
  }
});

// Computed variables
const isLoggedIn = computed(() => useUserStore().isLoggedIn);
const isAdmin = computed(() => useUserStore().$state.user?.role === "ADMIN");
const name = computed(() => useUserStore().$state.user?.name || "Customer");
const isProfessional = computed(() => {
  const role = useUserStore().$state.user?.role;
  return role === "PROFESSIONAL" || role == "REG_PROFESSIONAL";
});

function logout() {
  console.log("logout");
  localStorage.removeItem(JWT_KEY_NAME);
  const userStore = useUserStore();
  userStore.clearUserInfo();
}
</script>

<style scoped>
.special-link {
  font-weight: 600;
  text-decoration: underline;
}
</style>
