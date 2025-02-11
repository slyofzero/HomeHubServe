// userStore.js (Pinia)
import { defineStore } from "pinia";

export interface UserInfo {
  address: string;
  id: number;
  joined_on: number;
  mobile: string;
  name: string;
  pincode: number;
  role: "ADMIN" | "REG_PROFESSIONAL" | "PROFESSIONAL" | "CUSTOMER";
}

export interface UserApiRes {
  message: string;
  data: UserInfo;
}

export const useUserStore = defineStore("user", {
  state: () => ({
    user: null as UserInfo | null,
  }),
  getters: {
    isLoggedIn: (state) => Boolean(state.user),
  },
  actions: {
    setUserInfo(userInfo: UserInfo) {
      this.user = userInfo;
    },
    clearUserInfo() {
      this.user = null;
    },
  },
});
