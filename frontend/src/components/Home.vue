<template>
  <main class="d-flex flex-column gap-5">
    <div class="d-flex flex-column gap-4 p-4 border border-dark rounded">
      <div class="position-relative">
        <h5 class="text-center fw-semibold flex-grow-1">Looking for?</h5>
        <RouterLink to="/services" class="position-absolute top-0 end-0"
          >View All</RouterLink
        >
      </div>

      <div class="d-flex flex-column flex-md-row justify-content-center gap-4">
        <ServiceCard
          v-for="service in services.slice(0, 3)"
          :service="service"
        />
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
import { RouterLink } from "vue-router";
import { ServiceCard } from "./services";

const services = ref<IService[]>([]);
const servicesUrl = `${import.meta.env.VITE_API_URL}/service?limit=3`;
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
