// userStore.js (Pinia)
import { defineStore } from "pinia";
import { IUser } from "@/types/user";

export const useUserStore = defineStore("user", {
  state: () => ({
    user: null as IUser | null,
  }),
  getters: {
    isLoggedIn: (state) => Boolean(state.user),
    isAdmin: (state) => Boolean(state.user) && state.user.role === "ADMIN",
    isProfessional: (state) => {
      const role = state.user.role;
      return (
        Boolean(state.user) &&
        (role === "PROFESSIONAL" || role === "REG_PROFESSIONAL")
      );
    },
    isCustomer: (state) =>
      Boolean(state.user) && state.user.role === "CUSTOMER",
  },
  actions: {
    setUserInfo(userInfo: IUser) {
      this.user = userInfo;
    },
    clearUserInfo() {
      this.user = null;
    },
    setUserRole(role: IUser["role"]) {
      if (this.user) {
        this.user = { ...this.user, role };
      }
    },
  },
});
