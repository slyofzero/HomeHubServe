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
          <table class="table table-bordered text-nowrap">
            <thead>
              <tr>
                <th>ID</th>
                <th>Service Name</th>
                <th>Base Price</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody v-if="services.length">
              <tr v-for="service in services" :key="service.id">
                <td>{{ service.id }}</td>
                <td>{{ service.name }}</td>
                <td>{{ service.price }}</td>
                <td class="d-flex justify-content-center">
                  <button
                    @click="handleEditClick(service.id)"
                    class="btn btn-primary btn-sm me-2"
                  >
                    Edit
                  </button>
                  <button
                    @click="handleDeleteClick(service.id)"
                    class="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
            <tbody v-else>
              <tr>
                <td colspan="5">No services created yet.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Professional Applications Table -->
      <div class="mb-4">
        <h4>Professional Applications</h4>
        <div class="table-responsive mt-3">
          <table class="table table-bordered text-nowrap">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Experience (Yrs)</th>
                <th>Service Name</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody v-if="professionalApplications.length > 0">
              <tr
                v-for="professional in professionalApplications"
                :key="professional.id"
                class="text-capitalize"
              >
                <td>{{ professional.id }}</td>
                <td>{{ professional.name }}</td>
                <td>{{ professional.experience }}</td>
                <td>{{ professional.service_name }}</td>
                <td>
                  <button
                    @click="handleViewApplicationClick(professional.id)"
                    class="btn btn-primary btn-sm me-2"
                  >
                    View
                  </button>
                </td>
              </tr>
            </tbody>
            <tbody v-else>
              <tr>
                <td colspan="5">No pending professional applications.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- All Professionals Table -->
      <ProfessionalsTable :professionals="professionals" />

      <!-- All Users Table -->
      <UsersTable :users="users" />
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
    :service="serviceSelected"
    @close="showEditModal = false"
    @refreshServices="refreshServices"
  />

  <DeleteService
    v-if="showDeleteModal"
    :showModal="showDeleteModal"
    :service="serviceSelected"
    @close="showDeleteModal = false"
    @refreshServices="refreshServices"
  />

  <ApplicationProfessional
    v-if="showApplicationModal"
    :showModal="showApplicationModal"
    :professional="applicationSelected"
    @close="showApplicationModal = false"
    @refreshProfessionalApplications="refreshProfessionalApplications"
  />
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { useApi } from "@/utils/api";
import {
  IProfessional,
  IService,
  ProfessionalApiRes,
  ServiceApiRes,
} from "@/types";
import { useUserStore } from "@/stores";
import { JWT_KEY_NAME } from "@/utils/constants";
import router from "@/router";
import { IUser, UsersApiRes } from "@/types/user";
import {
  ApplicationProfessional,
  DeleteService,
  EditService,
  NewService,
} from "@/modals";
import { UsersTable } from "@/components/users";
import { ProfessionalsTable } from "@/components/professionals";

const showCreateModal = ref(false);
const showEditModal = ref(false);
const showDeleteModal = ref(false);
const serviceSelected = ref<number | null>(null);

// -------------------- Services --------------------
const services = ref<IService[]>([]);
const servicesUrl = `${import.meta.env.VITE_API_URL}/service/all`;
const { data: serviceRes, mutate: servicesMutate } =
  useApi<ServiceApiRes>(servicesUrl);

watch(serviceRes, () => {
  const new_services = serviceRes.value?.data.data;
  console.log(new_services);
  services.value = new_services ? new_services : [];
});

const handleEditClick = (serviceId: number) => {
  showEditModal.value = true;
  serviceSelected.value = serviceId;
};

const handleDeleteClick = (serviceId: number) => {
  showDeleteModal.value = true;
  serviceSelected.value = serviceId;
};

// -------------------- Professional Applications --------------------
const showApplicationModal = ref(false);
const applicationSelected = ref<IProfessional | null>(null);

const handleViewApplicationClick = (applicationId: number) => {
  showApplicationModal.value = true;
  applicationSelected.value = professionalApplications.value.find(
    ({ id }) => id === applicationId
  ) as IProfessional;
};

const professionalApplications = ref<IProfessional[]>([]);
const professoinalsApplicationsUrl = `${import.meta.env.VITE_API_URL}/professional/applications`; // prettier-ignore
const {
  data: professionalsApplicationRes,
  mutate: professionalsApplicationsMutate,
} = useApi<ProfessionalApiRes>(professoinalsApplicationsUrl);

const refreshProfessionalApplications = () => professionalsApplicationsMutate();

watch(professionalsApplicationRes, () => {
  professionalApplications.value =
    professionalsApplicationRes.value?.data.data || [];
});

// -------------------- All Professionals --------------------
const professionals = ref<IProfessional[]>([]);
const professoinalsUrl = `${import.meta.env.VITE_API_URL}/admin/professionals`; // prettier-ignore
const { data: professionalsRes, mutate: professionalsMutate } =
  useApi<ProfessionalApiRes>(professoinalsUrl);

watch(professionalsRes, () => {
  professionals.value = professionalsRes.value?.data.data || [];
});

const refreshServices = () => {
  servicesMutate();
  professionalsMutate();
  professionalsApplicationsMutate();
};

// -------------------- All Users --------------------
const users = ref<IUser[]>([]);
const usersUrl = `${import.meta.env.VITE_API_URL}/admin/users`; // prettier-ignore
const { data: usersRes } = useApi<UsersApiRes>(usersUrl);

watch(usersRes, () => {
  users.value = usersRes.value?.data.data || [];
});
</script>

<style scoped>
.table th,
.table td {
  vertical-align: middle;
  text-align: center;
}
</style>
