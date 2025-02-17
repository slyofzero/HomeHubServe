<template>
  <main class="d-flex flex-column gap-4 p-4 border border-dark rounded">
    <h4 class="text-center">Best {{ service.name }} packages</h4>

    <div class="table-responsive mt-3">
      <table
        class="table border-start border-end border-dark rounded overflow-hidden text-nowrap"
      >
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Joined On</th>
            <th>Role</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <!-- <tbody v-if="users.length > 0">
          <tr v-for="user in users" :key="user.id" class="text-capitalize">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>{{ formatUnixTimestamp(user.joined_on) }}</td>
            <td>{{ user.role }}</td>
            <td>{{ user.status }}</td>
            <td class="d-flex justify-content-center">
              <button
                @click="handleViewUserClick(user.id)"
                class="btn btn-primary btn-sm me-2"
              >
                View
              </button>
            </td>
          </tr>
        </tbody> -->
        <!-- <tbody v-else>
          <tr>
            <td class="text-center" colspan="6">No professionals found.</td>
          </tr>
        </tbody> -->
      </table>
    </div>
  </main>

  <!-- <ViewUser
    v-if="showViewModal"
    :showModal="showViewModal"
    :user="userSelected"
    @close="showViewModal = false"
    @refreshUsers="refreshUsers"
  /> -->
</template>

<script lang="ts" setup>
import { IProfessional, IService, ServiceProfessionalApiRes } from "@/types";
import { useApi } from "@/utils/api";
import { computed, ref, watch } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const service = ref<IService>();
const professionals = ref<IProfessional[]>([]);
const professionalsUrl = computed(
  () =>
    `${import.meta.env.VITE_API_URL}/service/${route.params.id}/professionals`
);
const { data: professionalsRes } = useApi<ServiceProfessionalApiRes>(
  professionalsUrl.value
);
watch(professionalsRes, () => {
  const data = professionalsRes.value.data.data;
  service.value = data.service;
  professionals.value = data.professionals;
});
</script>
