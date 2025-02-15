<template>
  <Modal :show-modal="props.showModal">
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Delete Service</h4>
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

        <p class="mb-0">
          Are you sure you want to delete this service? This action is
          <strong>unrecoverable</strong>. All professional accounts related to
          this service will consequently be delete.
        </p>

        <!-- Modal Body -->
        <form @submit.prevent="deleteService">
          <!-- Modal Footer -->
          <div class="d-flex justify-content-center gap-3 mt-3">
            <button type="submit" class="btn btn-primary px-4">Yes</button>
            <button
              type="button"
              class="btn btn-secondary px-4"
              @click="closeModal"
            >
              No
            </button>
          </div>
        </form>
      </div>
    </template>
  </Modal>
</template>

<script lang="ts" setup>
import { clientDelete } from "@/utils/api";
import router from "@/router";
import { IApiRes } from "@/types";
import { ref } from "vue";
import Modal from "../Modal.vue";

const props = defineProps({
  showModal: {
    type: Boolean,
    required: true,
  },
  service: {
    type: [Number, null],
    required: true,
  },
});

const emit = defineEmits(["close", "refreshServices"]);

const errorMessage = ref("");

// Action functions
async function closeModal() {
  emit("close");
}
async function deleteService() {
  const url = `${import.meta.env.VITE_API_URL}/service/${props.service}`;
  const res = await clientDelete<IApiRes>(url);
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/");
    emit("refreshServices");
  } else {
    errorMessage.value = res.data.message || "Couldn't delete service.";
  }
}
</script>
