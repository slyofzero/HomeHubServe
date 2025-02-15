<template>
  <div>
    <span>Account status</span> -
    <span v-if="isOk" class="text-success fw-bold">{{ account?.status }}</span>
    <span v-else-if="isPending" class="text-warning fw-bold">{{
      account?.status
    }}</span>
    <span v-else-if="isNotOk" class="text-danger fw-bold">{{
      account?.status
    }}</span>
    <span v-else class="fw-bold">{{ account?.status }}</span>
  </div>
</template>

<script lang="ts" setup>
import { IProfessional, IUser } from "@/types";
import { computed } from "vue";

interface Props {
  account: IUser | IProfessional;
}
const { account } = defineProps<Props>();

const isOk = computed(
  () => account.status === "ACCEPTED" || account.status === "ALLOWED"
);
const isPending = computed(() => account.status === "PENDING");
const isNotOk = computed(
  () => account.status === "BLOCKED" || account.status === "REJECTED"
);
</script>
