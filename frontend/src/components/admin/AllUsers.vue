<template>
  <UsersTable :users="users" :show-view-all="false" />
  <Pagination :url="usersUrl" :limit="10" v-model="users" />
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { IUser, UsersApiRes } from "@/types";
import { clientFetcher } from "@/utils/api";
import { UsersTable } from "@/components/users";
import Pagination from "../Pagination.vue";

const page = ref<number>(1);
const totalPages = ref<number>(1);

const users = ref<IUser[]>([]);
const usersUrl = `${import.meta.env.VITE_API_URL}/admin/users`;

watch(page, async () => {
  const res = await clientFetcher<UsersApiRes>(usersUrl);
  if (res.data.data) {
    users.value = res.data.data;
    totalPages.value = res.data.totalPages;
  }
});
</script>
