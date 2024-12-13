<template>
  <div class="container my-4">
    <!-- Dashboard -->
    <section>
      <!-- Services Table -->
      <div class="mb-4">
        <div
          class="d-flex justify-content-between align-items-center flex-wrap"
        >
          <h4>Services</h4>
          <button
            @click="showModal = true"
            class="btn btn-success btn-sm mt-2 mt-md-0"
          >
            + New Service
          </button>
        </div>
        <div class="table-responsive mt-3">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Service Name</th>
                <th>Base Price</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="service in services" :key="service.id">
                <td>{{ service.id }}</td>
                <td>{{ service.name }}</td>
                <td>{{ service.price }}</td>
                <td>
                  <button class="btn btn-primary btn-sm me-2">Edit</button>
                  <button class="btn btn-danger btn-sm">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Professionals Table -->
      <div class="mb-4">
        <h4>Professionals</h4>
        <div class="table-responsive mt-3">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Experience (Yrs)</th>
                <th>Service Name</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="professional in professionals" :key="professional.id">
                <td>{{ professional.id }}</td>
                <td>{{ professional.name }}</td>
                <td>{{ professional.experience }}</td>
                <td>{{ professional.serviceName }}</td>
                <td>
                  <button class="btn btn-success btn-sm me-2">Approve</button>
                  <button class="btn btn-warning btn-sm me-2">Reject</button>
                  <button class="btn btn-danger btn-sm">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Service Requests Table -->
      <div>
        <h4>Service Requests</h4>
        <div class="table-responsive mt-3">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Assigned Professional</th>
                <th>Requested Date</th>
                <th>Status (R/P/C)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="request in serviceRequests" :key="request.id">
                <td>{{ request.id }}</td>
                <td>{{ request.assignedProfessional }}</td>
                <td>{{ request.requestedDate }}</td>
                <td>{{ request.status }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>

  <NewService
    v-if="showModal"
    :showModal="showModal"
    @close="showModal = false"
  />
</template>

<script lang="ts">
import { ref } from "vue";
import NewService from "../modals/service/NewService.vue";
import { clientFetcher } from "../utils/api";
import { IService, ServiceApiRes } from "../types";

export default {
  name: "AdminDashboard",
  setup() {
    const showModal = ref(false);

    const services = ref<IService[]>([]);
    const servicesUrl = `${import.meta.env.VITE_API_URL}/service`;
    (async function () {
      const servicesRes = await clientFetcher<ServiceApiRes>(servicesUrl);
      if (servicesRes.response === 200) {
        services.value = servicesRes.data.data;
      }
    })();

    // const services = ref([
    //   { id: 1, name: "Service 1", price: "$100" },
    //   { id: 2, name: "Service 2", price: "$200" },
    // ]);

    const professionals = ref([
      { id: 1, name: "John Doe", experience: 5, serviceName: "Service 1" },
      { id: 2, name: "Jane Smith", experience: 8, serviceName: "Service 2" },
    ]);

    const serviceRequests = ref([
      {
        id: 1,
        assignedProfessional: "John Doe",
        requestedDate: "2024-12-13",
        status: "Requested",
      },
      {
        id: 2,
        assignedProfessional: "Jane Smith",
        requestedDate: "2024-12-12",
        status: "Accepted",
      },
    ]);

    return { services, professionals, serviceRequests, showModal };
  },
  components: {
    NewService,
  },
};
</script>

<style scoped>
.table th,
.table td {
  vertical-align: middle;
  text-align: center;
}
</style>
