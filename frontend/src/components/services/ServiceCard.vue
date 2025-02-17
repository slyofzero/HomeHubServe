<template>
  <RouterLink
    :to="`/service/${service.id}`"
    :key="service.id"
    class="p-4 border border-dark rounded service-width d-flex flex-column justify-content-center align-items-center gap-3 text-dark text-decoration-none"
  >
    <div class="d-flex gap-2 align-items-center">
      <h5 class="h5 fw-semibold">{{ service.name }}</h5>
    </div>
    <span>{{ service.description }}</span>
    <span>Starting from Rs {{ service.base_price }}</span>
  </RouterLink>
</template>

<script lang="ts" setup>
import { IService } from "@/types";

interface Props {
  service: IService;
}
const { service } = defineProps<Props>();
</script>
