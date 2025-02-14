<template>
  <main class="d-flex flex-column gap-5">
    <div class="d-flex flex-column gap-4 p-4 border border-dark rounded">
      <h5 class="text-center fw-semibold">Looking for?</h5>
      <div class="d-flex flex-column flex-md-row justify-content-center gap-4">
        <RouterLink
          v-for="service in services"
          :to="`/service/${service.id}`"
          :key="service.id"
          class="p-4 border border-dark rounded service-width d-flex flex-column justify-content-center align-items-center gap-3 text-dark text-decoration-none"
        >
          <h5 class="h5 fw-semibold">{{ service.name }}</h5>
          <p>{{ service.description }}</p>
        </RouterLink>
      </div>
    </div>

    <div class="d-flex flex-column gap-4">
      <h5 class="fw-semibold">Service History</h5>
      <table
        class="table border-start border-end border-dark rounded overflow-hidden"
      >
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Service Name</th>
            <th>Professional Name</th>
            <th>Phone No.</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Service 1</td>
            <td>.............</td>
            <td>.............</td>
            <td>Closed</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Service 2</td>
            <td>.............</td>
            <td>.............</td>
            <td>Requested</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Service 3</td>
            <td>.............</td>
            <td>.............</td>
            <td>Open</td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { useApi } from "@/utils/api";
import { IService, ServiceApiRes } from "@/types";

const services = ref<IService[]>([]);
const servicesUrl = `${import.meta.env.VITE_API_URL}/service`;
const { data: serviceRes } = useApi<ServiceApiRes>(servicesUrl);

watch(serviceRes, () => {
  const new_services = serviceRes.value?.data.data;
  services.value = new_services ? new_services : [];
});
</script>

<style scoped>
th,
td {
  padding: 0.5rem 1rem;
}

.service-width {
  width: 260px;
}
</style>
