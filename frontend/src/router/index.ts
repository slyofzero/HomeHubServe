// router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import { Login, Register } from "@/components/auth";
import {
  ProfessionalRegister,
  ProfessionalDashboard,
} from "@/components/professionals";
import { AdminDashboard, AllProfessionals, AllUsers } from "@/components/admin";

// Define routes
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  // ------------------------------ Auth ------------------------------
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
  // ------------------------------ Admin ------------------------------
  {
    path: "/admin",
    name: "AdminDashboard",
    component: AdminDashboard,
  },
  {
    path: "/admin/professionals",
    name: "AllProfessionals",
    component: AllProfessionals,
  },
  {
    path: "/admin/users",
    name: "AllUsers",
    component: AllUsers,
  },
  // ------------------------------ Professional ------------------------------
  {
    path: "/professional/register",
    name: "ProfessionalRegister",
    component: ProfessionalRegister,
  },
  {
    path: "/professional",
    name: "ProfessionalDashboard",
    component: ProfessionalDashboard,
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
