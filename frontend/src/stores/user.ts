// userStore.js (Pinia)
import { defineStore } from "pinia";
import { IUser } from "../types/user";

export const useUserStore = defineStore("user", {
  state: () => ({
    user: null as IUser | null,
  }),
  getters: {
    isLoggedIn: (state) => Boolean(state.user),
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
