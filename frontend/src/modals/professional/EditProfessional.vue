<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Edit Profile</h4>
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

        <p class="mb-0">
          To edit your service and years of experience you'd have to close the
          current profile and register again.
        </p>

        <div>
          <form @submit.prevent="editProfile">
            <div>
              <label for="description" class="form-label">Description</label>
              <textarea
                id="description"
                v-model="form.description"
                class="form-control shadow-none"
                rows="3"
              />
            </div>

            <!-- Modal Footer -->
            <div class="d-flex justify-content-center gap-3 mt-3">
              <button type="submit" class="btn btn-primary px-4">Edit</button>
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
      </div>
    </template>
  </Modal>
</template>

<script lang="ts" setup>
import { clientPut } from "@/utils/api";
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

const emit = defineEmits(["close", "refreshProfessional"]);

const form = ref({
  experience: "",
  service_id: "",
  description: "",
});
const errorMessage = ref("");

// Action functions
async function closeModal() {
  emit("close");
}
async function editProfile() {
  const url = `${import.meta.env.VITE_API_URL}/professional`;
  const res = await clientPut<IApiRes>(url, form.value);
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/professional");
    emit("refreshProfessional");
  } else {
    errorMessage.value = res.data.message || "Couldn't update profile.";
  }
}
</script>
