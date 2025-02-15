<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header
      ><div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Delete Profile</h4>
        <button
          @click="closeModal"
          class="btn-close"
          aria-label="Close"
        ></button></div
    ></template>

    <!-- Modal Body -->
    <template #body>
      <div class="d-flex flex-column gap-4">
        <span
          v-if="errorMessage"
          class="text-danger bg-danger-subtle rounded px-4 py-1"
          >{{ errorMessage }}</span
        >

        <p class="mb-0">
          Are you sure you want to delete your profile? This action is
          <strong>unrecoverable</strong>. You would lose all data regarding the
          account, ratings, and service requests included.
        </p>

        <form @submit.prevent="deleteProfile">
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
import { useUserStore } from "@/stores";
import Modal from "../Modal.vue";

const props = defineProps({
  showModal: {
    type: Boolean,
    required: true,
  },
});

const emit = defineEmits(["close", "refreshProfessional"]);
const userStore = useUserStore();
const errorMessage = ref("");

// Action functions
async function closeModal() {
  emit("close");
}
async function deleteProfile() {
  const url = `${import.meta.env.VITE_API_URL}/professional`;
  const res = await clientDelete<IApiRes>(url);
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/");
    emit("refreshProfessional");
    userStore.setUserRole("CUSTOMER");
  } else {
    errorMessage.value = res.data.message || "Couldn't delete profile.";
  }
}
</script>
