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
            @click="showCreateModal = true"
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
                  <button
                    @click="handleEditClick(service.id)"
                    class="btn btn-primary btn-sm me-2"
                  >
                    Edit
                  </button>
                  <button
                    @click="deleteService(service.id)"
                    class="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
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
    v-if="showCreateModal"
    :showModal="showCreateModal"
    @close="showCreateModal = false"
    @refreshServices="refreshServices"
  />

  <EditService
    v-if="showEditModal"
    :showModal="showEditModal"
    :service="serviceToEdit"
    @close="showEditModal = false"
    @refreshServices="refreshServices"
  />
</template>

<script lang="ts">
import { ref, watch } from "vue";
import { clientDelete, useApi } from "../utils/api";
import { IService, ServiceApiRes } from "../types";
import NewService from "../modals/service/NewService.vue";
import EditService from "../modals/service/EditService.vue";

export default {
  name: "AdminDashboard",
  setup() {
    const showCreateModal = ref(false);
    const showEditModal = ref(false);
    const serviceToEdit = ref<number | null>(null);

    // -------------------- Services --------------------
    const services = ref<IService[]>([]);
    const servicesUrl = `${import.meta.env.VITE_API_URL}/service`;
    const { data: serviceRes, mutate: servicesMutate } =
      useApi<ServiceApiRes>(servicesUrl);

    const refreshServices = () => servicesMutate();

    watch(serviceRes, () => {
      const new_services = serviceRes.value?.data.data;
      services.value = new_services ? new_services : [];
    });

    const handleEditClick = (serviceId: number) => {
      showEditModal.value = true;
      serviceToEdit.value = serviceId;
    };

    const deleteService = async (id: number) => {
      const deleteRes = await clientDelete(`${servicesUrl}/${id}`);
      if (deleteRes.response === 200) servicesMutate();
    };

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

    return {
      services,
      professionals,
      serviceRequests,
      showCreateModal,
      refreshServices,
      deleteService,
      showEditModal,
      serviceToEdit,
      handleEditClick,
    };
  },
  components: {
    NewService,
    EditService,
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
