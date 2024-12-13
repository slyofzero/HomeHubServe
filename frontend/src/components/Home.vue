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

<script lang="ts">
import { onMounted, ref } from "vue";
import { clientFetcher } from "../utils/api";
import { IService, ServiceApiRes } from "../types";

export default {
  setup() {
    const services = ref<IService[]>([]); // Reactive state for storing services

    async function getServices() {
      const url = `${import.meta.env.VITE_API_URL}/service`;
      const response = await clientFetcher<ServiceApiRes>(url);
      if (response.response === 200) {
        services.value = response.data.data.slice(0, 4); // Update reactive state
      }
    }

    onMounted(() => getServices());

    return { services }; // Expose services to the template
  },
};
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
