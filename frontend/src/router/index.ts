// router/index.ts
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import { Login, Register } from "@/components/auth";
import {
  ProfessionalRegister,
  ProfessionalDashboard,
} from "@/components/professionals";
import { AdminDashboard, AllProfessionals, AllUsers } from "@/components/admin";
import { useUserStore } from "@/stores";
import { JWT_KEY_NAME } from "@/utils/constants";
import { AllServices, ServiceProfessionals } from "@/components/services";

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
  // ------------------------------ Services ------------------------------
  {
    path: "/services",
    name: "AllServices",
    component: AllServices,
  },
  {
    path: "/service/:id",
    name: "ServiceProfessionals",
    component: ServiceProfessionals,
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();

  if (to.meta.requiresAdmin && !userStore.isAdmin) {
    next("/");
  } else {
    next();
  }
});

export default router;
