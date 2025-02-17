<template>
  <div class="mb-4">
    <div class="d-flex justify-content-between align-items-center">
      <h4>All Professionals</h4>
      <RouterLink v-if="showViewAll" to="/admin/professionals"
        >View All</RouterLink
      >
    </div>
    <div class="table-responsive mt-3">
      <table
        class="table border-start border-end border-dark rounded overflow-hidden text-nowrap"
      >
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Experience (Yrs)</th>
            <th>Pincode</th>
            <th>Service Name</th>
            <th>Price</th>
            <th></th>
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
            <td>{{ professional.pincode }}</td>
            <td>{{ professional.service_name }}</td>
            <td>Rs {{ professional.price }}</td>
            <td class="d-flex justify-content-center">
              <button
                @click="handleViewProfessionalClick(professional.id)"
                class="btn btn-primary btn-sm me-2"
              >
                View
              </button>
            </td>
          </tr>
        </tbody>
        <tbody v-else>
          <tr>
            <td class="text-center" colspan="4">No professionals.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <ViewProfessional
    v-if="showViewModal"
    :showModal="showViewModal"
    :professional="professionalSelected"
    @close="showViewModal = false"
    @refreshProfessionals="refreshProfessionals"
  />
</template>

<script lang="ts" setup>
import { ViewProfessional } from "@/modals";
import { IProfessional } from "@/types";
import { computed, ref } from "vue";

interface Props {
  professionals: IProfessional[];
  showViewAll?: any;
}
const { professionals, ...props } = defineProps<Props>();
const emit = defineEmits(["refreshProfessionals"]);

const showViewAll = computed(() =>
  typeof props.showViewAll === "boolean" ? props.showViewAll : true
);

const refreshProfessionals = () => {
  emit("refreshProfessionals");
};

// View Modal
const showViewModal = ref(false);
const professionalSelected = ref<IProfessional | null>();

const handleViewProfessionalClick = (professionalId: number) => {
  showViewModal.value = true;
  professionalSelected.value = professionals.find(
    ({ id }) => id === professionalId
  ) as IProfessional;
};
</script>
