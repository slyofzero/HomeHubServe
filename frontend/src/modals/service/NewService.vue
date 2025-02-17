<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">New Service</h4>
        <button
          @click="closeModal"
          class="btn-close"
          aria-label="Close"
        ></button>
      </div>
    </template>

    <!-- Modal Body -->
    <template #body>
      <div class="d-flex flex-column gap-4">
        <span
          v-if="errorMessage"
          class="text-danger bg-danger-subtle rounded px-4 py-1"
          >{{ errorMessage }}</span
        >

        <form @submit.prevent="(e: Event) => e.preventDefault()">
          <!-- Service Name -->
          <div class="mb-3">
            <label for="serviceName" class="form-label">
              <strong>Service Name:</strong>
            </label>
            <input
              type="text"
              id="serviceName"
              class="form-control"
              v-model="formData.name"
              placeholder="Enter service name"
              required
            />
          </div>

          <!-- Description -->
          <div class="mb-3">
            <label for="description" class="form-label">
              <strong>Description:</strong>
            </label>
            <textarea
              id="description"
              class="form-control"
              v-model="formData.description"
              placeholder="Enter description"
              rows="3"
              required
            ></textarea>
          </div>

          <!-- Base Price -->
          <div class="mb-3">
            <label for="basePrice" class="form-label">
              <strong>Base Price:</strong>
            </label>
            <input
              id="basePrice"
              class="form-control"
              v-model="formData.base_price"
              placeholder="Enter base price"
              required
            />
          </div>

          <!-- Modal Footer -->
          <div class="d-flex justify-content-center gap-3">
            <button
              type="submit"
              @click="addModal"
              class="btn btn-primary px-4"
            >
              Add
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
import router from "@/router";
import { IApiRes } from "@/types";
import { ref } from "vue";
import Modal from "../Modal.vue";

const props = defineProps({
  showModal: {
    type: Boolean,
    required: true,
  },
});

const emit = defineEmits(["close", "refreshServices"]);

const formData = ref({
  name: "",
  description: "",
  base_price: "",
});
const errorMessage = ref("");

async function closeModal() {
  emit("close");
}
async function addModal() {
  const url = `${import.meta.env.VITE_API_URL}/service`;
  const res = await clientPoster<IApiRes>(url, formData.value);
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/admin");
    emit("refreshServices");
  } else {
    errorMessage.value = res.data.message || "Couldn't create a new service";
  }
}
</script>
