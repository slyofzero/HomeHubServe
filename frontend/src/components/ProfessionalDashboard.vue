<template>
  <main class="d-flex flex-column gap-5">
    <div class="d-flex flex-column gap-4">
      <div class="d-flex flex-row gap-2 justify-content-between">
        <h3 class="fw-semibold">Professional Profile</h3>

        <div class="d-flex gap-2 align-items-center">
          <button
            @click="editProfile"
            class="d-flex gap-1 btn btn-secondary text-nowrap"
          >
            Edit <span class="d-none d-md-block">Profile</span>
          </button>
          <button @click="deleteProfile" class="d-flex gap-1 btn btn-danger">
            Delete <span class="d-none d-md-block">Profile</span>
          </button>
        </div>
      </div>
      <div class="d-flex flex-column gap-2">
        <div>
          <span class="text-capitalize text-decoration-underline">{{
            professionalData?.name
          }}</span
          >, {{ professionalData?.experience }} years experience in
          <span class="text-capitalize text-decoration-underline">{{
            professionalData?.service_name
          }}</span>
        </div>

        <div>
          <span>Description</span> -
          <span>{{ professionalData?.description }}</span>
        </div>

        <div>
          <span>Account status</span> -
          <span
            v-if="professionalData?.status === 'ACCEPTED'"
            class="text-success fw-bold"
            >{{ professionalData?.status }}</span
          >
          <span
            v-else-if="professionalData?.status === 'PENDING'"
            class="text-warning fw-bold"
            >{{ professionalData?.status }}</span
          >
          <span v-else class="text-success fw-danger">{{
            professionalData?.status
          }}</span>
        </div>
      </div>
    </div>

    <div
      v-if="isProfessional"
      class="table-responsive d-flex flex-column gap-4"
    >
      <h5 class="fw-semibold">Today's Service Requests</h5>
      <table
        class="table border-start border-end border-dark rounded overflow-hidden"
      >
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Customer Name</th>
            <th>Email</th>
            <th>Location</th>
            <th>Action</th>
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

  <EditProfessional
    v-if="showEditModal"
    :showModal="showEditModal"
    @close="showEditModal = false"
    @refreshProfessional="refreshProfessional"
  />

  <DeleteProfessional
    v-if="showDeleteModal"
    :showModal="showDeleteModal"
    @close="showDeleteModal = false"
    @refreshProfessional="refreshProfessional"
  />
</template>

<script lang="ts" setup>
import { computed, ref, watch } from "vue";
import router from "../router";
import { useUserStore } from "../stores";
import { JWT_KEY_NAME } from "../utils/constants";
import { useApi } from "../utils/api";
import { IProfessionalMe, ProfessionalApiRes } from "../types";
import EditProfessional from "../modals/professional/EditProfessional.vue";
import DeleteProfessional from "../modals/professional/DeleteProfessional.vue";

// Check if user is admin
const userStore = useUserStore();
if (!userStore.isLoggedIn && !localStorage.getItem(JWT_KEY_NAME))
  router.push("/login");

watch(userStore, () => {
  const role = userStore.$state.user?.role;
  if (!userStore.isLoggedIn) router.push("/login");
  else if (role !== "PROFESSIONAL" && role !== "REG_PROFESSIONAL")
    router.push("/");
});

const isProfessional = computed(
  () => userStore.$state.user?.role === "PROFESSIONAL"
);

// Get professional data
const professionalData = ref<IProfessionalMe>();
const showEditModal = ref(false);
const showDeleteModal = ref(false);

const professoinalsUrl = `${import.meta.env.VITE_API_URL}/professional/me`; // prettier-ignore
const { data: professionalRes, mutate: refreshProfessional } =
  useApi<ProfessionalApiRes>(professoinalsUrl);
watch(professionalRes, () => {
  professionalData.value = professionalRes.value?.data.data?.[0];
});

const editProfile = () => {
  showEditModal.value = true;
};

const deleteProfile = () => {
  showDeleteModal.value = true;
};
</script>
