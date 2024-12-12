// userStore.js (Pinia)
import { defineStore } from "pinia";

export interface UserInfo {
  address: string;
  id: number;
  joined_on: number;
  mobile: string;
  name: string;
  pincode: number;
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
    isLoggedIn: (state) => !!state.user,
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
