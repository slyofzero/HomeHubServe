<template>
  <Modal :show-modal="props.showModal">
    <template #header>
      <!-- Modal Header -->
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Professional Application</h4>
        <button
          @click="closeModal"
          class="btn-close"
          aria-label="Close"
        ></button>
      </div>
    </template>

    <template #body>
      <div class="d-flex flex-column gap-4">
        <span
          v-if="errorMessage"
          class="text-danger bg-danger-subtle rounded px-4 py-1"
          >{{ errorMessage }}</span
        >

        <div class="modal-body d-flex flex-column gap-2 text-capitalize">
          <div class="d-flex gap-2">
            <span>Name</span> -
            <span>{{ professional?.name }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Experience</span> -
            <span>{{ professional?.experience }} years</span>
          </div>
          <div class="d-flex gap-2">
            <span>Service</span> -
            <span>{{ professional?.service_name }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Description</span> -
            <span>{{ professional?.description }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Price</span> -
            <span>Rs {{ professional?.price }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Application Created On</span> -
            <span>{{ formatUnixTimestamp(professional?.created_on) }}</span>
          </div>
        </div>

        <!-- Modal Body -->
        <form @submit.prevent="() => {}">
          <!-- Modal Footer -->
          <div class="d-flex justify-content-center gap-3 mt-3">
            <button
              @click="applicationAction('ACCEPTED')"
              class="btn btn-success px-4"
            >
              Accept
            </button>
            <button
              @click="applicationAction('REJECTED')"
              class="btn btn-danger px-4"
            >
              Reject
            </button>
            <button
              type="button"
              class="btn btn-secondary px-4"
              @click="closeModal"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </template>
  </Modal>
</template>

<script lang="ts" setup>
import { clientPoster } from "@/utils/api";
import { IApiRes, IProfessional } from "@/types";
import { ref } from "vue";
import { formatUnixTimestamp } from "@/utils/time";
import Modal from "../Modal.vue";

const props = defineProps<{
  showModal: boolean;
  professional: IProfessional | null;
}>();

const emit = defineEmits(["close", "refreshProfessionalApplications"]);

const errorMessage = ref("");

// Action functions
async function closeModal() {
  emit("close");
}
async function applicationAction(status: IProfessional["status"]) {
  const url = `${import.meta.env.VITE_API_URL}/admin/professional/${props.professional?.id}`; // prettier-ignore
  const res = await clientPoster<IApiRes>(url, { status });
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    emit("refreshProfessionalApplications");
  } else {
    errorMessage.value = res.data.message || "Couldn't delete profile.";
  }
}
</script>
