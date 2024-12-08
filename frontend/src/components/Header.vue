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
          <li class="nav-item">
            <button class="btn btn-outline-danger btn-sm">Logout</button>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";

export default {
  name: "Header",
};
</script>
