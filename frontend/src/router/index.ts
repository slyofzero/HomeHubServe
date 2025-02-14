// router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import AdminDashboard from "@/components/AdminDashboard.vue";
import ProfessionalDashboard from "@/components/professionals/ProfessionalDashboard.vue";
import AllProfessionals from "@/components/professionals/AllProfessionals.vue";
import { Login, Register } from "@/components/auth";
import { ProfessionalRegister } from "@/components/professionals";

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
    meta: { requiresAuth: true },
  },
  {
    path: "/admin/professionals",
    name: "AllProfessionals",
    component: AllProfessionals,
    meta: { requiresAuth: true },
  },
  {
    path: "/professional/register",
    name: "ProfessionalRegister",
    component: ProfessionalRegister,
    meta: { requiresAuth: true },
  },
  {
    path: "/professional",
    name: "ProfessionalDashboard",
    component: ProfessionalDashboard,
    meta: { requiresAuth: true },
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
