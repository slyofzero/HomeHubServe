<template>
  <div class="mb-4">
    <div class="d-flex justify-content-between align-items-center">
      <h4>All Professionals</h4>
      <RouterLink to="/admin/professionals">View All</RouterLink>
    </div>
    <div class="table-responsive mt-3">
      <table class="table table-bordered text-nowrap">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Experience (Yrs)</th>
            <th>Service Name</th>
          </tr>
        </thead>
        <tbody v-if="professionals.length > 0">
          <tr
            v-for="professional in professionals"
            :key="professional.id"
            class="text-capitalize"
          >
            <td>{{ professional.id }}</td>
            <td>{{ professional.name }}</td>
            <td>{{ professional.experience }}</td>
            <td>{{ professional.service_name }}</td>
          </tr>
        </tbody>
        <tbody v-else>
          <tr>
            <td colspan="4">No professionals.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { IProfessional } from "@/types";

const { professionals } = defineProps<{ professionals: IProfessional[] }>();
</script>
