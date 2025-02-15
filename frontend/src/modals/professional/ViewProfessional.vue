<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Professional Profile</h4>
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
            <span>Application Created On</span> -
            <span
              >{{ formatUnixTimestamp(professional?.created_on) }} ({{
                timeSince(professional.created_on)
              }})</span
            >
          </div>
          <div class="d-flex gap-2">
            <span>Jobs done so far</span> -
            <span>{{ professional.jobs_done }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Rating</span> -
            <span>{{ professional.rating }}</span>
          </div>
          <AccountStatus :account="professional" />
        </div>

        <form v-if="userStore.isAdmin" @submit.prevent="() => {}">
          <!-- Modal Footer -->
          <div class="d-flex justify-content-center gap-3 flex-wrap">
            <button
              @click="applicationAction('BLOCKED')"
              class="btn btn-danger px-4"
              v-if="professional.status === 'ACCEPTED' && userStore.isAdmin"
            >
              Block
            </button>

            <button
              @click="applicationAction('ACCEPTED')"
              class="btn btn-success px-4"
              v-if="professional.status === 'BLOCKED' && userStore.isAdmin"
            >
              Unblock
            </button>

            <button
              v-if="professional.status === 'PENDING' && userStore.isAdmin"
              @click="applicationAction('ACCEPTED')"
              class="btn btn-success px-4"
            >
              Accept
            </button>
            <button
              v-if="professional.status === 'PENDING' && userStore.isAdmin"
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
import { formatUnixTimestamp, timeSince } from "@/utils/time";
import Modal from "../Modal.vue";
import { useUserStore } from "@/stores";
import { AccountStatus } from "@/components/utils";

const props = defineProps<{
  showModal: boolean;
  professional: IProfessional | null;
}>();

const emit = defineEmits(["close", "refreshProfessionals"]);
const errorMessage = ref("");
const userStore = useUserStore();

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
    emit("refreshProfessionals");
  } else {
    errorMessage.value = res.data.message || "Couldn't delete profile.";
  }
}
</script>
