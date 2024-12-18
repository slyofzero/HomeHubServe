// router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Register from "../components/Register.vue";
import Login from "../components/Login.vue";
import AdminDashboard from "../components/AdminDashboard.vue";

// Define routes
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/admin",
    name: "AdminDashboard",
    component: AdminDashboard,
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
